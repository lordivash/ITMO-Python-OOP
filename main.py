# Задание 7 "Поединок" (без 6)
# Ивашкявичус Александр
# Группа K33202

from interface import *
from Fighters import *
from Exeptions import HealthError

import asyncio
import random
import time
import threading


#Функция записи информации о бойце в файл 
def write_info(fighter):
    with open('{}.txt'.format(fighter.name), 'w', encoding='utf-8') as f:
        f.write('Боец: {}\nЗдоровье: {}'.format(fighter.name, fighter.hp))
    print('Информация о бойце {} записана в одноименный файл'.format(fighter.name))

    
# Инициализация бойцов
fighter1 = Judoist('Marco')
fighter2 = Boxer('Monica')

try:
    root = tk.Tk()
    game = Game(master=root)
    game.mainloop()
    hp = int(game.value)
    
    #hp = int(input('Введите hp бойца {}, HP = '.format(fighter1.name)))
    if hp < 0: raise HealthError(hp)
    fighter1.set_hp(hp)
except HealthError as e:
    print('{}. Здоровье бойца установлено равным 100'.format(e))
except ValueError:
    print('Ошибка ввода здоровья, здоровье бойца установлено равным 100')

try:
    hp = int(input('Введите hp бойца {}, HP = '.format(fighter2.name)))
    if hp < 0: raise HealthError(hp)
    fighter2.set_hp(hp)
except HealthError as e:
    print('{}. Здоровье бойца установлено равным 100'.format(e))
except ValueError:
    print('Ошибка ввода здоровья, здоровье бойца установлено равным 100')

#Два потока для записи информации о двух бойцах
t1 = threading.Thread(target=write_info, args=(fighter1,))
t2 = threading.Thread(target=write_info, args=(fighter2,))

t1.start()
t2.start()

t1.join()
t2.join()

fighter1.ring()

if fighter1 == fighter2:
    print('Бойцы равны по силам')
else:
    print('Один из бойцов в лучшем состоянии, чем другой')

turn = random.randint(0, 1)

# Бой
while fighter1.get_hp() > 0 and fighter2.get_hp() > 0:
    if turn:
        print('Боец {} производит удар по бойцу {}!'.format(fighter1.get_name(), fighter2.get_name()))
        fighter1.hit(fighter2)
        fighter2.display()
        print()
    else:
        print('Боец {} производит удар по бойцу {}!'.format(fighter2.get_name(), fighter1.get_name()))
        fighter2.hit(fighter1)
        fighter1.display()
        print()
    
    time.sleep(0.5)
    turn = random.randint(0, 1)
    
# Конец боя, подведение итогов
else:
    if fighter1.get_hp() <= 0:
        print('Боец %s больше не может продолжать бой' % fighter1.get_name())
        print('Побеждает боец %s' % fighter2.get_name())
    else:
        print('Боец %s больше не может продолжать бой' % fighter2.get_name())
        print('Побеждает боец %s' % fighter1.get_name())


async def write_info_async(fighter):
    with open('{}_after.txt'.format(fighter.name), 'w', encoding='utf-8') as f:
        f.write('Боец: {}\nЗдоровье: {}'.format(fighter.name, fighter.hp))
    print('Информация о бойце {} записана в одноименный файл'.format(fighter.name))


async def main():
    task1 = asyncio.create_task(write_info_async(fighter1))
    task2 = asyncio.create_task(write_info_async(fighter2))
    #asyncio.wait([task1, task2])

    await task1
    await task2


asyncio.run(main())
    
