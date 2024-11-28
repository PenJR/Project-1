import json 
from Musiclib import MusicLibrary
from Track import Track
from Playlist import Playlist

class DataStorage:
  @staticmethod
  def save(library,playlists):
    data = {
      "Music_Library": [track.__dict__ for track in library.get_tracks()],
      "Playlists" : { playlist.name : [track.__dict__ for track in playlist.get_tracks()]
                    for playlist in playlists
                   }
      }
     
    with open ('MusicData.json','w') as file:
      json.dump(data,file)
      
  @staticmethod
  def load():
    try:
      with open ('MusicData.json','r') as file:
        data = json.load(file)
        Library = MusicLibrary()
        playlists = []
      
        for track_data in data["music_library"]:
            track = Track(track_data["title"], track_data["artist"], track_data["duration"])
            Library.add_track(track)
                
             
        for playlist_name, track_data_list in data["playlists"].items():
             playlist = Playlist(playlist_name)

        for track_data in track_data_list:
                track = Track(track_data["title"], track_data["artist"], track_data["duration"])
              # playlist.add_track(track)
        playlists.append(playlist)

        return Library, playlists
      
    except FileNotFoundError:
        return MusicLibrary(), []

