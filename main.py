import pygame, os

from scripts.wallpaper import set_wallpaper

def main():
    pygame.init()

    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("Set Wallpaper")
    clock = pygame.time.Clock()

    home_dir = os.path.expanduser('~')
    path = f"{home_dir}/Pictures/Wallpapers"

    make_folder(path)
    images_links = update_images(path, 5)
    images = import_images(images_links[0], path)

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
                        rect = pygame.Rect(images_links[0][i][1][0] * 200, images_links[0][i][1][1] * 200, 200,200)
                        if rect.collidepoint((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - offset)):
                            set_wallpaper(os.path.join(path, images_links[0][i][0]))

                if event.button == 4:
                    offset = min(offset + mouse_sens, 0)
                elif event.button == 5:
                    clamp = (images_links[1] * -200) + screen.get_height() - 200
                    offset = max(offset - mouse_sens, clamp)

        screen.fill((25,25,25))
        render(screen, images, offset)
        pygame.display.flip()
        clock.tick(60)

def render(screen, images, offset):
    for image in images:
        screen.blit(image[0], (image[1][0], image[1][1] + offset))

def import_images(images_links, _path, max_image_size=(200, 200)):
    images = []
    for name, pos in images_links:
        try:
            path = os.path.join(_path, name)
            image = pygame.image.load(path).convert()
            image_size = image.get_size()

            size_ratio = (max_image_size[0] / image_size[0], max_image_size[1] / image_size[1])
            scale_ratio = min(size_ratio[0], size_ratio[1])

            scaled_image = pygame.transform.scale(image, (image_size[0] * scale_ratio, image_size[1] * scale_ratio))

            centered_pos = ((pos[0] * max_image_size[0] - scaled_image.get_width() // 2) + 100, (pos[1] * max_image_size[1] - scaled_image.get_height() // 2) + 100)

            images.append((scaled_image, centered_pos))
        except: 
            print(name)

    return images

def update_images(path, offset):
    images = []
    if os.path.exists(path):
        row_number = 0
        for i, j in enumerate(os.listdir(path)):
            if i % offset == offset - 1:
                row_number += 1
            images.append((j,(i % offset, row_number)))
    return (images, row_number)

def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == "__main__":
    main()