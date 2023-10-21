import os
import re
import urllib.parse
import shutil

os.chdir('/home/sacha/happy_share/Music/Music2023/Media.localized')
directory = 'Apple Music'
removed_dir = 'removed/'

with open('/home/sacha/work/music/output_links.txt', 'a') as the_file:
    # iterate over files in the directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isdir(f):
            artist = f.split('/')[1]
            print(artist)
            albums = os.listdir(f)
            mp3_path = f"Music/{artist}/"
            if os.path.isdir(mp3_path):
                # print(mp3_path)
                mp3_albums = os.listdir(mp3_path)
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
                        x = 'y'
                        if x == 'y':
                            the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist} {album}/Music/1/") + '\n')
                        # break
            else:
                # the m4p dir is NOT in the mp3 path
                pass
                # the_file.write('https:' + urllib.parse.quote(f"//1337x.torrentbay.net/category-search/{artist}/Music/1/") + '\n')


