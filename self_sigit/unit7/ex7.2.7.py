def arrow(my_char, max_length):
    for number in range(1,max_length + 1):
        print(" ".join(my_char * number))
    for number in range(max_length - 1, 0, -1):
        print(" ".join(my_char * number))