import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track

class DataStorage:

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


