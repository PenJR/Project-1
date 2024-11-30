import json
from Track import Track
from Playlist import Playlist

class DataStorage:
    def __init__(self, filename="MusicLibrary.json"):
        self.filename = filename

    @staticmethod
    def save_music(library, playlists, filename="MusicLibrary.json"):
        """Save the music library and playlists to a JSON file."""
        try:
            # Collecting music data (tracks and playlists)
            music_data = {
                "tracks": [
                    {"title": track.title, "artist": track.artist, "album": track.album, "duration": track.duration}
                    for track in library.get_tracks()
                ],
                "playlists": [
                    {"name": playlist.name, "tracks": [{"title": track.title} for track in playlist.tracks]}
                    for playlist in playlists
                ]
            }
            with open(filename, 'w') as json_file:
                json.dump(music_data, json_file, indent=4)
            print(f"Music Library saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving music library: {e}")

    @staticmethod
    def load(library, playlists, filename="MusicLibrary.json"):
        """Load music data (tracks and playlists) from a JSON file."""
        try:
            with open(filename, 'r') as json_file:
                music_data = json.load(json_file)

            # Load tracks into the library
            for track_data in music_data.get('tracks', []):
                track = Track(track_data['title'], track_data['artist'], track_data['album'], track_data['duration'])
                library.add_track(track)

            # Load playlists
            for playlist_data in music_data.get('playlists', []):
                playlist = Playlist(playlist_data['name'])
                for track_data in playlist_data.get('tracks', []):
                    track = library.search_track(track_data['title'])[0]  # assuming search_track returns a list of matching tracks
                    playlist.add_track(track)
                playlists.append(playlist)

            print(f"Music Library loaded successfully from {filename}")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in {filename}. The file might be corrupted.")
        except Exception as e:
            print(f"An error occurred while loading music data: {e}")

    def save_queue(self, queue, filename="queues.json"):
        """Save the current play queue to a file."""
        try:
            with open(filename, "w") as file:
                existing_tracks = [
                    {"title": track.title, "artist": track.artist, "duration": track.duration}
                    for track in queue
                ]
                json.dump(existing_tracks, file, indent=4)
            print("Queue saved successfully.")
        except Exception as e:
            print(f"Error saving queue: {e}")

    def load_queue(self, filename="queues.json"):
        """Load the current play queue from a file."""
        try:
            with open(filename, "r") as file:
                tracks = json.load(file)
            print("Queue loaded successfully.")
            return [Track(track["title"], track["artist"], track["album"], track["duration"]) for track in tracks]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error loading queue. No saved queue found or file corrupted.")
            return []

