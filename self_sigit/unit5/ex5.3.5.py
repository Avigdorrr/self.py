def distance(num1, num2, num3):
    condition1 = abs(num2-num1) == 1 or abs(num3-num1) == 1
    condition2 = (abs(num2-num1) >= 2 and abs(num2-num3) >= 2) or (abs(num3-num1) >= 2 and abs(num2-num3) >= 2)
    return condition1 and condition2
