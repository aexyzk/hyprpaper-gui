import os
import subprocess

hyprpaper_conf = os.path.expanduser('~')  + "/.config/hypr/hyprpaper.conf"
if os.path.isfile(hyprpaper_conf):
    print(hyprpaper_conf)
else:
    print("[ERROR] config doesn't exist")

def set_wallpaper(path):
    os.system('pkill hyprpaper')
    if os.path.isfile(path):
        with open(hyprpaper_conf, 'w') as conf:
            conf.write(f"preload = {path}\nwallpaper =  eDP-1,{path}\nipc = off\nsplash = off")
        
        os.system('pkill hyprpaper')

        process = subprocess.Popen(['hyprpaper'])
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            return
    else:
        print("[ERROR] not a valid image")