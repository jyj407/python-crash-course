def make_album(artist_name, album_title, num_tracks = ''):
    album = {'name' : artist_name, 'title' : album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album


while (True):
    artist_name = input("\nInput the artist name ('q' to quit): ")
    if (artist_name == 'q'):
        break;
    album_title = input("\nInput the album title ('q' to quit): ")
    if (album_title == 'q'):
        break;
    num_tracks = input("\nInput the number of tracks ('q' to quit): ")
    if (num_tracks == 'q'):
        break;
    album = make_album(artist_name, album_title, num_tracks)
    print(album)

    
    
