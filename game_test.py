import pygame
import os
import sys


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        if 'wall' in tile_type:
            group = wall_group
        else:
            group = walk_group
        super().__init__(group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


def terminate():
    pygame.quit()
    sys.exit()


def load_level(pack, filename):
    filename = "level/" + pack + '/' + filename + '.txt'
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
    except Exception:
        print('Файл с картой в папке levels не найден.')
        pygame.quit()
        sys.exit()
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Ходить можно только по траве",
                  "Цели пока что нет"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def generate_level(level):
    new_player, xx, yy = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            Tile('empty', x, y)
    for y in range(len(level)):
            if level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                xx = x
                yy = y
                new_player = Player(x, y)
    return new_player, xx, yy


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')}
player_image = load_image('character', 'DLE.png')
player_image = pygame.transform.scale(player_image, (100, 72))
tile_width = tile_height = 100
pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
FPS = 50
clock = pygame.time.Clock()
start_screen()
startsc = True
player = None
all_sprites = pygame.sprite.Group()
walk_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
camera = Camera()
level = [[]]
marx = None
mary = None
mario = None
level_name = "6"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif (event.type == pygame.KEYDOWN or
              event.type == pygame.MOUSEBUTTONDOWN) and startsc:
            screen.fill((255, 255, 255))
            startsc = False
            level = load_level(level_name)
            player = generate_level(level)
            mario = player[0]
            marx = player[1]
            mary = player[2]
            if not startsc:
                camera.update(mario)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif event.type == pygame.KEYDOWN and not startsc:
            if event.key == pygame.K_UP:
                if level[mary - 1][marx] == '.':
                    level2 = [[0] * len(level[0]) for _ in range(len(level))]
                    for y in range(len(level)):
                        for x in range(len(level[y])):
                            if x == marx and y == mary - 1:
                                level2[y][x] = '@'
                            elif x == marx and y == mary:
                                level2[y][x] = '.'
                            elif level[y][x] == '.':
                                level2[y][x] = '.'
                            elif level[y][x] == '#':
                                level2[y][x] = '#'
                    level = level2
                    player = generate_level(level)
                    mario = player[0]
                    marx = player[1]
                    mary = player[2]
            if event.key == pygame.K_LEFT:
                if level[mary][marx - 1] == '.':
                    level2 = [[0] * len(level[0]) for _ in range(len(level))]
                    for y in range(len(level)):
                        for x in range(len(level[y])):
                            if x == marx - 1 and y == mary:
                                level2[y][x] = '@'
                            elif x == marx and y == mary:
                                level2[y][x] = '.'
                            elif level[y][x] == '.':
                                level2[y][x] = '.'
                            elif level[y][x] == '#':
                                level2[y][x] = '#'
                    level = level2
                    player = generate_level(level)
                    mario = player[0]
                    marx = player[1]
                    mary = player[2]

            if event.key == pygame.K_DOWN:
                if level[mary + 1][marx] == '.':
                    level2 = [[0] * len(level[0]) for _ in range(len(level))]
                    for y in range(len(level)):
                        for x in range(len(level[y])):
                            if x == marx and y == mary + 1:
                                level2[y][x] = '@'
                            elif x == marx and y == mary:
                                level2[y][x] = '.'
                            elif level[y][x] == '.':
                                level2[y][x] = '.'
                            elif level[y][x] == '#':
                                level2[y][x] = '#'
                    level = level2
                    player = generate_level(level)
                    mario = player[0]
                    marx = player[1]
                    mary = player[2]
            if event.key == pygame.K_RIGHT:
                if level[mary][marx + 1] == '.':
                    level2 = [[0] * len(level[0]) for _ in range(len(level))]
                    for y in range(len(level)):
                        for x in range(len(level[y])):
                            if x == marx + 1 and y == mary:
                                level2[y][x] = '@'
                            elif x == marx and y == mary:
                                level2[y][x] = '.'
                            elif level[y][x] == '.':
                                level2[y][x] = '.'
                            elif level[y][x] == '#':
                                level2[y][x] = '#'
                    level = level2
                    player = generate_level(level)
                    mario = player[0]
                    marx = player[1]
                    mary = player[2]
    if not startsc:
        camera.update(mario)
        for sprite in all_sprites:
            camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
