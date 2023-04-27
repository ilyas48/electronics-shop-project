import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = Item.pay_rate * self.price
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        path = r'..\src\items.csv'
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            cls.all.clear()
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))
        return len(cls.all)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

# item1 = Item("Смартфон", 10000, 20)
# item2 = Item("Ноутбук", 20000, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# Item.pay_rate = 0.8  # цена со скидкой
# item1.apply_discount()

# print(item1.price)
# print(item2.price)
