def squared_numbers(start, stop):
    lst = []
    while start <= stop:
        lst.append(start ** 2)
        start += 1
    return lst
