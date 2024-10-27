price_gram_gold = 7000
price_gram_silver = 70
price_gram_platinum = 2300


def get_sale_price(material, weight):
    result = 0
    if material == 'gold':
        result = weight * price_gram_gold
    elif material == 'silver':
        result = weight * price_gram_silver
    elif material == 'platinum':
        result = weight * price_gram_platinum
    return result
