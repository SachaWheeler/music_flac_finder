import os
import re
import urllib.parse
import shutil

os.chdir('/home/sacha/happy_share/Music/Music2023/Media.localized')
m4p_directory = 'Apple Music'
mp3_directory = 'Music'
removed_dir = 'removed/'

def album_tuples(album_dirs):
    return [(re.sub('[\(\[].*[\)\]]', '', album).strip(), album) for album in album_dirs]

FILENAME = "/home/sacha/work/music/to_fetch.txt"
with open(FILENAME, 'w+') as the_file:
    # iterate over artists in the m4p directory
    for artist in os.listdir(m4p_directory):

        m4p_path = os.path.join(m4p_directory, artist)
        m4p_albums = album_tuples(os.listdir(m4p_path))
        if len(m4p_albums) == 0:
            os.rmdir(m4p_path)
            continue

        mp3_path = os.path.join(mp3_directory, artist)
        if os.path.isdir(mp3_path):
            mp3_albums = album_tuples(os.listdir(mp3_path))

            for (name1, album1) in m4p_albums:
                album_matched = False
                for (name2, album2) in mp3_albums:
                    if name1 == name2:
                        album_matched = True
                        # print(album1, "matches", album2)
                        m4ps = os.listdir(m4p_path + "/" + album1)
                        if len(m4ps) == 0:
                            os.rmdir(m4p_path + "/" + album1)
                            continue
                        mp3s = os.listdir(mp3_path + "/" + album2)

                        # check if the m4ps exist as mp3s
                        for m4p in m4ps:
                            title = re.sub('^[0-9\-\ ]+', '', m4p).split('.')[0]
                            mp3_matches = [s for s in mp3s if title in s]
                            if len(mp3_matches) == 0:
                                # fetch the album
                                pass
                                continue
                            print(artist, album1)
                            print("m4p:   ", m4p)
                            print("mp3:   ", mp3_matches)
                            if len(mp3_matches) ==  1:
                                mp3_matches = mp3_matches[0]
                            # x = input(f"\nreplace '{m4p}' with '{mp3_matches}'")
                            if True:  #'y' in x.lower():
                                print(f"removing {m4p_path}/{album1}/{m4p}")
                                shutil.move(f"{m4p_path}/{album1}/{m4p}", removed_dir)
                if not album_matched:
                    # write to the file
                    the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist} {name1}/Music/1/") + '\n')

        else:  # mp3 artist dir does njot exist
            # add mp4 album to torrent list
            the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist}/Music/1/") + '\n')
            pass





            """
                continue
                for album in albums:
                    album  = re.sub('\(.*\)', '', album)
                    print(album)
                    if album in mp3_albums:
                        # consider deleting the m4p dir
                        print(f"{album} exists as mp3")
                        # print(album)
                        print(os.listdir(mp3_path + album))
                        print(mp3_albums)
                        m4p_dir = f + '/' + album
                        print(os.listdir(m4p_dir))
                        x = input(f"delete {m4p_dir}? ")
                        if x.lower() == 'y':
                            print(f"deleting {m4p_dir}")
                            shutil.move(m4p_dir, removed_dir)
                            # exit(0)
                    else:
                        # continue
                        # x = input(f"get {artist}/{album}?")
                        x = ''
                        if x == 'y':
                            the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist} {album}/Music/1/") + '\n')
                        # break
            else:
                # the m4p dir is NOT in the mp3 path
                # the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist}/Music/1/") + '\n')
                the_file.write(artist  + '\n')


            """
