def add_item(cart, name, price, qty = 1):
    if qty<=0:
        raise ValueError("Quantity must be greater than zero")
    elif name in cart:
        cart[name]["qty"] += qty
    else:
        cart[name] = {"price": price, "qty": qty}
    return cart

def total(cart):
    total_amount = 0.0
    for item in cart.values():
        total_amount += item["price"] * item["qty"]
    return total_amount

def apply_discount(amount, code):
    if code == "SAVE10":
        return amount * 0.9
    elif code == "SAVE50":
        return amount * 0.5
    elif code == "":
        return amount
    else:
        raise ValueError("Invalid Discount Code")


