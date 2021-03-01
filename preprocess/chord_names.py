import pychord
import numpy as np

def get_unique(a):
    a_new = []
    for i in a:
        if i not in a_new:
            a_new.append(i)
    return a_new

NOTES = np.array([["", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
       ["", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
       ["", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
       ["", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"],
       ["", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
       ["", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"]])

def get_chord(Y):
    chord = []
    notes = []
    for i in range(6):
        ind = np.argmax(Y[i])
        if ind != 0:
            notes.append(NOTES[i][ind])
    if len(notes) != 0:
        notes = get_unique(notes)
        chord = pychord.analyzer.note_to_chord(notes)
        if len(chord) > 0:
            chord = [i.chord for i in chord]
    
    return chord
    