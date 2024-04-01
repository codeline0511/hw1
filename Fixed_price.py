def get_fixed_price(discount, discount_price):
    price = int((100 * discount_price) / (100 - discount))
    return price

    
