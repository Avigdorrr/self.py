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
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])