
class Geese:
    animal_list = []

    def __init__(self, name, sex, weight, sound='га-га-га', animal='гусь', daily_eggs_benefit=1, daily_norm_food=0.4):
        Geese.animal_list.append(self)
        self.name = name
        self.sex = sex
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.daily_eggs_benefit = daily_eggs_benefit
        self.daily_norm_food = daily_norm_food
        Geese.animal_list.append(self)

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def take_eggs(self, taken_eggs):
        name = self.name
        sex = self.sex
        eggs = 0
        daily_eggs_benefit = self.daily_eggs_benefit
        if sex != 'm':
            if taken_eggs <= daily_eggs_benefit:
                eggs += taken_eggs
                print(name, 'дала', str(eggs), 'шт яиц')
            else:
                print('Сегодня яиц больше не будет, животное и так отлично постаралось!')
        else:
            print(name, 'яиц не дает, зато окрас красивый.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не гусь.')


class Cows:
    animal_list = []

    def __init__(self, name, sex, weight, sound='му-му-му', animal='корова', daily_milk_benefit=15, daily_norm_food=5):
        Cows.animal_list.append(self)
        self.name = name
        self.sex = sex
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.daily_milk_benefit = daily_milk_benefit
        self.daily_norm_food = daily_norm_food

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def milk(self, taken_milk):
        name = self.name
        sex = self.sex
        milk = 0
        daily_milk_benefit = self.daily_milk_benefit
        if sex != 'm':
            if taken_milk <= daily_milk_benefit:
                milk += taken_milk
                print(name, 'дала', str(milk), 'л молока')
            else:
                print('Удой животного на сегодня закончен.')
        else:
            print(name, 'молока не дает, зато создает настроение.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не корова.')


class Sheep:
    animal_list = []

    def __init__(self, name, weight, sound='бе-бе-бе', animal='овца', month_wool_benefit=10, daily_norm_food=2):
        Sheep.animal_list.append(self)
        self.name = name
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.month_wool_benefit = month_wool_benefit
        self.daily_norm_food = daily_norm_food

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def cut_wool(self, taken_wool):
        name = self.name
        wool = 0
        month_wool_benefit = self.month_wool_benefit
        if taken_wool <= month_wool_benefit:
            wool += taken_wool
            print(name, 'дал(а)', str(wool), 'кг шерсти')
        else:
            print(name, '- в этом месяце больше не стричь, и так животное уже лысое.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не овца.')


class Hens():
    animal_list = []

    def __init__(self, name, sex, weight, sound='куд-куд-кудах', animal='курица', daily_eggs_benefit=1,
                 daily_norm_food=0.4):
        Hens.animal_list.append(self)
        self.name = name
        self.sex = sex
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.daily_eggs_benefit = daily_eggs_benefit
        self.daily_norm_food = daily_norm_food

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def take_eggs(self, taken_eggs):
        name = self.name
        sex = self.sex
        eggs = 0
        daily_eggs_benefit = self.daily_eggs_benefit
        if sex != 'm':
            if taken_eggs <= daily_eggs_benefit:
                eggs += taken_eggs
                print(name, 'дала', str(eggs), 'шт яиц')
            else:
                print('Сегодня яиц больше не будет, животное и так отлично постаралось!')
        else:
            print(name, 'яиц не дает, зато окрас красивый.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не курица.')


class Goats:
    animal_list = []

    def __init__(self, name, sex, weight, sound='ме-ме-ме', animal='коза', daily_milk_benefit=5, daily_norm_food=2):
        Goats.animal_list.append(self)
        self.name = name
        self.sex = sex
        self.weight = weight
        self.sound = sound
        self.animal = animal
        self.daily_milk_benefit = daily_milk_benefit
        self.daily_norm_food = daily_norm_food

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def milk(self, taken_milk):
        name = self.name
        sex = self.sex
        milk = 0
        daily_milk_benefit = self.daily_milk_benefit
        if sex != 'm':
            if taken_milk <= daily_milk_benefit:
                milk += taken_milk
                print(name, 'дала', str(milk), 'л молока')
            else:
                print('Удой животного на сегодня закончен.')
        else:
            print(name, 'молока не дает, зато создает настроение.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не коза.')

class Ducks:
    animal_list = []

    def __init__(self, name, sex, weight, sound='кря-кря-кря', animal='утка', daily_eggs_benefit=1,
                 daily_norm_food=0.4):
         Ducks.animal_list.append(self)
         self.name = name
         self.sex = sex
         self.weight = weight
         self.sound = sound
         self.animal = animal
         self.daily_eggs_benefit = daily_eggs_benefit
         self.daily_norm_food = daily_norm_food

    def feed(self, given_food):
         name = self.name
         daily_norm_food = self.daily_norm_food
         if given_food <= daily_norm_food:
             self.weight += given_food
             print(name, 'хочет еще разок сегодня поесть')
         else:
             print(name, 'не хочет переедать. Животное сегодня больше не кормить.')

    def take_eggs(self, taken_eggs):
        name = self.name
        sex = self.sex
        eggs = 0
        daily_eggs_benefit = self.daily_eggs_benefit
        if sex != 'm':
            if taken_eggs <= daily_eggs_benefit:
                eggs += taken_eggs
                print(name, 'дала', str(eggs), 'шт яиц')
            else:
                print('Сегодня яиц больше не будет, животное и так отлично постаралось!')
        else:
            print(name, 'яиц не дает, зато окрас красивый.')

    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не утка.')


goose1 = Geese('Серый', 'm',  3)
goose2 = Geese('Белая', 'f',  4)
cow1 = Cows('Манька', 'f',  800)
cow2 =Cows('Бычок', 'm', 1100)
sheep1 = Sheep('Барашек', 100)
sheep2 = Sheep('Кудрявый', 120)
hen1 = Hens('Ко-Ко', 'f', 3)
hen2 = Hens('Кукареку', 'm', 5)
goat1 = Goats('Рога', 'm', 110)
goat2 = Goats('Копыта', 'f', 100)
duck1 = Ducks('Кряква', 'f', 3)
duck2 = Ducks('Дональд', 'm', 7)

goose1.feed(0.4)
goose2.feed(0.5)
goose1.identify_sound('га-га-га')
goose2.identify_sound('кря')
goose1.take_eggs(1)
goose2.take_eggs(0)

cow1.feed(4)
cow2.feed(6)
cow1.identify_sound('му-му-му')
cow2.identify_sound('ббрр')
cow1.milk(15)
cow2.milk(0)

sheep1.feed(1)
sheep2.feed(3)
sheep1.identify_sound('бе-бе-бе')
sheep2.identify_sound('хрю')
sheep1.cut_wool(11)
sheep2.cut_wool(8)

hen1.feed(0.4)
hen2.feed(0.5)
hen1.identify_sound('куд-куд-кудах')
hen2.identify_sound('кря')
hen1.take_eggs(1)
hen2.take_eggs(0)

goat1.feed(4)
goat2.feed(2)
goat1.identify_sound('ме-ме-ме')
goat2.identify_sound('пшшшш')
goat1.milk(5)
goat2.milk(4)

duck1.feed(0.4)
duck2.feed(0.5)
duck1.identify_sound('га-га-га')
duck2.identify_sound('кря-кря-кря')
duck1.take_eggs(1)
duck2.take_eggs(0)

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




