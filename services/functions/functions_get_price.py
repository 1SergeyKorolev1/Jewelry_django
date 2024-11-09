price_gram_silver = 70
price_gram_platinum = 2300
gold_samples = {
    '999': 7800,
    '958': 7000,
    '900/916': 6800,
    '850': 6400,
    '750': 6000,
    '583/585': 4750,
    '500/555': 3800,
    '375': 2900,
}
silver_samples = {
    '999': 80,
    '925': 73,
    '900': 70,
    '875': 68,
    '800': 63,
    '750': 60,
    '600': 47,
}
platinum_samples = {
    '999': 2600,
    '950': 2500,
    '900': 2400,
    '850': 2200,
    '800': 2100,
}
making_set = {
    'gold': 1111,
    'silver': 999,
    'platinum': 1222,
}
making_set_ = {
    'gold': 888,
    'silver': 777,
    'platinum': 888,
}

def get_sale_price(material, weight, sample_gold, sample_silver, sample_platinum,):
    result = 0
    if material == 'gold':
        if sample_gold == 'none':
            result = abs(weight) * gold_samples['500/555']
        else:
            result = abs(weight) * gold_samples[sample_gold]
    elif material == 'silver':
        if sample_silver == 'none':
            result = abs(weight) * silver_samples['600']
        else:
            result = abs(weight) * silver_samples[sample_silver]
    elif material == 'platinum':
        if sample_platinum == 'none':
            result = abs(weight) * platinum_samples['800']
        else:
            result = abs(weight) * platinum_samples[sample_platinum]
    return result

def get_making_price(material, weight):
    result = 0
    if material:
        if abs(weight) < 6:
            result = abs(weight) * making_set[material]
        else:
            result = abs(weight) * making_set_[material]

    return result
