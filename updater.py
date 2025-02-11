url="https://raw.githubusercontent.com/LoryKiller/betterdiscorddl/refs/heads/main/betterdiscorddl.py"

import urllib.request
import requests
import glob

data = urllib.request.urlopen(url) 

response = requests.get(url, stream=True)
total_size = int(response.headers.get("content-length", 0))
block_size = 1024

onlinefile = ""
for line in data:
    onlinefile += str(line)
  #  print(line)

onlinefile = onlinefile.split(r"\n", 1)[0]
onlinefile = onlinefile[2:]

with open("betterdiscorddl.py", "r") as f:
    print(onlinefile)
    print(f.readline())
    if onlinefile == f.readline():
        print("The file is already up-to-date.")
    else:
        updatechar = input("A new update is available. Do you want to update it? [y/n]: ") 
        if updatechar.lower() == "y":
            wresponse = requests.get(url)
            open("betterdiscorddl.py", "wb").write(response.content)
                 
                 
                
                
            
                    
            while True:
                if glob.glob("betterdiscorddl.py"):
                    break





