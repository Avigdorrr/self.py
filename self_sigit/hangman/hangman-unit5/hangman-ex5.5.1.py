def is_valid_input(letter_guessed):
    letter_guessed = letter_guessed.lower()
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha())
