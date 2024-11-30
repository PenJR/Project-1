from Track import Track

class Playlist(Track):
    def __init__(self, name):
        self.name = name
        self.tracks = []
        self.total_duration = 0