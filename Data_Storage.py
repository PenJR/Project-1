import json

class DataStorage:
#MUSIC Library and Playlist
    #SAVE
    def save_music(music_data,filename):
        try:
            with open(filename, 'w') as json_file:
                json.dump(music_data, json_file, indent=4)  
            print(f"Playlist saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving playlist: {e}")

    #LOAD
    def load_music(filename):
        try:
          
            with open(filename, 'r') as json_file:
                playlist_data = json.load(json_file)  
            print(f"Playlist loaded successfully from {filename}")
            return playlist_data  
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON in playlist.json. It might be corrupted or not properly formatted.")



    
