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
            json.dump(data, file, indent=4)  # Pretty-printing for readability


    
