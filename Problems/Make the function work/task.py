def closest_higher_mod_5(x):
    y = int(x / 5) * 5
    if x % 5 > 0:
        y += 5
    return y
