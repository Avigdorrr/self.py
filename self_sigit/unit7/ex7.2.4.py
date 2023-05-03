def seven_boom(end_number):
    lst = []
    for n in range(end_number+1):
        if n % 7 == 0 or contains_digit(n,7):
            lst.append("BOOM")
        else:
            lst.append(n)
    return lst

def contains_digit (number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number //= 10
    return False