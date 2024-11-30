import json
from Track import Track
from Playlist import Playlist
from Music_Library import MusicLibrary

class DataStorage:
    @staticmethod
    def save(library, playlists):
        """Save music library and playlists to JSON."""
        data = {
            "Music_Library": [track.__dict__ for track in library.get_tracks()],
            "Playlists": {playlist.name: [track.__dict__ for track in playlist.tracks] for playlist in playlists}
        }
        with open('MusicData.json', 'w') as file:
            json.dump(data, file, indent=4) 

    @staticmethod
    def load():
        """Load music library and playlists from JSON."""
        try:
            with open('MusicData.json', 'r') as file:
                data = json.load(file)

                library = MusicLibrary()
                playlists = []

                # Load library tracks and ensure the duration format is correct
                for track_data in data.get("Music_Library", []):
                    try:
                        # Ensure duration is in mm:ss format
                        duration = track_data["duration"]
                        if isinstance(duration, int):  # If duration is in seconds
                            minutes = duration // 60
                            seconds = duration % 60
                            duration = f"{minutes:02}:{seconds:02}"

                        track = Track(
                            title=track_data["title"],
                            artist=track_data["artist"],
                            album=track_data["album"],
                            duration=duration
                        )
                        # Check for duplicates before adding to library
                        library.add_track(track)
                    except (ValueError, KeyError) as e:
                        print(f"Skipping invalid track data: {track_data} - Error: {e}")




    
