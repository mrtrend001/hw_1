class SuperHero:
    people = "people"
    def __init__(self, name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return self.name

    def hpX2(self):
        return self.health_points * self.health_points

    def __str__(self):
        return f'его прозвище {self.nickname} его суперсила {self.superpower} ,его здоровье {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("batyrkhan", "jeka", "tupism", 10000, "у меня нет времени ходить на тренировки")
print(hero.names())
print(hero.hpX2())
print(hero)
print(hero.__len__())