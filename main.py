from preprocess.audioBreakdown import pre_process_audio
from preprocess.tablature import process_tab_model_out
from pretrained_model.loadModel import get_model
from preprocess.chord_names import get_chord
import numpy as np
from sys import argv
import os
import warnings
warnings.filterwarnings("ignore")

MODEL, NORMALISER = get_model()

def run(audio_file, model, normaliser):
    X, times = pre_process_audio(audio_file, normaliser)
    print("Predicting Tablature....")
    Y = model.predict(X)
    Y = np.array(process_tab_model_out(Y))
    print("Final Tablature!\n\n")
    for i in range(Y.shape[0]):
        if i%4==0:
            print("\n" + "-"*50)
        print(times[i])
        print(Y[i], get_chord(Y[i]))


audio_file = "C:\\Users\\ss380\\Downloads\\IDMT-SMT-GUITAR_V2\\dataset4\\acoustic_pickup\\slow\\pop\\audio\\pop_1_130BPM.wav"
print(audio_file)
run(audio_file, model = MODEL, normaliser = NORMALISER)

