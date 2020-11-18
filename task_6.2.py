class Track:

    track_list = []

    def __init__(self, name, album, duration):
        Track.track_list.append(self)
        self.name = name
        self.album = album
        self.duration = duration

    def show(self):
        print(f'"{self.name}" - {int(self.duration)} min')


class Album:

    album_list = []

    def __init__(self, name, group, track_list=[]):
        Album.album_list.append(self)
        self.name = name
        self.group = group
        self.track_list = track_list

    def present(self):
        print(f'Let me present a new album "{self.name}" of the cool group "{self.group}"')


    def add_track(self):
        for x in Track.track_list:
            if x.album == self.name:
                self.track_list.append(x)

    def get_tracks(self):
        for x in self.track_list:
            x.show()

    def get_duration(self):
        duration = sum((x.duration for x in Track.track_list))
        print(duration)



album1 = Album('Shades of Black', 'Kovacs')
album2 = Album('The game', 'Queen')
album3 = Album('Группа крови', 'Кино')



track1 = Track('50 Shades of Black', 'Kovacs', 3)
track2 = Track('My Love', 'Kovacs', 5)
track3 = Track('Whiskey and Fun', 'Kovacs', 4)
track4 = Track('Rock it', 'Queen', 5)
track5 = Track('Save me', 'Queen', 3)
track6 = Track('Another one bites the dust', 'Queen', 5)
track7 = Track('Группа крови', 'Кино', 5)
track8 =Track('Война', 'Кино', 4)
track9 = Track('Дальше действовать будем мы', 'Кино', 4)


album1.get_tracks()


