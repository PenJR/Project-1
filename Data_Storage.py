import json
from Musiclib import MusicLibrary
from Track import Track
from Playlist import Playlist

class DataStorage:
    
    @staticmethod
    def save_music_library(library):
        # Assume the input data is already a dictionary
        data = {
            "Music_Library": [track for track in library.get_tracks()]
        }
        
        with open('MusicLibrary.json', 'w') as file:
            json.dump(data, file)
    
    @staticmethod
    def load_music_library():
        try:
            with open('MusicLibrary.json', 'r') as file:
                data = json.load(file)
                library = MusicLibrary()

                for track_data in data["Music_Library"]:
                    # Assuming track_data is a dictionary already
                    track = Track(track_data["title"], track_data["artist"], track_data["duration"])
                    library.add_track(track)
                    
                return library
                
        except FileNotFoundError:
            return MusicLibrary()
    
    @staticmethod
    def save_playlists(playlists):
        # Assume the input data is already a dictionary
        data = {
            "Playlists": {
                playlist.name: [track for track in playlist.get_tracks()]
                for playlist in playlists
            }
        }
        
        with open('Playlists.json', 'w') as file:
            json.dump(data, file)
    
    @staticmethod
    def load_playlists():
        try:
            with open('Playlists.json', 'r') as file:
                data = json.load(file)
                playlists = []

                for playlist_name, track_data_list in data["Playlists"].items():
                    playlist = Playlist(playlist_name)
                    
                    for track_data in track_data_list:
                        # Assuming track_data is a dictionary already
                        track = Track(track_data["title"], track_data["artist"], track_data["duration"])
                        playlist.add_track(track)
                    
                    playlists.append(playlist)
                    
                return playlists

        except FileNotFoundError:
            return []
    
    @staticmethod
    def save(library, playlists):
        DataStorage.save_music_library(library)
        DataStorage.save_playlists(playlists)
    
    @staticmethod
    def load():
        library = DataStorage.load_music_library()
        playlists = DataStorage.load_playlists()
        return library, playlists

