import webbrowser
import re


# Define the path to your text file containing URLs
file_path = 'music_m4p.txt'

# Open and read the file
with open(file_path, 'r') as file:
    urls = file.readlines()

# Iterate through each URL and open it in a web browser
for url in urls:
    # Strip any leading/trailing whitespaces or newline characters
    if url[0] == "#":
        continue
    url = url.strip()
    s = re.sub('[^0-9a-zA-Z]+', ' ', url)

    # Open the URL in the default web browser
    webbrowser.open(f"https://magnetdl.torrentbay.net/search/?q={s}&m")

    print(url)
    x = input('Continue?')
    if x in ['x', 'n']:
        print("stop")
        break
    print("next")
    # break
