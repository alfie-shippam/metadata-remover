import os
from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen.id3 import TIT2, TPE1, TALB, TCON, COMM, TCOM
from mutagen.id3 import ID3, ID3NoHeaderError

def remove_metadata(file_path):
    try:
        audio = ID3(file_path)

        tags_to_remove = ["TALB", "TCON", "COMM", "TCOM", "TPE2"]
        for tag in tags_to_remove:
            if tag in audio:
                del audio[tag]

                audio.save()
                print(f"Metadata removed from: {file_path}")

    except ID3NoHeaderError:
        print(f"No ID3 tags found in: {file_path}")
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")

def process_folder(folder_path):

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(('.mp3', '.wav', '.flac')):
            remove_metadata(file_path)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ")
    process_folder(folder_path)
    