str = input("enter a string: ")
lst = str.split(",")
num = int(input("enter a num: "))
while (num != 9):
    if num == 1:
        print(lst)
    if num == 2:
        print(len(lst))
    if num == 3:
        prod = input("enter product to check")
        print(prod in lst)
    if num == 4:
        prod = input("enter product to check")
        print(lst.count(prod))
    if num == 5:
        prod = input("enter product to check")
        lst.remove(prod)
    if num == 6:
        prod = input("enter product to check")
        lst.append(prod)
    if num == 7:
        for prod in lst:
            if len(prod) < 3 and not prod.isalpha():
                print(prod)
    if num == 8:
        lst = list(dict.fromkeys(lst))
    num = int(input("enter a num: "))