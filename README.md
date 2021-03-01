# AGTT
Automated Guitar Tablature Transcription System

Example usage:
> python main.py "<audio_path>" "<output_path>(default:output\output.json)"

Returns:
JSON file with structure:
{
    "time": time of the beat in seconds,
    "tab": list of size 6x19 i.e. 6 strings X 1 open position + 18 fret positions,
    "chord": list of chord names (str) corresponding to the notes played,
    "position": str of fret numbers from e to E string
}
