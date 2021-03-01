from preprocess.audioBreakdown import pre_process_audio
from preprocess.tablature import process_tab_model_out
from pretrained_model.loadModel import get_model
from preprocess.chord_names import get_chord
import numpy as np
from sys import argv
import os
import json
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

MODEL, NORMALISER = get_model()

def run(audio_file, model, normaliser):
    X, times = pre_process_audio(audio_file, normaliser)
    print("Predicting Tablature....")
    Y = model.predict(X)
    Y = np.array(process_tab_model_out(Y))
    print("Final Tablature!\n\n")
    results = {"results":[]}
    for i in range(Y.shape[0]):
        tab = {}
        if i%4==0:
            print("\n" + "-"*50)
        tab["time"] = times[i]
        tab["tab"] = Y[i].tolist()
        tab["chord"] = get_chord(Y[i])
        print(tab["time"])
        print(Y[i], tab["chord"])
        results["results"].append(tab)
    return results

audio_file = Path(argv[1])
output_path = "output\\output.json"
results = run(audio_file, model = MODEL, normaliser = NORMALISER)
with open(output_path, "w") as outfile:  
        json.dump(results, outfile)
print("Results saved at: ", output_path)