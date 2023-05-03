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