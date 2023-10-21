'''Напишите программу по следующему описанию. Есть класс &quot;Воин&quot;. От него
создаются два экземпляра-юнита---. Каждому устанавливается здоровье в 100
очков. В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не
теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После
каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у
противника осталось здоровья. Как только у кого-то заканчивается ресурс
здоровья, программа завершается сообщением о том, кто одержал победу.'''
import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        
    def attack(self, enemy):
        print(f"{self.name} атакует {enemy.name}")
        enemy.health -= 20
        print(f"У {enemy.name} осталось {enemy.health} здоровья")
        
# Создаем двух юнитов
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

# Бой идет до тех пор, пока у одного из юнитов не закончится здоровье
while warrior1.health > 0 and warrior2.health > 0:
    # Выбираем случайного атакующего
    attacker = random.choice([warrior1, warrior2])
    # Выбираем противника для атаки
    enemy = warrior1 if attacker == warrior2 else warrior2
    # Атакуем
    attacker.attack(enemy)

# Выводим сообщение о победителе
if warrior1.health > 0:
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")
