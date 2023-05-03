def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True
