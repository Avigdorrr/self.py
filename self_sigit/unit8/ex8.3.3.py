def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != " " and char not in my_dict.keys():
            my_dict[char] = my_str.count(char)
    return my_dict