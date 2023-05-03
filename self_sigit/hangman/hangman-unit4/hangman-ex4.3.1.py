guessed_char = input("Guess a letter: ").lower()
if (len(guessed_char) > 1) and not (guessed_char.isalpha()):
    print("E3")
elif not guessed_char.isalpha():
    print("E2")
elif len(guessed_char) > 1:
    print("E1")
else:
    print(guessed_char)