def get_percentage(number, round_digits=0):
    number *= 100
    if round_digits == 0:
        number = int(number)
    number = round(number, round_digits)
    return str(number) + '%'
