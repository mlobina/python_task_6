class Animals:
    pass

    animal_list = []

    def __init__(self, name, sex, weight, sound='', animal='', daily_norm_food=0):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.daily_norm_food = daily_norm_food


    def identify_sound(self, given_sound):
        name = self.name
        animal = self.animal
        sound = self.sound
        if given_sound == sound:
            print(sound, ' - это', animal)
        else:
            print(f'Возможно, так говорил Заратустра, но не {animal}.')

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть.')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def get_benefits(self):
        animal = self.animal
        print(animal, 'на ферме приносит разную пользу')


    def slaughter(self):
        animal = self.animal
        meat = self.weight
        print(animal, '- это примерно', meat, 'кг свежего мяса, если хорошо покормили')

    def act(self):
        self.identify_sound('га-га-га')
        self.feed(2)
        self.get_benefits()
        self.slaughter()


class Poultry(Animals):
    pass

    def __init__(self, name, sex, weight, sound, animal, daily_norm_food, daily_eggs_benefit=0, month_plumage=0):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food)
        self.daily_eggs_benefit = daily_eggs_benefit
        self.month_plumage = month_plumage

    def take_plumage(self, taken_plumage):
        name = self.name
        month_plumage = self.month_plumage
        plumage = 0
        if taken_plumage <= month_plumage:
            plumage += taken_plumage
            print(f'{name} дал(а) {plumage} кг пуха')
        else:
            print(f'{name} - в этом месяце больше не обдирать')


    def take_eggs(self, taken_eggs):
        name = self.name
        sex = self.sex
        eggs = 0
        daily_eggs_benefit = self.daily_eggs_benefit
        if sex != 'm':
            if taken_eggs <= daily_eggs_benefit:
                eggs += taken_eggs
                print(f'{name} дала {eggs} шт яиц')
            else:
                 print('Сегодня яиц больше не будет, животное и так отлично постаралось!')
        else:
                 print(f'{name} яиц не дает, зато окрас красивый.')

    def get_benefits(self):
        super().get_benefits()
        self.take_plumage(1)
        self.take_eggs(1)



class Geese(Poultry):

    animal_list = []

    def __init__(self, name, sex, weight, sound='га-га-га', animal='гусь', daily_norm_food=1, daily_eggs_benefit=1,
                 month_plumage=2):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food, daily_eggs_benefit, month_plumage)
        Geese.animal_list.append(self)
        Animals.animal_list.append(self)

class Hens(Poultry):

    animal_list = []

    def __init__(self, name, sex, weight, sound='куд-куд-кудах', animal='курица', daily_norm_food=1,
                 daily_eggs_benefit=1, month_plumage=1):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food, daily_eggs_benefit, month_plumage)
        Hens.animal_list.append(self)
        Animals.animal_list.append(self)

class Ducks(Poultry):

    animal_list = []

    def __init__(self, name, sex, weight, sound='кря-кря-кря', animal='утка', daily_norm_food=1,
                 daily_eggs_benefit=1, month_plumage=2):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food, daily_eggs_benefit, month_plumage)
        Ducks.animal_list.append(self)
        Animals.animal_list.append(self)


class Mammals(Animals):
    pass

    def __init__(self, name, sex, weight, sound, animal, daily_norm_food, daily_milk_benefit=0):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food)
        self.daily_milk_benefit = daily_milk_benefit


    def milk(self, taken_milk):
        name = self.name
        sex = self.sex
        milk = 0
        daily_milk_benefit = self.daily_milk_benefit
        if sex != 'm':
            if taken_milk <= daily_milk_benefit:
                milk += taken_milk
                print(f'{self.name} дала {milk} л молока')
            else:
                print('Удой животного на сегодня закончен.')
        else:
            print(f'{self.name} молока не дает, зато создает настроение.')

    def get_benefits(self):
        super().get_benefits()
        self.milk(1)


class Goats(Mammals):

    animal_list = []

    def __init__(self, name, sex, weight, sound='ме-ме-ме', animal='коза', daily_norm_food=3, daily_milk_benefit=4):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food, daily_milk_benefit)
        Goats.animal_list.append(self)
        Animals.animal_list.append(self)


class Cows(Mammals):

    animal_list = []

    def __init__(self, name, sex, weight, sound='му-му-му', animal='корова', daily_norm_food=7, daily_milk_benefit=15):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food, daily_milk_benefit)
        Cows.animal_list.append(self)
        Animals.animal_list.append(self)

class Sheep(Mammals):

    animal_list = []

    def __init__(self, name, sex, weight, sound='бе-бе-бе', animal='овца', daily_norm_food=4, month_wool_benefit=15):
        super().__init__(name, sex, weight, sound, animal, daily_norm_food)
        self.month_wool_benefit = month_wool_benefit
        Sheep.animal_list.append(self)
        Animals.animal_list.append(self)

    def cut_wool(self, taken_wool):
        wool = 0
        month_wool_benefit = self.month_wool_benefit
        if taken_wool <= month_wool_benefit:
            wool += taken_wool
            print(f'{self.name} дал(а) {wool} кг шерсти')
        else:
            print(f'{self.name}- в этом месяце больше не стричь, и так животное уже лысое.')

    def get_benefits(self):
        self.cut_wool(1)





goose1 = Geese('Серый', 'm',  3)
goose2 = Geese('Белая', 'f',  4)
cow1 = Cows('Манька', 'f',  800)
cow2 =Cows('Бычок', 'm', 1100)
sheep1 = Sheep('Барашек', 'm', 100)
sheep2 = Sheep('Кудрявый', 'm', 120)
hen1 = Hens('Ко-Ко', 'f', 3)
hen2 = Hens('Кукареку', 'm', 5)
goat1 = Goats('Рога', 'm', 110)
goat2 = Goats('Копыта', 'f', 100)
duck1 = Ducks('Кряква', 'f', 3)
duck2 = Ducks('Дональд', 'm', 7)




weight_geese = sum((x.weight for x in Geese.animal_list))
print('Общий вес всех гусей - ', weight_geese, 'кг')

max_weight = max((x.weight for x in Geese.animal_list))

for x in Geese.animal_list:
    if x.weight == max_weight:
        print('Самый тяжелый гусь - ', x.name)
        break

weight_cows = sum((x.weight for x in Cows.animal_list))
print('Общий вес всех коров - ', weight_cows, 'кг')

max_weight = max((x.weight for x in Cows.animal_list))

for x in Cows.animal_list:
    if x.weight == max_weight:
        print('Самая тяжелая корова - ', x.name)
        break

weight_sheep = sum((x.weight for x in Sheep.animal_list))
print('Общий вес всех овец - ', weight_sheep, 'кг')

max_weight = max((x.weight for x in Sheep.animal_list))

for x in Sheep.animal_list:
    if x.weight == max_weight:
        print('Самая тяжелая овца - ', x.name)
        break

weight_hens = sum((x.weight for x in Hens.animal_list))
print('Общий вес всех кур - ', weight_hens, 'кг')

max_weight = max((x.weight for x in Hens.animal_list))

for x in Hens.animal_list:
    if x.weight == max_weight:
        print('Самая тяжелая курица - ', x.name)
        break

weight_goats = sum((x.weight for x in Goats.animal_list))
print('Общий вес всех коз - ', weight_goats, 'кг')

max_weight = max((x.weight for x in Goats.animal_list))

for x in Goats.animal_list:
    if x.weight == max_weight:
        print('Самая тяжелая коза - ', x.name)
        break

weight_ducks = sum((x.weight for x in Ducks.animal_list))
print('Общий вес всех уток - ', weight_ducks, 'кг')

max_weight = max((x.weight for x in Ducks.animal_list))

for x in Ducks.animal_list:
    if x.weight == max_weight:
        print('Самая тяжелая утка - ', x.name)
        break


for x in Animals.animal_list:
    x.act()

