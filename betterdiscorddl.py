version=0.3
#Do not touch
def installbd():
    import requests
    import os
    import glob
    import tqdm






    url = "https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Windows.exe"
    userprofile = os.getenv("USERPROFILE")
    temp = os.getenv('temp') + "\\"
    temp = str(temp)
    temp = temp.replace(" ","")
    temp = temp.replace(os.sep,"/")
    path=temp+"BetterDiscord-Windows.exe"


    response = requests.get(url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024

    with tqdm.tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
        with open(path, "wb") as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

    if total_size != 0 and progress_bar.n != total_size:
        raise RuntimeError("Could not download file")

    while True:
        if glob.glob(path):
            break
    os.startfile(path)

