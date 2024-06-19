from PIL import Image
import os, glob

def resize_images (wallpaper, path, new_path, size):
    with Image.open(os.path.join(path,wallpaper)) as im:
        im.thumbnail(size)
        im.save(os.path.join(preview_path, wallpaper) + ".thumbnail", "PNG")

home_dir = os.path.expanduser('~')
path = f"{home_dir}/Pictures/Wallpapers"
preview_path = f"{home_dir}/Pictures/.wallpapers"
size = 128, 128

wallpaper = "7.jpg"
resize_images(wallpaper, path, preview_path, size)