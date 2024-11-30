import random
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track
from Data_Storage import DataStorage

# MENUS dictionary
MENUS = {
    "main": {
        1: "Play Music",
        2: "Music Library",
        3: "Playlists",
        4: "Exit"
    },
    "Play Music": {
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

def manage_play_music(library, queue, repeat=False, shuffle=False):
    """Handles operations related to playing music from a queue."""
    current_track_index = 0

    while True:
        if queue:
            print(f"Total Duration: {get_total_duration(queue)}")
            print(f"Shuffled: {'Yes' if shuffle else 'No'}")
            print(f"Repeat: {'Yes' if repeat else 'No'}")
            print(f"Currently Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
            print("Tracks in Queue:")
            for i in range(current_track_index, len(queue)):
                print(f"({i+1}) {queue[i].title} – {queue[i].artist} ({queue[i].duration})")
        else:
            print("No tracks available.")

        choice = show_menu("Play Music")
        
        if choice == 1:
            print(f"Now Playing: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        elif choice == 2:
            current_track_index = (current_track_index + 1) % len(queue)
            print(f"Next Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        elif choice == 3:
            current_track_index = (current_track_index - 1) % len(queue)
            print(f"Previous Track: {queue[current_track_index].title} – {queue[current_track_index].artist}")
        elif choice == 4:
            repeat = not repeat
            print(f"Repeat is now {'on' if repeat else 'off'}.")
        elif choice == 5:
            shuffle = not shuffle
            if shuffle:
                random.shuffle(queue)  # Shuffle the queue when enabled
                print("Shuffle is now on.")
            else:
                print("Shuffle is now off.")
        elif choice == 6:
            queue.clear()  # Clear the queue
            print("Queue has been cleared.")
        elif choice == 7:
            DataStorage.save(library, queue)  # Save queue when exiting
            print("Queue saved successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_music_library(library):
    """Handles operations related to the music library."""
    while True:
        choice = show_menu("Music Library")
        
        if choice == 1:  # Add Track
            title = input("Enter track title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            duration = input("Enter duration (mm:ss): ")

            try:
                duration = validate_duration(duration)
                track = Track(title, artist, album, duration)
                library.add_track(track)
                print(f"Track '{title}' added successfully!")
            except ValueError as e:
                print(f"Error adding track: {e}")
        
        elif choice == 2:  # View all Tracks
            if library.get_tracks():
                library.display_tracks()
            else:
                print("No tracks in the library.")
        
        elif choice == 3:  # Search Tracks
            title = input("Enter track title to search: ")
            results = library.search_track(title)
            if results:
                print("Search Results:")
                for i, track in enumerate(results, 1):
                    print(f"{i}. {track}")
            else:
                print("No tracks found.")
        
        elif choice == 4:  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

def manage_playlists(library, playlists):
    """Handles operations related to playlists."""
    while True:
        choice = show_menu("Playlist")

        if choice == 1:  # Create Playlist
            name = input("Enter playlist name: ")
            if any(playlist.name == name for playlist in playlists):
                print("A playlist with that name already exists.")
            else:
                playlists.append(Playlist(name))
                print(f"Playlist '{name}' created successfully!")

        elif choice == 2:  # View all Playlists
            if playlists:
                for i, playlist in enumerate(playlists, 1):
                    print(f"{i}. {playlist.name} ({len(playlist.tracks)} tracks)")
            else:
                print("No playlists available.")
        
        elif choice == 3:  # Add Track to Playlist
            print("Select a track to add to a playlist:")
            library.display_tracks()
            track_index = int(input("Enter the track number to add: ")) - 1
            track = library.get_tracks()[track_index]
            
            print("Select a playlist:")
            for i, playlist in enumerate(playlists, 1):
                print(f"{i}. {playlist.name}")
            playlist_index = int(input("Enter the playlist number: ")) - 1
            playlists[playlist_index].add_track(track)
            print(f"Track '{track.title}' added to playlist.")

        elif choice == 4:  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

# -----------------------------
# USER INTERACTION (Frontend)
# -----------------------------

def show_menu(menu_name):
    """Displays a menu and gets user choice, ensuring input is valid."""
    print(f"\n{menu_name} Menu:")
    # Display all menu options with proper numbering
    for key, value in MENUS[menu_name].items():
        print(f"{key}. {value}")
    
    # Ensure the input is a valid menu option
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in MENUS[menu_name]:
                return choice  # Return the choice as an integer
            else:
                print("Invalid choice. Please enter a number corresponding to the menu options.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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
