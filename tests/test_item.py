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


