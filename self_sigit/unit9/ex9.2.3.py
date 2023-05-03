def who_is_missing(file_name):
    with open(r"%s" % file_name, "r") as file:
        data = file.read()
    lst = data.split(",")
    for i in range(1, 10):
        if str(i) not in lst:
            number = str(i)
    with open(r"unit9/text_files/found.txt", "w") as file:
        file.write(number)
    return int(number)
