# hyprpaper-gui
A Wallpaper changer for Hyprpaper, written in Python with Pygame. I find it very frustrating to change wallpapers with hyprpaper, because you have to go to the configuration file, change the link to the file, then save it and restart the daemon. Soooo i wrote this! x3

 ![example](https://github.com/aexyzk/hyprpaper-gui/blob/main/examples/example.png?raw=true)

## using
 - Download the latest release
 - Unzip it
 - Run the following command to make the execuatable runable
 ```
    chmod +x change-wallpaper
 ```
 - Then you can run it
 ```
    ./change-wallpaper
 ```
 - This will create a folder called $HOME/Pictures/Wallpapers if it doesnt exist already, this is were it will look for wallpapers in (you can change this if you build from source, but i am way to lazy to add in a way to change it with a config rn)
 - It also assumes you hyprpaper config is $HOME/.config/hypr/hyprpaper.conf

 (i added a folder to my .bashrc called apps and put it in there so i can just run the command easily)

## building from source
 - Install pygame (i used pygame-ce, but both should work), and pyinstaller
 - Clone the Repo
 - Run
 ```
    pyinstaller main.py --onefile
 ```
 - Your executable should be in the /dist folder