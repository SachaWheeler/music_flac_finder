import webbrowser
import re


# Define the path to your text file containing URLs
COUNT = 4
file_path = 'music_m4p_list.txt'

# Open and read the file
with open(file_path, 'r') as file:
    urls = file.readlines()

# Iterate through each URL and open it in a web browser
count = 0
for url in urls:
    # Strip any leading/trailing whitespaces or newline characters
    if url[0] == "#":
        continue
    count +=  1
    url = url.strip()
    url = re.sub(r'^\d+ ', '', url)
    url = re.sub('\(.*\)', '', url)
    s = re.sub('[^0-9a-zA-Z]+', ' ', url)

    print(url)
    # Open the URL in the default web browser
    webbrowser.open(f"https://magnetdl.torrentbay.net/search/?q={s}&m")

    if count >= COUNT:
        x = input('Continue?')
        count = 0
        if x in ['x', 'n']:
            print("stop")
            break
    print("next")
    # break
