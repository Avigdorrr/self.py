def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


def main():
    print(are_lists_equal([4, 5, 6],[6, 5, 4]))

if __name__ == '__main__':
    main()