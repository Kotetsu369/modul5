class Berserk:

    def __init__(self, name):
        self.name = name
        self.health = 100
    def fight(self):
        self.health -= 20
#       self.health = new_health

voin1 = Berserk(input("Имя 1"))
voin2 = Berserk(input("Имя 2"))
print(voin1.name, voin1.health," vs ", voin2.name,  voin2.health)

while voin1.health > 0 and voin2.health > 0:
    who = input("Кто нападает? Введите имя:")
    if who == voin1.name:
        voin2.fight()
        print('attack voin',voin1.name,' health = ', voin1.health, 'voin', voin2.name, ' health = ', voin2.health)
    elif who == voin2.name:
        voin1.fight()
        print('attack voin', voin2.name, ' health = ', voin2.health, 'voin', voin1.name, ' health = ', voin1.health)
    else:
        print("введите правильное имя")
else:
    if voin1.health == 0:
        print('Выиграл воин', voin2.name)
    else:
        print('Выиграл воин', voin1.name)