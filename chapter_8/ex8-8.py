def make_album():
    while True:
        print("Let's build a music collection by entering albums.\nType 'q' as an entry to quit the program.")
        artist = input('Type the name name of a musical artist: ')
        if artist == 'q':
            break;
        album = input('Type a hit album they have: ')
        print('Type "q" to quit the program.')
        if album == 'q':
            break;
        album = {
            'artist_name': artist.title(),
            'album_name': album.title(),
            }
        print(album)

make_album()
