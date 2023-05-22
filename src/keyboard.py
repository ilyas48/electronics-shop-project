from src.item import Item


class MixinLanguage:
    """Класс и метод для смены языка на клавиатуре (раскладки клавиатуры)"""

    def __init__(self, *args):
        self.__language = 'EN'
        super().__init__(*args)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    """
        Класс Keyboard, наследник классов MixinLanguage, Item
        """

    def __int__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
