class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)
        else:
            print(f"Track '{track.title}' is already in the playlist.")

    def get_tracks(self):
        return self.tracks

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for track in self.tracks:
            print(f"- {track}")
