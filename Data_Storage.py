import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track

class DataStorage:
#MUSIC LIBRARY
   def save_music_library(library):
    try:
        with open("MusicLibrary.json", 'w') as json_file:
            json.dump(library, json_file, indent=4)
        print(f"Music library saved to MusicLibrary.json")
    except Exception as e:
        print(f"Error saving library: {e}")


    def load_music_library(self):
        try:
            with open("MusicLibrary.json", 'r') as json_file:
                library = json.load(json_file)
            print(f"Music library loaded from {MusicLibrary.json}")
            return library
        except Exception as e:
            print(f"Error loading library: {e}")


#PLAYLIST

    def save_playlist(playlist_data):
        try:
            with open("playlist.json", 'w') as json_file:
                json.dump(playlist_data, json_file, indent=4)  
            print(f"Playlist saved successfully to playlist.json")
        except Exception as e:
            print(f"Error saving playlist: {e}")

    def load_playlist(self):
        try:
          
            with open("playlist.json", 'r') as json_file:
                playlist_data = json.load(json_file)  
            print(f"Playlist loaded successfully from playlist.json")
            return playlist_data  
        except FileNotFoundError:
            print(f"Error: The file playlist.json was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in playlist.json. It might be corrupted or not properly formatted.")


#QUEUE
    def save_queue(self):
        try:
            with open("queues.json", "r") as file:
                existing_tracks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_tracks = []

        current_tracks = [
            {"title": track.title, "artist": track.artist, "duration": track.duration}
            for track in self.list
        ]
        existing_tracks.extend(current_tracks)

        with open("queues.json", "w") as file:
            json.dump(existing_tracks, file, indent=4)

        print("Queues saved.")

    def load_queue(self):
        try:
            with open("queues.json", "r") as file:
                tracks = json.load(file)

            self.list = [
                Track(track["title"], track["artist"], track["album"], track["duration"]) for track in tracks
            ]
            self.total_duration = sum(track["duration"] for track in tracks)
            self.current_index = 0 if self.list else None
            print("Queues loaded.")
        except FileNotFoundError:
            print("No saved queue found.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Queue file might be corrupted.")


