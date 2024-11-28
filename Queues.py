class Node:
    def __init__(self, track):
        self.track = track
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, track):
        new_node = Node(track)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def remove_list(self):
        self.head = None
        self.tail = None
        self.size = 0



class Queues:
    def __init__(self):
        self.list = List()
        self.current = None
        self.shuffle = False
        self.repeat = False
        self.paganation = 10
        self.total_duration = 0
