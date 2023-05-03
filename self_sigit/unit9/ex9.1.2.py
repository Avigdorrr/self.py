path = input("input path: ")
action = input("enter last, rev or sort: ")
with open(r"%s" % path, "r") as file:
    text = file.read()
lines_lst = text.split("\n")
if action == "sort":
    one_line_text = " ".join(lines_lst)
    print(sorted(dict.fromkeys(one_line_text.split(' '))))
if action == "rev":
    for line in lines_lst:
        print(line[::-1])
if action == "last":
    num = int(input("enter a num: "))
    for line in lines_lst[-num:]:
        print(line)