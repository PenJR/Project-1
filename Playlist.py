import json
from Track import Track  
from Queue import Queue
class Playlist(Track):
    def __init__(self, name):
        """
        Initializes a playlist with a given name and a Queue object to manage tracks.
        """
        self.name = name
        self.tracks = []
        self.queue = Queue()  # Instance of Queue to manage the tracks
        self.total_duration = 0  # Store the total duration as a single number (in seconds)

    def place_track(self, track):
        """
        Adds a track to the playlist (via the Queue) if it is not already present.
        Returns True if the track was placed successfully, False if it already exists.
        """
        if track in self.queue.list:
            return False
        self.queue.add_tracks([track])  # Adds the track to the Queue
        return True


    def search_and_place(self, library, title, selected_index):
        """
        Searches for a track by title in the library and places the selected one into the playlist.
        Returns True if the track was placed successfully, False otherwise.
        """
        if not library:
            print("The library is empty.")
            return False

        matches = [track for track in library if title.lower() in track.title.lower()]
        if not matches:
            print("No matching tracks found.")
            return False

        if selected_index < 0 or selected_index >= len(matches):
            print("Invalid index selected.")
            return False

        return self.place_track(matches[selected_index])

    def update_playlist(self, new_tracks):
        """
        Adds multiple tracks to the playlist (via the Queue), avoiding duplicates.
        Returns a list of tracks that were successfully added.
        """
        added_tracks = []
        for track in new_tracks:
            if self.place_track(track):  # Ensure no duplicates
                added_tracks.append(track)
        return added_tracks


    def view_playlist(self):
        """
        Returns the list of tracks in the playlist.
        """
        return self.queue.list


    def play_track(self, track):
        """
        Simulates playing a track from the playlist.
        Returns True if the track exists in the playlist and can be played, False otherwise.
        """
        if track in self.queue.list:
            print(f"Playing: {track.title} by {track.artist}")
            return True
        print("Track not found in the playlist.")
        return False


    def play_all(self):
        """
        Simulates playing all tracks in the playlist in order.
        """
        if not self.queue.list:
            print("The playlist is empty.")
            return

        print(f"Playing all tracks in playlist '{self.name}':")
        for track in self.queue.list:
            print(f"Now playing: {track.title} by {track.artist}")


    def get_total_duration(self):
        """
        Returns the total duration of all tracks in the playlist (in seconds),
        by calling the Queue's get_total_duration method.
        """
        return self.queue.get_total_duration()



    def __str__(self):
        """Return a string representation of the playlist."""
        track_list = "\n".join([str(track) for track in self.tracks])
        duration = f"{self.total_duration['minutes']} min {self.total_duration['seconds']} sec"
        return f"Playlist: {self.name}\nTotal Duration: {duration}\nTracks:\n{track_list}"
