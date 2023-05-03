string = input("Enter a word: ").lower().replace(" ","")
if string == string[::-1]:
    print("OK")
else:
    print("NOT")