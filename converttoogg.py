import os
from pydub import AudioSegment

# Function to convert wav to ogg
def convert_wav_to_ogg(wav_path, ogg_path):
    sound = AudioSegment.from_wav(wav_path)
    sound.export(ogg_path, format="ogg")

# Walk through all files in directory and subdirectories
def convert_all_wav_to_ogg(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".wav"):
                wav_path = os.path.join(dirpath, filename)
                ogg_path = os.path.splitext(wav_path)[0] + ".ogg"
                convert_wav_to_ogg(wav_path, ogg_path)
                print(f"Converted {wav_path} to {ogg_path}")

# Specify the root directory
root_dir = "C:\\Users\\natha\\Documents\\GitHub\\SoundSpindle\\data\\outputs_part4"
convert_all_wav_to_ogg(root_dir)
