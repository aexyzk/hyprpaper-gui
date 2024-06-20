from PIL import Image
import os, glob

def create_preview (wallpaper, path, preview_path, size):
    try:
        with Image.open(os.path.join(path,wallpaper)) as im:
            im.thumbnail(size)
            im.save(os.path.join(preview_path, wallpaper) + ".thumbnail", "PNG")
    except Exception as e:
        print(f"[ERROR] There was an error loading '{wallpaper}'")

if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    path = f"{home_dir}/Pictures/Wallpapers"
    preview_path = f"{home_dir}/Pictures/.wallpapers"
    size = 128, 128

    wallpaper = "idk.png"
    resize_images(wallpaper, path, preview_path, size)