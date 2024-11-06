import json


def read_json():
    filename = 'songs.json'
    input_file_ptr = None
    while True:
        try:
            input_file_ptr = open(filename, 'r')
            break
        except FileNotFoundError:
            print('The file does not exist')
            filename = input('Enter the correct file name: ')
            continue
    outer_dictionary = json.load(input_file_ptr)
    song_list = outer_dictionary.get('songlist')
    input_file_ptr.close()
    return song_list


def create_playlist(songs):
    # create empty list, then loop while user wants to enter a song
    # print songs, user chooses song, get song info from dict, add to list
    # playlist is a 2d list with each row a song
    playlist = list()
    while True:
        num = 1
        print('Here are your song options:\n')
        for song in songs:
            title = song.get('title')
            artist = song.get('artist')
            print(num, '. ' + title + ' by ' + artist)
            print()
            num += 1
        print('Choose a song to add to your playlist')
        user_num = int(input('Enter the song number: '))
        song_dict_chosen = songs[user_num - 1]
        inner_list = list()
        inner_list.append(song_dict_chosen.get('title'))
        inner_list.append(song_dict_chosen.get('artist'))
        inner_list.append(song_dict_chosen.get('year'))
        inner_list.append(song_dict_chosen.get('album'))
        playlist.append(inner_list)
        choose_more = input("do you want to choose another song? y/n: ").lower()
        if choose_more == 'n':
            break
    return playlist


def write_to_csv(list_playlist):
    # open csv file for writing
    output_file_ptr = open('playlist.csv', 'w')
    output_file_ptr.write('Title,Artist,Year,Album\n')
    for song_inner_list in list_playlist:
        title = song_inner_list[0]
        artist = song_inner_list[1]
        year = str(song_inner_list[2])
        album = song_inner_list[3]
        output_file_ptr.write(title + ',' + artist + ',' + year + ',' + album + '\n')
    output_file_ptr.close()


def main():
    songs = read_json()
    two_d_playlist = create_playlist(songs)
    write_to_csv(two_d_playlist)


main()
