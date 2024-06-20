from PIL import Image
import os

def convert_to_png(input_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        try:
            with Image.open(os.path.join(input_dir, filename)) as img:
                if img.format != 'PNG':
                    png_filename = os.path.splitext(filename)[0] + '.png'
                    img.save(os.path.join(output_dir, png_filename), 'PNG')
                else:
                    img.save(os.path.join(output_dir, filename), 'PNG')
                    
                print(f"Converted {filename} to PNG.")
        
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

# Example usage:
input_directory = '/home/aexyzk/Wallpapers'
output_directory = '/home/aexyzk/NewWallpapers'

convert_to_png(input_directory, output_directory)
