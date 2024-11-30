import random
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track
from Data_Storage import DataStorage

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

# -----------------------------
# Functions to manage playback and library
# -----------------------------

def get_total_duration(queue):
    """Calculate the total duration of the tracks in the queue in mm:ss format."""
    total_seconds = sum([track.duration_seconds() for track in queue])  # sum the raw seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def validate_duration(duration):
    """Validate and fix incorrect mm:ss format like 2:0 -> 02:00"""
    parts = duration.split(":")
    if len(parts) != 2:
        raise ValueError("Invalid duration format. Expected mm:ss.")
    
    minutes, seconds = parts
    if len(minutes) < 2:
        minutes = "0" + minutes
    if len(seconds) < 2:
        seconds = "0" + seconds
    return f"{minutes}:{seconds}"

def show_play_options():
    """Display available playback options."""
    print("\nOptions:")
    print("1. Play by Track Title")
    print("2. Play by Artist Name")
    print("3. Play by Album")

def manage_play_music(library, queue):
    current_track_index = 0
    playing = False  # Ensure nothing plays until user selects what to play

    # Prompt user to choose what to play first
    while True:
        show_play_options()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please select a valid option (1-3).")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        # Based on the user choice, play by Track Title, Artist Name, or Album
        if choice == 1:  # Play by Track Title
            track_title = input("Enter track title: ").strip().lower()
            selected_tracks = [track for track in library.get_tracks() if track_title in track.title.lower()]
            if selected_tracks:
                queue.clear()
                queue.extend(selected_tracks)
                current_track_index = 0
                playing = True
                print(f"Playing all tracks matching '{track_title}'.")
            else:
                print(f"No tracks found with title containing '{track_title}'.")
        elif choice == 2:  # Play by Artist Name
            artist_name = input("Enter artist name: ").strip().lower()
            selected_tracks = [track for track in library.get_tracks() if artist_name in track.artist.lower()]
            if selected_tracks:
                queue.clear()
                queue.extend(selected_tracks)
                current_track_index = 0
                playing = True
                print(f"Playing all tracks by artist '{artist_name}'.")
            else:
                print(f"No tracks found by artist '{artist_name}'.")
        elif choice == 3:  # Play by Album
            album_name = input("Enter album name: ").strip().lower()
            selected_tracks = [track for track in library.get_tracks() if album_name in track.album.lower()]
            if selected_tracks:
                queue.clear()
                queue.extend(selected_tracks)
                current_track_index = 0
                playing = True
                print(f"Playing all tracks from album '{album_name}'.")
            else:
                print(f"No tracks found in album '{album_name}'.")
        
        if playing:
            break  # Exit the loop once music is selected and queued

    # Now show the music player options and manage playback
    while True:
        # Show current playing track
        if queue:
            print(f"\nCurrently Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        
        show_music_player_options()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:  # Play
                print("Resuming playback.")
            elif choice == 2:  # Next Track
                if queue:
                    current_track_index = (current_track_index + 1) % len(queue)
                    print(f"Next Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
                else:
                    print("No tracks are currently playing.")
            elif choice == 3:  # Previous Track
                if queue:
                    current_track_index = (current_track_index - 1) % len(queue)
                    print(f"Previous Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
                else:
                    print("No tracks are currently playing.")
            elif choice == 4:  # Toggle Repeat
                print("Toggling repeat mode.")
            elif choice == 5:  # Toggle Shuffle
                print("Toggling shuffle mode.")
            elif choice == 6:  # Clear Queue
                queue.clear()
                print("Queue has been cleared.")
                playing = False
                break  # Exit playback options
            elif choice == 7:  # Exit
                DataStorage.save(library, queue)
                print("Queue saved successfully. Exiting player.")
                break  # Exit the loop and program
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 7.")

# Other functions such as manage_music_library and manage_playlists remain unchanged.

# Ensure the main menu, play music, library, and playlist menus work with this validation.

def main():
    """Main function to handle the program's execution flow."""
    # Load existing data
    library, playlists = DataStorage.load()

    # Main menu loop
    while True:
        choice = show_menu("main")
        if choice == 1:
            manage_play_music(library, [])
        elif choice == 2:
            manage_music_library(library)
        elif choice == 3:
            manage_playlists(library, playlists)
        elif choice == 4:
            # Save data and exit
            DataStorage.save(library, playlists)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# -----------------------------
# RUN THE PROGRAM
# -----------------------------
main()
