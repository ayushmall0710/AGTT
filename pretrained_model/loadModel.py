from pickle import load
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from tensorflow.keras import models

def get_model():
    model_name = "NSGD-09_h5"
    normaliser_name = "NORMALISERNN.pkl"
    model = models.load_model(f"pretrained_model/{model_name}",)
    normaliser = load(open(f"pretrained_model/{normaliser_name}", 'rb'))
    return model, normaliser