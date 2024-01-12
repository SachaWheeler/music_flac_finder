#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <string>"
    exit 1
fi

# Store the argument
command="$1"
year=$(date +%Y)
app="Music"
voice="Fiona"
notification_title="Music command"

# display notification \"liked\" with title \"${notification_title}\"
if [ "$command" == "fetch" ]; then
        instruction="
          if player state is playing then -- like if a song is playing
            if loved of current track is false then
              set loved of current track to true
              say \"liked\" using \"${voice}\"
            else
              say \"already liked\" using \"${voice}\"
            end if
             set trackName to name of current track
             set artistName to artist of current track
             set albumName to album of current track

             set musicFolderPath to POSIX path of \"/Volumes/moshpit/Music/\"
             set filePath to musicFolderPath & \"${app}/\" & artistName & \"/\" & albumName & \"/\"

             set albumDirExists to (do shell script \"[ -e \" & quoted form of filePath & \" ] && echo 'true' || echo 'false'\")

             if albumDirExists is not \"true\" then
               display dialog \"File does not exist on disk. Shall I fetch \" & artistName & \", \" & albumName
               display dialog filePath
             end if
          else -- otherwise start a playlist
            play playlist named \"${default_playlist}\"
          end if"

elif [ "$command" == "info" ]; then
          # get {name, artist, album}  of current track
        instruction="
          get {name, artist, album}  of current track
          "
fi

ssh happy@happy.local "osascript -e '
    tell application \"${app}\"
      ${instruction}
    end tell '"
