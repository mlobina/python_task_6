class Geese:
    pass

    def __init__(self, name, sex, weight, sound='га-га-га', animal='гусь', daily_eggs_benefit=1, daily_norm_food=0.4):
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
             print('Возможно, так говорил Заратустра, но не животные на ферме.')

goose1 = Geese('Серый', 'm', 3)
goose1.identify_sound('ура')



class Cows:
    pass

    def __init__(self, name, sex, weight, sound='му-му-му', animal='корова', daily_milk_benefit=15, daily_norm_food=5):
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
             print('Возможно, так говорил Заратустра, но не животные на ферме.')

cow1 = Cows('Манька','f', 800)
cow1.milk(10)


class Sheep:
    pass

    def __init__(self, name, sex, weight, sound='бе-бе-бе', animal='овца', month_wool_benefit=10, daily_norm_food=2):
        self.name = name
        self.sex = sex
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
            print(name, 'в этом месяце больше не стричь, и так животное уже лысое.')


    def identify_sound (self, given_sound):
         name = self.name
         animal = self.animal
         sound = self.sound
         if given_sound == sound:
             print(sound, ' - это', animal)
         else:
             print('Возможно, так говорил Заратустра, но не животные на ферме.')

sheep1 = Sheep('Барашек', 'f', 100)
sheep1.cut_wool(11)


class Hens:
    pass

    def __init__(self, name, sex, weight, sound='куд-куд-кудах', animal='курица', daily_eggs_benefit=1, daily_norm_food=0.4):
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
             print('Возможно, так говорил Заратустра, но не животные на ферме.')



class Goats:
    pass

    def __init__(self, name, sex, weight, sound='ме-ме-ме', animal='коза', daily_milk_benefit=5, daily_norm_food=2):
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
             print('Возможно, так говорил Заратустра, но не животные на ферме.')



goat1 = Goats('Рога', 'f', 200)
goat2 = Goats('Копыта', 'm', 240)

goat2.milk(6)



class Ducks:
    pass

    def __init__(self, name, sex, weight, sound='кря-кря-кря', animal='утка', daily_eggs_benefit=1, daily_norm_food=0.4):
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
             print('Возможно, так говорил Заратустра, но не животные на ферме.')

duck1 = Ducks('Кряква', 'f', 3)
duck2 = Ducks('Fooo','m', 3)
duck1.take_eggs(2)






#goose1 = Geese('Серый', 3)
#goose2 = Geese('Белый', 4)
#cow1 = Cows('Манька', 800)
#sheep1 = Sheep('Барашек', 100)
#sheep2 = Sheep('Кудрявый', 120)
#hen1 = Hens('Ко-Ко', 2)
#hen2 = Hens('Кукареку', 3)
#goat1 = Goats('Рога', 200)
#goat2 = Goats('Копыта', 240)
#duck1 = Ducks('Кряква', 'f', 3)
#duck2 = Ducks('F", 'm', 3)


