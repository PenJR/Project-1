import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track

class DataStorage:
#MUSIC Library and Playlist
    #SAVE
    def save_music(playlist_data,filename):
        try:
            with open(filename, 'w') as json_file:
                json.dump(playlist_data, json_file, indent=4)  
            print(f"Playlist saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving playlist: {e}")

    #LOAD
    def load_music_library(self):
        try:
            with open("MusicLibrary.json", 'r') as json_file:
                library = json.load(json_file)
            print(f"Music library loaded from {MusicLibrary.json}")
            return library
        except Exception as e:
            print(f"Error loading library: {e}")


    
