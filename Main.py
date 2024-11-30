import json
from Music_Library import MusicLibrary
from Playlist import Playlist
from Track import Track
from Data_Storage import DataStorage
import random

# MENUS dictionary
MENUS = {
    "main": {
        1: "Play Music",
        2: "Music Library",
        3: "Playlists",
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
                return str(choice)  # Return the choice as a string, since inputs are compared as strings
            else:
                print("Invalid choice. Please enter a number corresponding to the menu options.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
