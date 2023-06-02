"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.price == 20000

def test_string_to_number():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    # TestCase #1
    try:
        item1.name = "Очень длинное наименование товара"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов"

    # TestCase #2
    try:
        item2.name = "Очень длинное наименование товара"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов"

def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path="нет такого файла")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path=r"src/items.csv")


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25

