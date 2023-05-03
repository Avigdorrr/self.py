def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for char in secret_word:
        if char in old_letters_guessed:
            result += char
        else:
            result += "_"
    return " ".join(result)
