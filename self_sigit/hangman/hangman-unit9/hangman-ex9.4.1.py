def choose_word(file_path, index):
    with open(r"%s" % file_path, "r") as file:
        words = file.read().split(" ")
    new_words = []
    for word in words:
        if word not in new_words:
            new_words.append(word)
    num_words = len(new_words)
    chosen_word = new_words[(index - 1) % len(words)]
    return num_words, chosen_word
