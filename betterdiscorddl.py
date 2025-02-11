
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


#from git import Repo
##import requests
#import os
##import glob
#import shutil
#import time
##url = "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe"
#userprofile = os.getenv("USERPROFILE")
#temp = os.getenv('temp') + r"\ " +"BetterDiscord"
#temp = str(temp)
#temp = temp.replace(" ","")
#temp = temp.replace(os.sep,"/")
#i = 1
#err=True
#backtemp = temp
#while err:
#    try:
#        Repo.clone_from("https://github.com/BetterDiscord/BetterDiscord.git", temp)
#        err=False
#    except Exception as e:
#        
#        temp = backtemp + str(i)
#        i += 1
#        err = True
#
#
#os.system(userprofile+"/Binary-Converter/betterdiscorddl/"+"script.bat "+ temp)
#time.sleep(1)
#try:
#    shutil.rmtree(temp)
#except Exception as e:
#    pass
#
#
##response = requests.get(url)
##open(path, "wb").write(response.content)
##
##while True:
##    if glob.glob(path):
##        break
##
#