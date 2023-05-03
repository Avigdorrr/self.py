HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6

picture1 = "    x-------x"
picture2 = """    x-------x
    |
    |
    |
    |
    |"""
picture3 = """    x-------x
    |       |
    |       0
    |
    |
    |"""
picture4 = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""
picture5 = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""
picture6 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""
picture7 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

HANGMAN_PHOTOS = {0: picture1, 1: picture2, 2: picture3, 3: picture4, 4: picture5, 5: picture6, 6: picture7}


def choose_word(file_path, index):
    """chooses a word from the words file.
        :param file_path: the words file path
        :param index: the index of word to choose
        :type index: int
        :type file_path: str
        :return: The chosen word
        :rtype: str
        """
    with open(r"%s" % file_path, "r") as file:
        words = file.read().split(" ")
    new_words = []
    for word in words:
        if word not in new_words:
            new_words.append(word)
    chosen_word = new_words[(index - 1) % len(words)]
    return chosen_word


def check_win(secret_word, old_letters_guessed):
    """return boolean value based on if the whole word has been guessed.
        :param secret_word: the word that needs to be guessed
        :param old_letters_guessed: list of all guessed values
        :type secret_word: str
        :type old_letters_guessed: lst
        :return: boolean value based on if the whole word has been guessed
        :rtype: bool
        """
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """return string that hide the letter that has not been guessed.
        :param secret_word: the word that needs to be guessed
        :param old_letters_guessed: list of all guessed values
        :type secret_word: str
        :type old_letters_guessed: lst
        :return: string that hide the letter that has not been guessed
        :rtype: str
        """
    result = ""
    for char in secret_word:
        if char in old_letters_guessed:
            result += char
        else:
            result += "_"
    return " ".join(result)


def check_valid_input(letter_guessed, old_letters_guessed):
    """return boolean value based on if the input is a valid letter.
        :param letter_guessed: the letter that been guessed
        :param old_letters_guessed: list of all guessed values
        :type letter_guessed: str
        :type old_letters_guessed: lst
        :return: boolean value based on if the input is a valid letter
        :rtype: bool
        """
    letter_guessed = letter_guessed.lower()
    return (len(letter_guessed) == 1) and (letter_guessed.isalpha()) and letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """return boolean value based on if the input is a valid letter.
    if it is, its added to the list of guessed letter and returns True, else prints the list and returns False
        :param letter_guessed: the letter that been guessed
        :param old_letters_guessed: list of all guessed values
        :type letter_guessed: str
        :type old_letters_guessed: lst
        :return: boolean value based on if the input is a valid letter
        :rtype: bool
        """
    if check_valid_input(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X\n" + " -> ".join(old_letters_guessed))
    return False


def show_start_page():
    """prints the start page of the game.
        :return: None
        :rtype: None
        """
    print(f"{HANGMAN_ASCII_ART}\nYou have {MAX_TRIES}, guesses")


def print_hangman(num_of_tries):
    """prints the hangman based on tries that been left.
        :param num_of_tries: number of tries that failed in game
        :type num_of_tries: int
        :return: None
        :rtype: None
        """
    print(HANGMAN_PHOTOS[num_of_tries])


def init_game(secret_word):
    """managing the game.
        :param secret_word: the word that needs to be guessed
        :type secret_word: str
        :return: None
        :rtype: None
        """
    num_of_tries = 0
    old_letters_guessed = []
    print("lets start the game :)\n")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while True:
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if letter_guessed not in secret_word:
                num_of_tries += 1
                print(":(\n")
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
                if num_of_tries == MAX_TRIES:
                    print("LOSE")
                    break
            else:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed):
                    print("WIN")
                    break

def main():
    show_start_page()
    path = input("enter path for a the words.txt")
    index = int(input("enter the word index"))
    secret_word = choose_word(path, index)
    init_game(secret_word)


if __name__ == '__main__':
    main()