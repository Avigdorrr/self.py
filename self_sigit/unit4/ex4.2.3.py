temp = input("Insert the temperature you would like to convert: ")
num_temp = float(temp[:-1])
if temp[-1].lower() == "f":
    print(str((5 * num_temp - 160) / 9) + "C")
else:
    print(str((9 * num_temp + 160) / 5) + "F")