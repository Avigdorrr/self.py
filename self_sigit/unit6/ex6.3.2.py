def longest(my_list):
    return max(my_list, key=len)

def main():
    print(longest(["111", "234", "2000", "goru", "birthday", "09"]))

if __name__ == '__main__':
    main()