# Automated Guitar Tablature Transcription (AGTT)

This project is focused on generating guitar tablature directly from audio files using deep learning techniques. The core model is a Convolutional Neural Network (CNN) trained to analyze the spectrograms of guitar audio and output the corresponding tablature, indicating the strings and frets that were played.

## Features

- **Automatic Guitar Tablature Generation**: Given an audio file, the model generates the guitar tablature corresponding to the input.
- **Multi-task CNN Model**: The architecture branches out into six parts to predict the string-fret combinations for each of the six guitar strings.
- **REST API**: A FastAPI-based RESTful service allows for easy integration and interaction with the model.
- **Chord Image Generation**: Generates chord diagrams based on the model's output, which can be used for visualizing the chords.

## Project Pipeline

1. **Audio Preprocessing**:
   - **Beat Tracking**: Detects beats in the audio for beat-synchronous analysis.
   - **Constant-Q Transform**: Converts the audio into spectrograms that the CNN processes.
   
2. **Model**:
   - A **Multi-task CNN** with six outputs for each guitar string, predicting the fret positions.
   - Trained on the **GuitarSet** dataset and additional labeled chord datasets.
   
3. **Backend**: - Not included in this codebase
   - The backend uses FastAPI to expose the model via a REST API.
   - The API allows uploading audio files and returns a JSON response with the tablature data.

4. **Frontend**: - Not included in this codebase
   - **File Upload**: Drag and drop or browse to upload the audio file.
   - **Audio Player**: An audio player that displays chord images and tablature while the audio plays.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ayushmall0710/AGTT.git
   cd agtt
   ```

2. Install the required dependencies:

   ```bash
   pip install -r app/requirements.txt
   ```

3. Run the application: - Not included in this codebase

   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage

### Offline
- **Run**: command to run in the local directory
> python main.py "<audio_path>" "<output_path>(default:output\output.json)"
- **Response**: A JSON object containing the tablature data:
  - String/fret combinations
  - Timestamps for each chord
```yaml
{
    "time": time of the beat in seconds,
    "tab": list of size 6x19 i.e. 6 strings X 1 open position + 18 fret positions,
    "chord": list of chord names (str) corresponding to the notes played,
    "position": str of fret numbers from e to E string
}
```

### REST API 
Not included in this codebase
- **Endpoint**: `/predict`
- **Method**: POST
- **Request**: Upload an audio file in `.wav` format.
- **Response**: A JSON object containing the tablature data:
  - String/fret combinations
  - Timestamps for each chord
```yaml
{
    "time": time of the beat in seconds,
    "tab": list of size 6x19 i.e. 6 strings X 1 open position + 18 fret positions,
    "chord": list of chord names (str) corresponding to the notes played,
    "position": str of fret numbers from e to E string
}
```

### Frontend
Not included in this codebase
- Access the application at `http://127.0.0.1:8000`.
- Upload a `.wav` file to receive the tablature output.
- View the chord diagrams synchronized with the audio playback.

## Results

The CNN model has achieved the following accuracy rates across the six guitar strings:

- E String: 95.05%
- A String: 91.54%
- D String: 86.75%
- G String: 84.00%
- B String: 85.15%
- e String: 89.78%
- **Overall Accuracy**: 88.71%

## Future Scope

- **Stem Separation**: Adding functionality to isolate guitar parts from audio files with multiple instruments.
- **Multiple Instruments**: Expanding the system to support other instruments such as piano and drums.
  
## References

1. Schörkhuber, C., & Klapuri, A. **Constant-Q Transform Toolbox for Music Processing**. [Link to paper](https://www.researchgate.net/publication/228523955_Constant-Q_transform_toolbox_for_music_processing)

2. Xi, Q., Bittner, R. M., Pauwels, J., Ye, X., & Bello, J. P. (2018). **GuitarSet: A dataset for guitar transcription**. Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR 2018), 453-460. [Link to paper](https://archives.ismir.net/ismir2018/paper/000188.pdf)

3. Osmalsky, J., Embrechts, J., Van Droogenbroeck, M., & Pierard, S. (2012). **Neural Networks for Musical Chords Recognition**. Journées d'informatique musicale. [Link to Paper](https://hdl.handle.net/2268/115963)

4. Ruder, S. (2018). **An Overview of Multi-Task Learning for Deep Learning**. [Link to article](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1224/reports/custom_116658224.pdf)

5. LeCun, Y., et al. (1998). **Gradient-Based Learning Applied to Document Recognition**. Proceedings of the IEEE, 86(11), 2278-2324. [DOI](https://doi.org/10.1109/5.726791)

6. Tio, D. (2019). **Automated Guitar Transcription with Deep Learning**. Medium. [Link to article](https://towardsdatascience.com/audio-to-guitar-tab-with-deep-learning-d76e12717f81)

---

Feel free to contribute by submitting a pull request or creating an issue!
