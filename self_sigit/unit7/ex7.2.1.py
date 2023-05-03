def is_greater(my_list, n):
    lst = []
    for number in my_list:
        if number > n:
            lst.append(number)
    return lst