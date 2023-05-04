import pytest

from src.item import Item


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


def test__repr__():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'
