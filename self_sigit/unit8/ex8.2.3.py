def mult_tuple(tuple1, tuple2):
    lst = []
    for one in tuple1:
        for two in tuple2:
            lst.append((one, two))
            lst.append((two, one))
    return tuple(lst)