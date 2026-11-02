import pytest

from stuff import cart
from stuff.cart import add_item, total, apply_discount

@pytest.fixture
def filled_cart():
    return {
        "apple": {"price":2.0, "qty": 2},
        "milk": {"price": 15.0, "qty": 1}
    }

discount = [
    ("SAVE10", 100, 90),
    ("SAVE50", 100, 50),
    ("", 100, 100)
    ]

def test_empty_cart_total_is_zero():
    assert total({}) == 0

def test_filled_cart_total(filled_cart):
    assert total(filled_cart) == 19.0

def test_adding_existing_item_increases_qty(filled_cart):
    add_item(filled_cart, "apple", 2.0, 1)
    assert filled_cart["apple"]["qty"] == 3

@pytest.mark.parametrize('code, original_amount, expected_amount', discount)
def test_apply_discount(code, original_amount, expected_amount):
    assert apply_discount(original_amount, code) == expected_amount

def test_negative_qty_raises():
    cart = {}
    with pytest.raises(ValueError): 
        add_item(cart, "egg", 1.0, -1)

