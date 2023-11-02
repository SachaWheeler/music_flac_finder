from tpb import TPB
from tpb import CATEGORIES, ORDERS

# t = TPB('https://mirrorbay.org/')
t = TPB('https://thepiratebay.torrentbay.net/')

ARTISTS_FILE = "output_artists.txt"
with open(ARTISTS_FILE) as file:
    artists = list(map(str.strip, file.readlines()))
    count = 0
    for artist in artists:
        print(artist)
        count += 1

        try:
            for torrent in t.search(
                    artist,
                    category=CATEGORIES.AUDIO.MUSIC
                    ).order(ORDERS.SEEDERS.DES):
                print(torrent.info)
        except Exception as e:
            print(e)

