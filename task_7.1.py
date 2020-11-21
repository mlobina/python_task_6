class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} min'

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration


    def __gt__(self, other):
        if not isinstance(other, Track):
            raise NotImplementedError('Can not be compared with track')
        print(self.duration > other.duration)

    def __eq__(self, other):
        if not isinstance(other, Track):
            raise NotImplementedError('Can not be compared with track')
        print(self.duration == other.duration)



class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        return [track.__str__() for track in self.tracks]

    def get_duration(self):
        return sum([track.duration for track in self.tracks])

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)

    def __str__(self):
        print(f"""Name group: {album.group}
Name album: {album.name}
Tracks:""")
        for track in (album.get_tracks()):
            print(f'       {track}')

albums = []
album = Album('50 Shades of Black', 'Covacs')
album.add_track(Track('50 Shsdes of Black', 5))
album.add_track(Track('My Love', 4))
album.add_track(Track('Diggin', 4))
albums.append(album)

album = Album('The game', 'Queen')
album.add_track(Track('Play the game', 5))
album.add_track(Track('Save me', 5))
album.add_track(Track('Coming soon', 6))
albums.append(album)

for album in albums:
    print(f'Альбом "{album.name}" группы "{album.group}":')
    for track in enumerate(album.get_tracks(), 1):
        print(f'{track[0]}. {track[1]}')
    print(f'Общая длительность альбома: {album.get_duration()} минут\n')


print(track[1].__str__())
album.__str__()

track1 = Track('Yesterday', 5)
track2 = Track('All you need is love', 6)
track3 = Track('Let it be', 5)
track2 > track1
track3 == track1