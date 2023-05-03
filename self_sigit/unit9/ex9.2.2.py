def copy_file_content(source, destination):
    with open(r"%s" % source, "r") as file:
        data = file.read()
    with open(r"%s" % destination, "w") as file:
        file.write(data)
