def make_album(artist, album, tracks=''):
    album = {
        'artist_name': artist.title(),
        'album_name': album.title(),
        }
    if tracks:
        album['number_of_tracks'] = tracks
    return album

beatles = make_album('beatles', 'white album')
pinkfloyd = make_album('pink floyd', 'the wall', 10)

print(beatles)
print(pinkfloyd)
