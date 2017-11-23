def score(game):
    result = 0
    frame = 1
    is_half_try = True
    pin = 10
    for i in range(len(game)):
        if game[i] == '/':
            result += pin - last
        else:
            result += get_value(game[i])
        if frame < pin and get_value(game[i]) == pin:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i].lower() == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += pin - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if not is_half_try:
            frame += 1
        if is_half_try:
            is_half_try = False
        else:
            is_half_try = True
        if game[i].lower() == 'x':
            is_half_try = True
            frame += 1
    return result


def get_value(char):
    if char.isnumeric():
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
