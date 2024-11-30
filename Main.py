import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track
from Data_Storage import DataStorage
import random

# MENUS dictionary
MENUS = {
    "main": {
        1: "Music Player",
        2: "Music Library",
        3: "Playlists",
        4: "Exit"
    },
    "Music Player": {
        1: "Play",
        2: "Next",
        3: "Previous",
        4: "Toggle Repeat",
        5: "Toggle Shuffle",
        6: "Clear Queue",
        7: "Exit"
    },
    "Music Library": {
        1: "Add Track",
        2: "View Tracks",
        3: "Search Tracks",
        4: "Go Back to Main Menu"
    },
    "Playlist": {
        1: "Create Playlist",
        2: "View Playlists",
        3: "Add Track to Playlist",
        4: "Go Back to Main Menu"
    }
}

def get_total_duration(queue):
    """Calculate the total duration of the tracks in the queue."""
    total_seconds = sum([track.get_duration_seconds() for track in queue])
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours} hr {minutes} min {seconds} sec" if hours else f"{minutes} min {seconds} sec"

def manage_play_music(library):
    """Handles operations related to playing music."""
    current_track_index = 0
    repeat = False
    shuffle = False
    queue = library.tracks[:]

    while True:
        if queue:
            print(f"\nTotal Duration: {get_total_duration(queue)}")
            print(f"Shuffled: {'Yes' if shuffle else 'No'} | Repeat: {'Yes' if repeat else 'No'}")
            print(f"Currently Playing: {queue[current_track_index]}")
            print("Queue:")
            for i, track in enumerate(queue):
                print(f"({i + 1}) {track}")
        else:
            print("\nNo tracks available.")

        choice = show_menu("Music Player")
        if choice == "1" and queue:  # Play current track
            print(f"Now Playing: {queue[current_track_index]}")
        elif choice == "2" and queue:  # Next track
            current_track_index = (current_track_index + 1) % len(queue)
            print(f"Next Track: {queue[current_track_index]}")
        elif choice == "3" and queue:  # Previous track
            current_track_index = (current_track_index - 1) % len(queue)
            print(f"Previous Track: {queue[current_track_index]}")
        elif choice == "4":  # Toggle Repeat
            repeat = not repeat
            print(f"Repeat is now {'ON' if repeat else 'OFF'}.")
        elif choice == "5":  # Toggle Shuffle
            shuffle = not shuffle
            if shuffle:
                random.shuffle(queue)
                print("Shuffle is now ON.")
            else:
                queue = library.tracks[:]  # Reset queue order
                print("Shuffle is now OFF.")
        elif choice == "6":  # Clear Queue
            queue = library.tracks[:]
            current_track_index = 0
            print("Queue reset to original order.")
        elif choice == "7":  # Exit Music Player
            break
        else:
            print("Invalid choice or no tracks available.")

def manage_music_library(library):
    """Handles operations related to the music library."""
    while True:
        choice = show_menu("Music Library")

        if choice == "1":  # Add Track
            title = input("Enter track title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            duration = input("Enter duration (mm:ss): ")
            try:
                track = Track(title, artist, album, duration)
                library.add_track(track)
                print(f"Track '{title}' added successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":  # View Tracks
            if library.tracks:
                print("\nMusic Library:")
                library.display_tracks()
            else:
                print("The music library is empty.")

        elif choice == "3":  # Search Tracks
            title = input("Enter track title to search: ")
            results = library.search_track(title)
            if results:
                print("\nSearch Results:")
                for i, track in enumerate(results, 1):
                    print(f"{i}. {track}")
            else:
                print("No matching tracks found.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

def manage_playlists(library, playlists):
    """Handles operations related to playlists."""
    while True:
        choice = show_menu("Playlist")

        if choice == "1":  # Create Playlist
            name = input("Enter playlist name: ")
            if any(playlist.name == name for playlist in playlists):
                print("A playlist with that name already exists.")
            else:
                playlists.append(Playlist(name))
                print(f"Playlist '{name}' created successfully!")

        elif choice == "2":  # View Playlists
            if playlists:
                print("\nPlaylists:")
                for i, playlist in enumerate(playlists, 1):
                    print(f"{i}. {playlist.name} ({len(playlist.tracks)} tracks)")
            else:
                print("No playlists available.")

        elif choice == "3":  # Add Track to Playlist
            playlist_name = input("Enter playlist name: ")
            playlist = next((p for p in playlists if p.name == playlist_name), None)
            if playlist:
                track_title = input("Enter track title to add: ")
                results = library.search_track(track_title)
                if results:
                    playlist.add_track(results[0])
                    print(f"Track '{results[0].title}' added to playlist '{playlist.name}'!")
                else:
                    print("Track not found.")
            else:
                print("Playlist not found.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

def show_menu(menu_name):
    """Display menu options and get user choice."""
    options = MENUS.get(menu_name, {})
    if not options:
        print(f"Invalid menu: {menu_name}")
        return None
    print(f"\n{menu_name} Menu")
    for key, value in options.items():
        print(f"{key}. {value}")
    return input("Enter your choice: ")

def main():
    """Run the main program."""
    library = MusicLibrary()
    playlists = []
    data_storage = DataStorage("MusicLibrary.json")

    # Load data from storage
    data_storage.load(library, playlists)

    while True:
        choice = show_menu("main")
        if choice == "1":
            manage_play_music(library)
        elif choice == "2":
            manage_music_library(library)
        elif choice == "3":
            manage_playlists(library, playlists)
        elif choice == "4":
            print("Saving data and exiting...")
            data_storage.save(library, playlists)
            break
        else:
            print("Invalid choice. Please try again.")
