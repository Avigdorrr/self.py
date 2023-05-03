import datetime

str_date = input("Enter a date: ")
weekday = datetime.date(int(str_date[6:]), int(str_date[3:5]), int(str_date[:2])).weekday()
if weekday == 0:
    print("Monday")
elif weekday == 1:
    print("Tuesday")
elif weekday == 2:
    print("Wednesday")
elif weekday == 3:
    print("Thursday")
elif weekday == 4:
    print("Friday")
elif weekday == 5:
    print("Saturday")
elif weekday == 6:
    print("Sunday")
