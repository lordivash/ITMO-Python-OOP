def meta_class(name, parents, attributes):
    print('Класс {} был создан метаклассом'.format(name))
    return type(name, parents, attributes)

# Класс-миксин для вывода информации о ринге
class RingMixin(metaclass=meta_class):
    def ring(self):
        print('Информация о ринге:')
        print('Название: FighterClub\n')
