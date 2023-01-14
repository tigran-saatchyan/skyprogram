def set_suffix(number):
    number %= 100

    if 11 <= number <= 14:
        return "ев"

    number %= 10

    if number >= 5:
        return "ев"
    elif number < 2:
        if number == 0:
            return "ев"
        else:
            return "й"
    else:
        return "я"
