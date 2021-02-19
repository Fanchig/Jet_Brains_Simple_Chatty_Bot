def closest_higher_mod_5(x):
    remainder = x % 5  # 3
    if remainder == 0:
        return x
    return x + 5 - remainder
