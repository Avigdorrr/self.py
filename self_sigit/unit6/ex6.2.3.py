def format_list(my_list):
    return ", ".join(my_list[::2]) + " and " + my_list[-1]

def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

if __name__ == '__main__':
    main()