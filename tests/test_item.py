import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def item1():
    return Item("Смартфон", 1000, 2)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 2000


def test_apply_discount(item1):
    Item.pay_rate = 0.85
    assert item1.apply_discount() == 850


def test_string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number(5.0) == 5
    assert Item.string_to_number(5.5) == 5


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    with pytest.raises(Exception, match='Длина наименования товара превышает 10 символов.'):
        item.name = 'СуперСмартфон'


def test_name_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.name = 'iPhone 14'
    assert phone1.number_of_sim == 2


def test__repr__():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_repr_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test__str__():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'


def test_str_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test__str__():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.language == "EN"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == 'RU'
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang().change_lang()
    assert kb.language == 'EN'
