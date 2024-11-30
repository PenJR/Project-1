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
    "Playback Options": {
        1: "Play by Track Title",
        2: "Play by Artist Name",
        3: "Play by Album",
        4: "Exit"
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

def show_music_player_options():
    """Display available music player options based on MENUS dictionary."""
    print("\nMusic Player Options:")
    # Loop through the 'Music Player' options in the MENUS dictionary
    for key, value in MENUS["Music Player"].items():
        print(f"{key}. {value}")

def show_playback_options():
    """Display available playback options based on MENUS dictionary."""
    print("\nPlayback Options:")
    # Loop through the 'Playback Options' in the MENUS dictionary
    for key, value in MENUS["Playback Options"].items():
        print(f"{key}. {value}")

def manage_play_music(library, queue):
    current_track_index = 0
    playing = False  # Ensure nothing plays until user selects what to play

    # Prompt user to choose what to play first
    while True:
        show_playback_options()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a valid option (1-4).")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
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
        elif choice == 4:  # Exit to previous menu
            print("Going back to the previous menu...")
            return  # Return to the previous menu when the user selects option 4

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
def manage_music_library(library):
    """Handles operations related to the music library, including CRUD for Tracks."""
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
                print(f"Error adding track: {e}")

        elif choice == "2":  # View all Tracks
            if library.get_tracks():
                print("\nMusic Library:")
                library.display_tracks()
                track_index = int(input("Enter track number to modify (0 to skip): ")) - 1
                if 0 <= track_index < len(library.get_tracks()):
                    track = library.get_tracks()[track_index]
                    print(f"Selected Track: {track}")
                    action_choice = input("1. Update  2. Delete  3. Discard: ")
                    if action_choice == "1":
                        # Update Track
                        new_title = input(f"Enter new title (leave blank to keep '{track.title}'): ") or track.title
                        new_artist = input(f"Enter new artist (leave blank to keep '{track.artist}'): ") or track.artist
                        new_album = input(f"Enter new album (leave blank to keep '{track.album}'): ") or track.album
                        new_duration = input(f"Enter new duration (leave blank to keep '{track.duration}'): ") or track.duration

                        # Update track details
                        track.title = new_title
                        track.artist = new_artist
                        track.album = new_album
                        track.duration = new_duration

                        print(f"Track '{track.title}' updated successfully!")
                    elif action_choice == "2":
                        # Delete Track
                        library.get_tracks().remove(track)
                        print(f"Track '{track.title}' deleted successfully!")
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid track number.")
            else:
                print("The music library is empty.")

        elif choice == "3":  # Search Tracks
            title = input("Enter track title to search: ")
            results = library.search_track(title)
            if results:
                print("\nSearch Results:")
                for i, track in enumerate(results, 1):
                    print(f"{i}. {track}")
                track_index = int(input("Enter track number to modify (0 to skip): ")) - 1
                if 0 <= track_index < len(results):
                    track = results[track_index]
                    print(f"Selected Track: {track}")
                    action_choice = input("1. Update  2. Delete  3. Discard: ")
                    if action_choice == "1":
                        # Update Track
                        new_title = input(f"Enter new title (leave blank to keep '{track.title}'): ") or track.title
                        new_artist = input(f"Enter new artist (leave blank to keep '{track.artist}'): ") or track.artist
                        new_album = input(f"Enter new album (leave blank to keep '{track.album}'): ") or track.album
                        new_duration = input(f"Enter new duration (leave blank to keep '{track.duration}'): ") or track.duration

                        # Update track details
                        track.title = new_title
                        track.artist = new_artist
                        track.album = new_album
                        track.duration = new_duration

                        print(f"Track '{track.title}' updated successfully!")
                    elif action_choice == "2":
                        # Delete Track
                        library.get_tracks().remove(track)
                        print(f"Track '{track.title}' deleted successfully!")
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid track number.")
            else:
                print("No tracks found with that title.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")

def manage_playlists(library, playlists):
    """Handles operations related to playlists, including CRUD."""
    while True:
        choice = show_menu("Playlist")

        if choice == "1":  # Create Playlist
            name = input("Enter playlist name: ")
            if any(playlist.name == name for playlist in playlists):
                print("A playlist with that name already exists.")
            else:
                playlists.append(Playlist(name))
                print(f"Playlist '{name}' created successfully!")

        elif choice == "2":  # View all Playlists
            if playlists:
                print("\nPlaylists:")
                for i, playlist in enumerate(playlists, 1):
                    print(f"{i}. {playlist.name} ({len(playlist.tracks)} tracks)")
                playlist_index = int(input("Enter playlist number to modify (0 to skip): ")) - 1
                if 0 <= playlist_index < len(playlists):
                    playlist = playlists[playlist_index]
                    print(f"Selected Playlist: {playlist.name}")
                    action_choice = input("1. Add Track  2. View Tracks  3. Discard: ")
                    if action_choice == "1":
                        track_title = input("Enter track title to add: ")
                        track = library.search_track(track_title)
                        if track:
                            playlist.add_track(track[0])
                            print(f"Track '{track[0].title}' added to playlist '{playlist.name}'!")
                        else:
                            print("Track not found.")
                    elif action_choice == "2":
                        playlist.display_tracks()
                    else:
                        print("Changes discarded.")
                else:
                    print("Invalid playlist number.")
            else:
                print("No playlists available.")

        elif choice == "3":  # Add Track to Playlist
            playlist_name = input("Enter playlist name to add a track to: ")
            playlist = next((p for p in playlists if p.name == playlist_name), None)
            if playlist:
                track_title = input("Enter track title to add: ")
                track = library.search_track(track_title)
                if track:
                    playlist.add_track(track[0])
                    print(f"Track '{track[0].title}' added to playlist '{playlist.name}'!")
                else:
                    print("Track not found.")
            else:
                print("Playlist not found.")

        elif choice == "4":  # Go Back
            break
        else:
            print("Invalid choice. Please try again.")
            
def show_menu(menu_name):
    """Show the appropriate menu based on the selected category."""
    options = MENUS.get(menu_name, {})
    if not options:
        print(f"Invalid menu: {menu_name}")
        return None
    print(f"\n{menu_name} Menu")
    for key, value in options.items():
        print(f"{key}. {value}")
    return input("Enter your choice: ")
# Other functions such as manage_music_library and manage_playlists remain unchanged.

# Ensure the main menu, play music, library, and playlist menus work with this validation.

def main():
    """Main function to handle the program's execution flow."""
    # Load existing data
    library, playlists = DataStorage.load()

    # Main menu loop
    while True:
        # Assuming `show_menu()` is a function that displays the main menu and returns the user's choice
        print("\nMain Menu:")
        for key, value in MENUS["main"].items():
            print(f"{key}. {value}")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

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
