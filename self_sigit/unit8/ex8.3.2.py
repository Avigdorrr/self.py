dic = {"first_name": "Mariah", "last_name": "Carey",
       "birth_date": "27.03.1970", "hobbies": ["Sing", "Compose", "Act"]}
num = int(input("enter a number: "))
if num == 1:
    print(dic["last_name"])
if num == 2:
    print(dic["birth_date"][3:5])
if num == 3:
    print(len(dic["hobbies"]))
if num == 4:
    print(dic["hobbies"][-1])
if num == 5:
    dic["hobbies"].append("Cooking")
    print(dic["hobbies"])
if num == 6:
    dic["birth_date"] = int(dic["birth_date"][:2]), int(dic["birth_date"][3:5]), int(dic["birth_date"][6:])
    print(dic["birth_date"])
if num == 7:
    dic["age"] = 2023 - int(dic["birth_date"][6:])
    print(dic["age"])