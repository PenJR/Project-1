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
