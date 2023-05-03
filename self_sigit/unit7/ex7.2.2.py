def numbers_letters_count(my_str):
    number = 0
    not_number = 0
    for char in my_str:
        if char.isnumeric():
            number += 1
        else:
            not_number += 1
    return [number, not_number]