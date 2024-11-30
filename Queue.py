import json
import random

class Queue:
    def __init__(self):
        self.list = []
        self.current = None
        self.shuffle = False
        self.repeat = False
        self.pagination = 10
        self.total_duration = 0
        self.current_index = None  # Initialize current_index

    def play(self):
        if self.shuffle:
            shuffled_queue = random.sample(self.list, len(self.list))
            self.current_index = 0
            print(f"Playing: {shuffled_queue[self.current_index]}")
        elif self.current_index is None:
            print("No track is currently playing.")
        else:
            print(f"Playing: {self.list[self.current_index]}")

    def skip(self):
        if self.current is None:
            print("No track is currently playing.")
            return
        
        if self.current.next is None and not self.repeat:
            print("End of the queue. No more tracks to skip to.")
            return
        
        if self.repeat:
            self.current = self.list.head.track
            print(f"Playing: {self.current}")
        else:
            self.current = self.current.next.track if self.current.next else None
            if self.current:
                print(f"Playing: {self.current}")
            else:
                print("End of the queue.")

    def previous(self):
        if self.current is None:
            print("No track is currently playing.")
            return
        
        if self.current.prev is None:
            print("No previous track. You are at the start of the queue.")
            return
        
        self.current = self.current.prev.track
        print(f"Playing: {self.current}")

    def toggle_shuffle(self):
        self.shuffle = not self.shuffle
        status = "enabled" if self.shuffle else "disabled"
        print(f"Shuffle is now {status}.")

    def toggle_repeat(self):
        self.repeat = not self.repeat
        print(f"Repeat mode is now {'enabled' if self.repeat else 'disabled'}.")