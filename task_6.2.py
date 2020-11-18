class Track:
    track_list = []

    def __init__(self, name, duration):
        Track.track_list.append(self)
        name = self.name
        duration = self.duration

    def show(self):
        print(self.name, int(self.duration))

track1 = Track('The Celebration Song', 2)
track1.show()