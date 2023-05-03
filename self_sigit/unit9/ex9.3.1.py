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