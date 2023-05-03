def sort_anagrams(list_of_strings):
    lst = []
    for i in list_of_strings:
        if is_in_list(i, lst):
            continue
        mini_lst = [i]
        for j in list_of_strings:
            if i != j and sorted(i) == sorted(j):
                mini_lst.append(j)
        lst.append(mini_lst)
    return lst

def is_in_list(element, lst):
    for n in lst:
        if element in n:
            return True
    return False