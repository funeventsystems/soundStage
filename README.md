
# SoundStage

Soundstage is a basic audio player which outputs on all available interfaces based on triggers from the webUI, this can be modified to suit any needs, and we will be working more on this as use cases present themselves.

## Setup
- Clone the repository.
- Install FFMPEG `sudo apt-get update` and `sudo apt-get install ffmpeg -y`
- Install Flask and Python3 `sudo apt-get install python3` and `sudo apt-get install python3-flask`
-
## Setting up with multimedia
Currently the system only supports jpg and png files, which will be converted into the .fb format.

1. Use the `Upload files` function to upload your images, please give them names based on which cue you would like them to be a part of. e.x `1.wav` `2.wav` `3.wav`
2. Done, the files will be loaded automatically. Just ensure that the uploaded names match the cue you would like to assign. 

If a file is already written to a cue. Run the command `sudo rm /home/pi/{cue_number}.wav`

## Running it live in a show
Not much setup is required, beyond pressing the `setup` button, which is available on the webpage at `10.0.0.181:106` or `127.0.0.1:106` or `{ip_address}:106`
