def make_album(band_name, title, songs = ""):
    if songs:
        album = {'band': band_name, 'title': title, 'number_songs': songs}
    else:
        album = {'band': band_name, 'title': title}

    return album


while True:
    print('type q to exit')
    print('Provide band name, album name and optionally number of songs: ')

    band = input('Band: ')
    if band == 'q':
        break

    album = input('Album name: ')
    if album == 'q':
        break

    number = input('Number of songs: ')
    if number =='q':
        break

whole_album = make_album(band, album, number)
print(whole_album)