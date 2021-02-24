import librosa
import numpy as np
from preprocess.audioCQTransform import audio_CQT

def beats(y, sr):
#     y = highpass_filter(y, sr)

    o_env = librosa.onset.onset_strength(y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(o_env)), sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    tempo, beats_time = librosa.beat.beat_track(onset_envelope=o_env,sr=sr)
    return librosa.frames_to_time(beats_time)

def pre_process_audio(audio_file, normaliser, sampling_dur=0.2):
    # Load audio and define paths
    print(audio_file)
    duration = librosa.get_duration(filename = audio_file)
    print("Loading Audio File....")
    data, _ = librosa.load(audio_file)
    print("Tracking Beats....")
    time = beats(data, _)
    X = []
    print("Performing CQ Transform....")
    for j in time:
        if j + sampling_dur < duration:
            image = audio_CQT(audio_file, j, sampling_dur)
            X.append(image.flatten())
    X = np.array(X)
    print("Normalising Data....")
    X = normaliser.transform(X)
    X = np.array([x.reshape(96,9) for x in X])
    X = X.reshape(X.shape[0],96,9,1)
    print("Data Pre-processed!")
    return (X, time)