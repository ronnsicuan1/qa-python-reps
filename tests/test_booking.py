import pytest

from stuff.booking import create_booking, booking_cost, cancel_booking

@pytest.fixture
def bookings():
    return{
    "B1": {"guest": "Ronn", "nights": 2, "rate": 500.0},
    "B2": {"guest": "Athena", "nights": 3, "rate": 200.0}
    }

cost = [
    (1, 99.9, 99.9), (6, 99.9, 599.4), (7, 99.9, 629.37)
]

def test_create_booking_adds_entry(bookings):
    create_booking(bookings, "B3", "Rene", 2, 700.0)
    assert len(bookings) == 3
    assert bookings["B3"]["guest"] == "Rene"

def test_duplicate_id_raises(bookings):
    with pytest.raises(ValueError, match="already exists"): 
        create_booking(bookings, "B1", "Rene", 1, 100.0)

@pytest.mark.parametrize('nights', [0,-1])
def test_invalid_nights_raises(bookings, nights):
    with pytest.raises(ValueError, match = 'Nights must be at least 1'):
        create_booking(bookings, 'B3', 'Kingsley', nights, 500.0)

@pytest.mark.parametrize('nights, rate, expected_output', cost)
def test_booking_cost(nights, rate, expected_output):
    assert booking_cost(nights, rate) == pytest.approx(expected_output)

def test_cancel_removes_booking(bookings):
    cancel_booking(bookings, 'B1')
    assert 'B1' not in bookings

def test_cancel_missing_raises(bookings):
    with pytest.raises(KeyError, match="Booking does not exists"):
        cancel_booking(bookings, 'B99')



