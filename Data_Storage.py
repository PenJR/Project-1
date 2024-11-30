import json

class DataStorage:
#MUSIC Library and Playlist
    #SAVE
    def save_music(music_data):
        try:
            with open("Music_Data.json", 'w') as json_file:
                json.dump(music_data, json_file, indent=4)  
            print(f"Playlist saved successfully to Music_Data}")
        except Exception as e:
            print(f"Error saving playlist: {e}")

    #LOAD
    def load_music(self):
        try:
          
            with open("Music_Data.json", 'r') as json_file:
                playlist_data = json.load(json_file)  
            print(f"Playlist loaded successfully from Music_Data.json")
            return playlist_data  
        except FileNotFoundError:
            print(f"Error: The file Music_Data.json was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in Music_Data.json, It might be corrupted or not properly formatted.")

    def save_playlist(self, file_path="Playlist.json"):
        """Save the playlist to a JSON file."""
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data[self.name] = {
            "Playlist Name": self.name,
            "Total Duration": f"{self.total_duration[0]} min {self.total_duration[1]} sec",
            "Tracks": [
                {
                    "Title": track.title,
                    "Artist": track.artist,
                    "Album": track.album,
                    "Duration": track.duration,
                }
                for track in self.tracks
            ],
        }


        try:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            print(f"Playlist '{self.name}' saved successfully.")
        except Exception as e:
            print(f"Error saving playlist: {e}")


    
