class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def show_name(self):
        return self.name

    def healthpower(self):
        return self.health_points * 2

    def __str__(self):
        return f"nickname - {self.nickname}\nsuperpower - {self.superpower}\nhealth_points - {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

boss = SuperHero('Abu', 'boss', 'fire', 200, 'abu bandit iiiuuuuu')
print(boss.show_name())
print(boss.healthpower())
print(boss)
print(boss.__len__())




