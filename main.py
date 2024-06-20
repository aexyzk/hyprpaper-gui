import pygame, os, toml

from scripts.wallpaper import set_wallpaper

def main():
    pygame.init()

    home_dir = os.path.expanduser('~')
    path = f"{home_dir}/Pictures/Wallpapers"
    preview_path = f"{home_dir}/Pictures/.wallpapers"

    make_folder(path, preview_path)
    padding = 10
    size = 128
    colum_count = 8
    
    screen_width = ((colum_count * (size + padding)) + padding)

    screen = pygame.display.set_mode((screen_width,800))
    pygame.display.set_caption("Set Wallpaper")
    clock = pygame.time.Clock()

    images_links = update_images(preview_path, colum_count)
    images = get_preview_images(images_links[0], preview_path, size, padding)

    offset = 0
    mouse_sens = 30

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, image in enumerate(images):
                        rect = pygame.Rect(images_links[0][i][1][0] * size, images_links[0][i][1][1] * size, size,size)
                        if rect.collidepoint((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - offset)):
                            set_wallpaper(os.path.join(path, images_links[0][i][0]))

                if event.button == 4:
                    offset = min(offset + mouse_sens, 0)
                elif event.button == 5:
                    clamp = (images_links[1] * -size) + screen.get_height() - size
                    offset = max(offset - mouse_sens, clamp)

        screen.fill((25,25,25))
        for i, image in enumerate(images):
            rect = pygame.Rect(
                                images_links[0][i][1][0] * (size + padding) + padding,
                                images_links[0][i][1][1] * (size + padding) + padding + offset,
                                size,size)

            pygame.draw.rect(screen, (35,35,35), rect)
        render(screen, images, offset, size)
        pygame.display.flip()
        clock.tick(60)

def render(screen, images, offset, size):
    for image in images:
        image_size = image[0].get_size()
        screen.blit(image[0], (image[1][0], image[1][1] + offset))

def get_preview_images(images_links, _path, size, padding):
    images = []
    for name, pos in images_links:
        try:
            path = os.path.join(_path, name)
            image = pygame.image.load(path).convert()
            image_size = image.get_size()

            #centered_pos = (
            #    pos[0] * size + image_size[0] // 2,
            #    pos[1] * size + image_size[1] // 2
            #)
            centered_pos = (
                pos[0] * (size + padding) + padding + (size - image_size[0]) // 2,
                pos[1] * (size + padding) + padding + (size - image_size[1]) // 2
            )

            #centered_pos = ((pos[0] * image_size[0]) + (image_size[0] // 2), (pos[1] * image_size[1]) + (image_size[1] // 2))
            #rect_pos = ((pos[0] * image_size[0]) + (image_size[0] // 2), (pos[1] * image_size[1]) + (image_size[1] // 2))

            images.append((image, centered_pos))
        except Exception as e:
            print(f"[ERROR] {name}: {e}")

    return images

def update_images(path, offset):
    images = []
    if os.path.exists(path):
        row_number = 0
        for i, j in enumerate(os.listdir(path)):
            if i % offset == offset - 1:
                row_number += 1
            images.append((j,(i % offset, row_number)))
    print(images)
    return (images, row_number)

def make_folder(path, preview_path):
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(preview_path):
        os.makedirs(preview_path)

if __name__ == "__main__":
    main()