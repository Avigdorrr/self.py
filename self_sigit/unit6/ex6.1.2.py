def shift_left(my_list):
    a, b, c = my_list
    my_list = b, c, a
    return my_list

def main():
    print(shift_left([1, 2, 3]))

if __name__ == '__main__':
    main()