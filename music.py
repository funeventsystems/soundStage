
from fileinput import filename 
from flask import * 
import os
import time
import json
import subprocess

app = Flask(__name__)





# Setup, clears the screen and makes it so no system messages show.
@app.route('/setup/', methods=['GET','POST'])
def setup():
    os.system("ffplay -v 0 -nodisp -autoexit WakeMeUp.wav ")
    initialized = "yes"
    image = "splash"
    return("Setup")

@app.route('/stop/', methods=['GET', 'POST'])
def stop():
    os.system("killall ffplay")
    return("stopped")

#Route to run a command on the system.
@app.route('/command/', methods=['POST', 'FETCH'])
def command():
    data = request.get_json()
    receivedCommand = data
    os.system(receivedCommand["sentCommand"])
    return "Command worked, possibly. Look at the screen!"
#File upload
@app.route('/upload', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)   
        return render_template("Acknowledgement.html", name = f.filename)   
# upload page
@app.route('/uploadpage')   
def main():   
    return render_template("upload.html")    
#Main page.
@app.route("/") 
def hello(): 
    message = "Hello, World"
    return render_template('index.html',  
                           message=message) 

#volume page
@app.route("/volumepage") 
def volumePage(): 
    message = "Hello, World"
    return render_template('volume.html',  
                           message=message) 




# Scene routes to start a numberical scene.
@app.route('/startScene/<scene_id>')
def start_scene(scene_id):
    # Validate and sanitize the scene_id to prevent command injection
    if not scene_id.isdigit():
        return 'Invalid scene_id'

    # Use subprocess.run to execute the command safely
    command = f"ffplay -v 0 -nodisp -autoexit /home/pi/music/{scene_id}.wav "
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode == 0:
        return f'Starting scene {scene_id}'
    else:
        return f'Error starting scene {scene_id}: {result.stderr}'


# Scene routes to start a numberical scene.
@app.route('/volume/<volume>')
def volume(volume):

    if not volume.isdigit():
        return 'Invalid volume'


    command = f"amixer sset 'PCM' {volume}%"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode == 0:
        return f'Starting scene {volume}'
    else:
        return f'Error starting scene {volume}: {result.stderr}'




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=106)
    

