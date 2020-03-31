#python 3.6 ++ -formatted string literals
def demo():
    track = 'Perfect'
    artist = 'Ed sheeran'
    album = 'divide'
    download = 1234567852
    print(f'track name = {track}, artist = {artist}, download = {download:,}') #string interpolation
    print('track name = {}, artist = {}, download = {:,}'.format(track, artist, download))
    
demo()