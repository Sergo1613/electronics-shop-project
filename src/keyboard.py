from src.item import Item


class MixinLanguage:
    """Миксин по смене языка на клавиатуре"""

    def __init__(self):
        self.__language = 'EN'


    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLanguage):
    """Класс, определяющий товар "Клавиатура"""
    def __int__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name