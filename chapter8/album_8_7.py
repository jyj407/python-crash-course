def make_album(artist_name, album_title, num_tracks = ''):
    album = {'name' : artist_name, 'title' : album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

jay_album = make_album('Jay Chou', 'QiLixiang', '10')
print(jay_album)
my_album = make_album('Tony Jiang', 'Oh Canada & China')
print(my_album)
james_album = make_album('James Jiang', 'Oh Canada & USA & China')
print(james_album)
