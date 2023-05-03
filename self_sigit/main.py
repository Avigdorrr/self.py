def last_early(my_str):
    return my_str.lower().count(my_str[-1]) >= 2


def distance(num1, num2, num3):
    condition1 = abs(num2-num1) == 1 or abs(num3-num1) == 1
    condition2 = (abs(num2-num1) >= 2 and abs(num2-num3) >= 2) or (abs(num3-num1) >= 2 and abs(num2-num3) >= 2)
    return condition1 and condition2


def filter_teens(a=13, b=13, c=13):
    if 13 <= a <= 14 or 16 <= a <= 19:
        a = fix_age()
    if 13 <= b <= 14 or 16 <= b <= 19:
        b = fix_age()
    if 13 <= c <= 14 or 16 <= c <= 19:
        c = fix_age()
    return a+b+c


def fix_age():
    return 0


def chocolate_maker(small, big, x):
    if (big * 5 + small) < x or x % 5 > small:
        return False
    return True


def func(num1, num2):
    """Calculates an average between 2 numbers.
       :param num1: number 1 value
       :param num2: number 2 value
       :type num1: float
       :type num2: float
       :return: The result of average of num1 and num2
       :rtype: float
       """
    return (num1 + num2) / 2


def shift_left(my_list):
    a, b, c = my_list
    my_list = b, c, a
    return my_list

def format_list(my_list):
    return ", ".join(my_list[::2]) + " and " + my_list[-1]

def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2

def longest(my_list):
    return max(my_list, key=len)

def squared_numbers(start, stop):
    lst = []
    while start <= stop:
        lst.append(start ** 2)
        start += 1
    return lst

def is_greater(my_list, n):
    lst = []
    for number in my_list:
        if number > n:
            lst.append(number)
    return lst

def numbers_letters_count(my_str):
    number = 0
    not_number = 0
    for char in my_str:
        if char.isnumeric():
            number += 1
        else:
            not_number += 1
    return [number, not_number]


def seven_boom(end_number):
    lst = []
    for n in range(end_number+1):
        if n % 7 == 0 or contains_digit(n,7):
            lst.append("BOOM")
        else:
            lst.append(n)
    return lst

def contains_digit (number, digit):
    while number > 0:
        if number % 10 == digit:
            return True
        number //= 10
    return False

def sequence_del(my_str):
    result = ""
    prev_char = ""
    for char in my_str:
        if char != prev_char:
            result += char
        prev_char = char
    return result

def arrow(my_char, max_length):
    for number in range(1,max_length + 1):
        print(" ".join(my_char * number))
    for number in range(max_length - 1, 0, -1):
        print(" ".join(my_char * number))

def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=key_func, reverse=True)

def key_func(lst):
    return float(lst[1])

def mult_tuple(tuple1, tuple2):
    lst = []
    for one in tuple1:
        for two in tuple2:
            lst.append((one, two))
            lst.append((two, one))
    return tuple(lst)

def sort_anagrams(list_of_strings):
    lst = []
    for i in list_of_strings:
        if is_in_list(i, lst):
            continue
        mini_lst = [i]
        for j in list_of_strings:
            if i != j and sorted(i) == sorted(j):
                mini_lst.append(j)
        lst.append(mini_lst)
    return lst

def is_in_list(element, lst):
    for n in lst:
        if element in n:
            return True
    return False

def count_chars(my_str):
    my_dict = {}
    for char in my_str:
        if char != " " and char not in my_dict.keys():
            my_dict[char] = my_str.count(char)
    return my_dict

def inverse_dict(my_dict):
    inv_dict = {}
    for key, value in my_dict.items():
        if value not in inv_dict:
            inv_dict[value] = [key]
        else:
            inv_dict[value].append(key)
    return inv_dict

def copy_file_content(source, destination):
    with open(r"%s" % source, "r") as file:
        data = file.read()
    with open(r"%s" % destination, "w") as file:
        file.write(data)


def who_is_missing(file_name):
    with open(r"%s" % file_name, "r") as file:
        data = file.read()
    lst = data.split(",")
    for i in range(1,10):
        if str(i) not in lst:
            number = str(i)
    with open(r"unit9/text_files/found.txt", "w") as file:
        file.write(number)

def logest_song(str):
    lst = str.split(";")
    duration_parts = lst[2].split(":")
    return int(duration_parts[0]) * 60 + int(duration_parts[1])


def my_mp3_playlist(file_path):
    with open(r"%s" % file_path, "r") as file:
        data = file.read()
    lines = data.split("\n")

    lines_len = len(lines)
    max_line = max(lines, key=logest_song)
    max_len_song = max_line.split(';')[0]
    artist_dict = {}
    for line in lines:
        artist = line.split(';')[1]
        if artist_dict.get(artist, 0) == 0:
            artist_dict[artist] = 1
        else:
            artist_dict[artist] += 1
    most_appears_artist = max(artist_dict, key=lambda key: artist_dict[key])
    return max_len_song, lines_len, most_appears_artist

def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    while len(lines) < 3:
        lines.append(";;\n")
    info = lines[2].split(";")
    lines[2] = f"{new_song};{info[1]};{info[2]};\n"

    with open(file_path, 'w') as f:
        f.writelines(lines)

    with open(file_path, 'r') as f:
        print(f.read())

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


def main():
    print(choose_word(r"hangman/hangman-unit9/words.txt", 15))

if __name__ == '__main__':
    main()


