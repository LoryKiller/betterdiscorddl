
import requests
import os
import glob
url = "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe"
userprofile = os.getenv("USERPROFILE")
temp = os.getenv('userprofile') + r"\ " +"downloads" + r"\ "
temp = str(temp)
temp = temp.replace(" ","")
temp = temp.replace(os.sep,"/")
path=temp+"BetterDiscord-Windows.exe"




response = requests.get(url)
open(path, "wb").write(response.content)

while True:
    if glob.glob(path):
        break
os.startfile(path)