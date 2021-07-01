from RingMixin import RingMixin
from abc import ABC, abstractmethod


#def check_hp(func):
#    def wrapper(self):
#        if self.hp < 0:
#            self.hp = 100
#            print('Здоровье бойца установлено равным 100')
#        else:
#            print('Все в порядке')
#        return func(self)
#    return wrapper


def notify(func):
    def wrapper(self, *args):
        print('Произошел вызов функции {}'.format(func.__name__))
        return func(self, *args)
    return wrapper


# Базовый абстрактный класс боец
class Fighter(ABC, RingMixin):
    def __init__(self, name):
        self.name = name
        self.hp = 100

    # Отображение состояния бойца (абстрактный метод)
    @abstractmethod
    def display(self):
        print('Fighter {}, HP = {}'.format(self.name, self.hp))
    
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    # Функция "Принять удар"
    @notify
    def take_hit(self):
        self.hp -= 20

    # Функция "Нанести удар"
    def hit(self, target):
        target.take_hit()

    # Переопределение оператора ==
    def __eq__(self, other):
        if self.hp == other.hp:
            return True
        else:
            return False


# Производные класс Боксер
class Boxer(Fighter):
    def display(self):
        print('Boxer {}, HP = {}'.format(self.name, self.hp))


# Производный класс дзюдоист
class Judoist(Fighter):  
    def display(self):
        print('Judoist {}, HP = {}'.format(self.name, self.hp))


