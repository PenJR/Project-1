from Track import Track

class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def add_track(self, track):
        if self.duplicate(track):
            return "Track already exist."
        else:
            self.tracks.append(track)
            self.tracks.sort(key=Track.sort)

    def duplicate(self, new_track):
        for track in self.tracks:
            if (track.title == new_track.title and
                track.album == new_track.album and
                track.artist == new_track.artist):
                return True
            return False
     
    def display_tracks(self):
        if not self.tracks:
            return('No tracks in the library.')
        else:
            for i, track in enumerate(self.tracks):
                return(f"[{i + 1}] {track}")
    
    def search_track(self, title):
        if not title:
            return []
        else:
            return [track for track in self.tracks if title.lower() in track.title.lower()]
        
    def validate_duration(self, duration):
        try:
            mins, seconds = map(int, duration.split(':'))
            return mins >= 0 and 0 <= seconds < 60
        except ValueError:
            return False


class Track:
    def __init__(self, title, artist, album, duration, additional_artist):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.additional_artist = [additional_artist] if isinstance(additional_artist, str) else additional_artist or []

    def getDuration(self):
        mins, seconds = int(self.duration.split(':')[0]), int(self.duration.split(':')[1])
        return mins * 60 + seconds

    def getDurationstr(self):
        total_seconds = self.getDuration()
        mins = total_seconds // 60
        seconds = total_seconds % 60
        return f'{mins:02}:{seconds:02}'
    
    def sort(self):
        return self.title.lower(), self.artist.lower(), self.album.lower(), self.duration

    def __str__(self):
        add = ", ".join(self.additional_artist) if self.additional_artist else 'No additional artists'
        return f'Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nDuration: {self.duration}\nAdditional Artist: {add}\n'