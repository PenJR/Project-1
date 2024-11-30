import json
from Track import Track 
class DataStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, library, playlists):
        """Save library and playlists to the JSON file."""
        data = {
            "Music_Library": [
                {
                    "title": track.title,
                    "artist": track.artist,
                    "album": track.album,
                    "duration": track.duration_seconds()  # Save duration in seconds for consistency
                } for track in library.get_tracks()
            ],
            "Playlists": {
                playlist.name: [
                    {
                        "title": track.title,
                        "artist": track.artist,
                        "album": track.album,
                        "duration": track.duration_seconds()
                    } for track in playlist.tracks
                ] for playlist in playlists
            }
        }
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved successfully to {self.filepath}")

    def load(self, library, playlists):
        """Load library and playlists from the JSON file."""
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)

            # Load music library
            if "Music_Library" in data:
                for track_data in data["Music_Library"]:
                    track = Track(
                        title=track_data["title"],
                        artist=track_data["artist"],
                        album=track_data["album"],
                        duration=f"{track_data['duration'] // 60}:{track_data['duration'] % 60:02}"
                    )
                    library.add_track(track)

            # Load playlists
            if "Playlists" in data:
                for playlist_name, tracks in data["Playlists"].items():
                    playlist = Playlist(playlist_name)
                    for track_data in tracks:
                        track = Track(
                            title=track_data["title"],
                            artist=track_data["artist"],
                            album=track_data["album"],
                            duration=f"{track_data['duration'] // 60}:{track_data['duration'] % 60:02}"
                        )
                        playlist.add_track(track)
                    playlists.append(playlist)

            print(f"Data loaded successfully from {self.filepath}")
        except FileNotFoundError:
            print(f"No existing data file found at {self.filepath}. Starting fresh.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON file at {self.filepath}.")
