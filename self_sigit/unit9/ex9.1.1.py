def are_files_equal(file1, file2):
    with open(file1, "r") as file:
        text1 = file.read()
    with open(file2, "r") as file:
        text2 = file.read()
    return text1 == text2
