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
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

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
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all = []
        with open("src/items.csv", newline='') as csvfile:
            data = csv.DictReader(csvfile)
            for row in data:
                cls(row['name'], row['price'], int(row['quantity']))
            return cls.all

    @staticmethod
    def string_to_number(string: str):
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        try:
            return int(string)
        except ValueError:
            num = int(string[0])
            return num

