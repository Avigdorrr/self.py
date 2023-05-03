def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

def main():
    print(extend_list_x([4, 5, 6],[1,2,3]))

if __name__ == '__main__':
    main()