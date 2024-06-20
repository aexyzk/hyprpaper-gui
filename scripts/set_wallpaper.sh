#!/bin/bash

wallpaper='/home/aexyzk/Pictures/Wallpapers/arch.png'

echo "preload = $1" > ~/.config/hypr/hyprpaper.conf
for monitor in $(hyprctl monitors | grep 'Monitor' | awk '{ print $2 }'); do
    echo -e "wallpaper = $monitor,$1" >> ~/.config/hypr/hyprpaper.conf
done
echo -e "ipc = off\nsplash = off" >> ~/.config/hypr/hyprpaper.conf
