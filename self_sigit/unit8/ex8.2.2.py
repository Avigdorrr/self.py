def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=key_func, reverse=True)

def key_func(lst):
    return float(lst[1])