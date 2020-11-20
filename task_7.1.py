class Track:
    def __init__(self, name='', duration=0):
        self.name = name
        self.duration = duration

    def show(self):
        return f'<{self.name} - {self.duration}>'

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration


class Album:
    def __init__(self, name='', group=''):
        self.name = name
        self.group = group
        self.tracks = []

    def get_tracks(self):
        return [track.show() for track in self.tracks]

    def get_duration(self):
        return sum([track.duration for track in self.tracks])

    def add_track(self, track):
        if not isinstance(track, Track):
            raise NotImplementedError('Can not add this object to track list')
        self.tracks.append(track)

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


