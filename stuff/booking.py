def create_booking(bookings, booking_id, guest, nights, rate):
    if booking_id in bookings:
        raise ValueError("Booking already exists")
    elif nights < 1:
        raise ValueError("Nights must be at least 1")
    else:
        bookings[booking_id] = {"guest": guest, "nights": nights, "rate": rate}
    return bookings

def booking_cost(nights, rate):
    cost = nights * rate
    if nights >= 7:
        cost = (nights * rate) * 0.9
    return cost

def cancel_booking(bookings, booking_id):
    if booking_id not in bookings:
        raise KeyError("Booking does not exists")
    else:
        del bookings[booking_id]
    return bookings
