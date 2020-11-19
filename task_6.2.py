class Track:
    my_track_list = []

    def __init__(self, name, album, duration):  # атрибут album добавлен для автоматизации добавления треков в альбом
        Track.my_track_list.append(self)
        self.name = name
        self.album = album
        self.duration = duration

    def show(self):
        print(f'"{self.name}" - {int(self.duration)} min')


class Album:
    my_album_list = []

    def __init__(self, name, group):
        Album.my_album_list.append(self)
        self.name = name
        self.group = group
        self.track_list = []

    def present(self):
        print(f'Let me present a new album "{self.name}" of the cool group "{self.group}"')

    def add_track(self, track_name):
        self.track_name = track_name
        for x in Track.my_track_list:
            if track_name == x.name:
                self.track_list.append(x)

    def add_tracks(self):  # добавить в альбом сразу все треки, относящиеся к этому альбому
        for x in Track.my_track_list:
            if self.name == x.album:
                self.track_list.append(x)

    def get_tracks(self):
        for x in self.track_list:
            x.show()

    def get_duration(self):
        duration = sum((x.duration for x in self.track_list))
        print(f'The whole duration of the album "{self.name}" is {duration} min')


album1 = Album('Shades of Black', 'Kovacs')
album2 = Album('The game', 'Queen')
album3 = Album('Группа крови', 'Кино')

track1 = Track('50 Shades of Black', 'Shades of Black', 3)
track2 = Track('My Love', 'Shades of Black', 5)
track3 = Track('Whiskey and Fun', 'Shades of Black', 4)
track4 = Track('Rock it', 'The game', 5)
track5 = Track('Save me', 'The game', 3)
track6 = Track('Another one bites the dust', 'The game', 5)
track7 = Track('Группа крови', 'Группа крови', 5)
track8 = Track('Война', 'Группа крови', 4)
track9 = Track('Дальше действовать будем мы', 'Группа крови', 4)
track10 = Track('Звезда по имени Солнце', 'Группа крови', 4)

album1.present()
album1.add_tracks()
album1.get_tracks()
album1.get_duration()

album2.present()
album2.add_tracks()
album2.get_tracks()
album2.get_duration()

album3.present()
album3.add_tracks()
album3.get_tracks()
album3.get_duration()
