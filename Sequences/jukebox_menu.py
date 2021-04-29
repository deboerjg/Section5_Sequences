from nested_data import albums
# When you import another file, python automatically excecutes entire other script

SONGS_LIST_INDEX = 3 # Name all in capitals represents a CONSTANT - not to be changed
TRACK_NUMBER_INDEX = 0
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your album (Invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]

    else:
        break

    print("Please choose your song (Invalid choice exits): ")
    for index, (track_number, songs) in enumerate(songs_list):
        print("{}: {}".format(index + 1, songs))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("="*40)

