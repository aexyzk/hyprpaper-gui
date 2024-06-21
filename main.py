import pygame, os, time
import threading

from scripts.wallpaper import set_wallpaper
from scripts.utils import *
from scripts.preview import create_preview

def main():
    pygame.init()

    home_dir = os.path.expanduser('~')
    path = f"{home_dir}/Pictures/Wallpapers"
    preview_path = f"{home_dir}/Pictures/.wallpapers"

    make_folder(path, preview_path)
    padding = 10
    size = 128
    size = 250
    column_count = 5
    
    screen_width = ((column_count * (size + padding)) + padding) + 10

    screen = pygame.display.set_mode((screen_width,800))
    pygame.display.set_caption("Set Wallpaper")
    clock = pygame.time.Clock()

    preview_images_links, images_links, images = reload_images(path, preview_path, column_count, size, padding)

    offset = 0
    mouse_sens = 30

    # ui elements
    bar_rect = pygame.Rect(0, screen.get_height() - 48, screen.get_width() - 10, 48)
    scroll_bar_rect =  pygame.Rect(screen.get_width() - 10, 0, 10, screen.get_height())
    refresh_button_rect = pygame.Rect(screen.get_width() - 48 - 10, screen.get_height() - 48, 48, 48)

    # assets
    assets = {
        "refresh_button": load_image("refresh.png")
    }

    running = True
    while running:
        clamp = (preview_images_links[1] * -(size + padding)) + screen.get_height() - size - padding
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bar_rect.collidepoint((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                        if refresh_button_rect.collidepoint((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])):
                            create_previews(path, preview_path, size)
                        break
                    for i, image in enumerate(images):
                        rect = pygame.Rect(
                                preview_images_links[0][i][1][0] * (size + padding) + padding,
                                preview_images_links[0][i][1][1] * (size + padding) + padding + offset,
                                size,size)
                        if rect.collidepoint((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - offset)):
                            set_wallpaper(os.path.join(path, images_links[0][i][0]))

                if event.button == 4:
                    offset = min(offset + mouse_sens, 0)
                    #offset += mouse_sens
                elif event.button == 5:
                    offset = max(offset - mouse_sens - 48, clamp)
                    #offset -= mouse_sens

        screen.fill((25,25,25))
        for i, image in enumerate(images):
            rect = pygame.Rect(
                                preview_images_links[0][i][1][0] * (size + padding) + padding,
                                preview_images_links[0][i][1][1] * (size + padding) + padding + offset,
                                size,size)

            pygame.draw.rect(screen, (35,35,35), rect)
        render(screen, images, offset, size)
        bar(screen, assets, bar_rect, scroll_bar_rect, refresh_button_rect, offset, clamp)
        pygame.display.flip()
        clock.tick(60)

def render(screen, images, offset, size):
    for image in images:
        image_size = image[0].get_size()
        screen.blit(image[0], (image[1][0], image[1][1] + offset))

def bar(screen, assets, bar_rect, scroll_bar_rect, refresh_button_rect, offset, clamp):
    # bar
    pygame.draw.rect(screen, (40,40,40), bar_rect)
    screen.blit(assets["refresh_button"], refresh_button_rect.topleft)

    # scroll bar
    pygame.draw.rect(screen, (45,45,45), scroll_bar_rect)
    # scroll handle
    handle_size = ((clamp * screen.get_height()) * -1)
    handle_pos = (-clamp * -offset - handle_size) // screen.get_height()
    pygame.draw.rect(screen, (80,80,80), pygame.Rect(screen.get_width() - 10, handle_pos, 10, handle_size))
    print(f"{screen.get_height()} {-offset}")
    print(handle_pos)

def get_preview_images(preview_images_links, _path, size, padding):
    images = []
    for name, pos in preview_images_links:
        try:
            path = os.path.join(_path, name)
            image = pygame.image.load(path).convert()
            image_size = image.get_size()

            centered_pos = (
                pos[0] * (size + padding) + padding + (size - image_size[0]) // 2,
                pos[1] * (size + padding) + padding + (size - image_size[1]) // 2
            )

            images.append((image, centered_pos))
        except Exception as e:
            print(f"[ERROR] {name}: {e}")

    return images

def update_images(path, offset):
    images = []
    if os.path.exists(path):
        row_number = 0
        for i, j in enumerate(sorted(os.listdir(path))):
            if i % offset == offset - 1:
                row_number += 1
            images.append((j,(i % offset, row_number)))
    print(images)
    return (images, row_number)

def make_folder(path, preview_path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_previews(path, preview_path, size):
    if not os.path.exists(preview_path):
        os.makedirs(preview_path)
    if os.path.exists(path):
        row_number = 0
        for i, j in enumerate(sorted(os.listdir(path))):
            print(j)
            create_preview(j, path, preview_path, (size, size))


def reload_images(path, preview_path, column_count, size, padding):
    preview_images_links = update_images(preview_path, column_count)
    images_links = update_images(path, column_count)
    images = get_preview_images(preview_images_links[0], preview_path, size, padding)
    return preview_images_links, images_links, images

if __name__ == "__main__":
    main()