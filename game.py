import pygame
import sys


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.x = 1240 / 2
        self.y = 768 / 2

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.x -= self.dx
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
        self.y -= self.dy


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        group = wall_group
        super().__init__(group, all_sprites)
        if tile_type == 'walkgrass':
            self.image = image_grass
        elif tile_type == 'wallstone':
            self.image = image_stone
        self.image = load_image(level_name, tile_type[4:], 'png')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.images = []
        self.count = 0
        for i in range(11):
            self.images.append(load_image('character', 'Run\Running_0' + str(i + 1), 'png'))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

    def stopped(self):
        self.image = player_image
        self.count = 0

    def go(self):
        self.image = self.images[self.count]
        self.count = (self.count + 1) % 11



def load_image(pack, name, png, colorkey=None):
    fullname = 'data/' + pack + '/' + name + '.' + png
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


def terminate():
    pygame.quit()
    sys.exit()


def load_level(filename):
    filename = "level/" + filename + '.txt'
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

    fon = pygame.transform.scale(load_image('fon', 'fon', 'jpg'), (width, height))
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
            Tile('walkgrass', x, y)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('wallstone', x, y)
            elif level[y][x] == '@':
                Tile('walklandleft', x, y)
                xx = x
                yy = y
            elif level[y][x] == 'S':
                Tile('wallstones_7', x, y)
            elif level[y][x] == 'p':
                Tile('walldecor_1', x, y)
            elif level[y][x] == 'l':
                Tile('walllake', x, y)
            elif level[y][x] == 'b':
                Tile('walldecor_6', x, y)
            elif level[y][x] == 'd':
                Tile('walldecor_5', x, y)
            elif level[y][x] == 'y':
                Tile('walklandleft', x, y)
                Tile('walldecor_3', x, y)
            elif level[y][x] == 'r':
                Tile('walldecor_8', x, y)
            elif level[y][x] == 'z':
                Tile('walldecor_2', x, y)
            elif level[y][x] == 'k':
                Tile('walldecor_7', x, y)
            elif level[y][x] == 'f':
                Tile('wallbuilding_3', x, y)
            elif level[y][x] == 'w':
                Tile('wallbuilding_2', x, y)
            elif level[y][x] == 'W':
                Tile('wallbuilding_1', x, y)
            elif level[y][x] == 'O':
                Tile('wallbuilding_5', x, y)
            elif level[y][x] == 'P':
                Tile('wallbuilding_4', x, y)
            elif level[y][x] == '1':
                Tile('walktree_1', x, y)
            elif level[y][x] == '2':
                Tile('walktree_2', x, y)
            elif level[y][x] == '3':
                Tile('walktree_3', x, y)
            elif level[y][x] == '4':
                Tile('walktree_4', x, y)
            elif level[y][x] == '5':
                Tile('walktree_5', x, y)
            elif level[y][x] == '6':
                Tile('walktree_6', x, y)
            elif level[y][x] == '7':
                Tile('walktree_7', x, y)
            elif level[y][x] == '8':
                Tile('walktree_8', x, y)
            elif level[y][x] == '9':
                Tile('walktree_9', x, y)
            elif level[y][x] == 'J':
                Tile('wallstones_2', x, y)
            elif level[y][x] == 'K':
                Tile('walkgreenery_1', x, y)
            elif level[y][x] == 'L':
                Tile('walkgreenery_2', x, y)
            elif level[y][x] == 'D':
                Tile('walkgreenery_4', x, y)
            elif level[y][x] == 'E':
                Tile('walkgreenery_5', x, y)
            elif level[y][x] == 'Q':
                Tile('walkgreenery_9', x, y)
            elif level[y][x] == 'g':
                Tile('walkgreenery_10', x, y)
            elif level[y][x] == 't':
                Tile('walklandleft', x, y)
            elif level[y][x] == 'T':
                Tile('walklandup', x, y)
            elif level[y][x] == 'V':
                Tile('walklandupper', x, y)
            elif level[y][x] == 'v':
                Tile('walklandlefter', x, y)
            elif level[y][x] == 'F':
                Tile('wallzdanie', x, y)
    new_player = Player(xx, yy)
    return new_player, xx, yy


player_image = load_image('character', 'DLE', 'png')
player_image = pygame.transform.scale(player_image, (100, 100))
tile_width = tile_height = 100
pygame.init()
size = width, height = 1240, 768
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
FPS = 25
clock = pygame.time.Clock()
start_screen()
startsc = True
player = None
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
camera = Camera()
level = [[]]
marx = None
mary = None
mario = None
level_name = "6"
image_grass = load_image(level_name, 'grass', 'png')
image_stone = load_image(level_name, 'stone', 'png')
g_right = False
g_left = False
g_up = False
g_down = False
reverse = False
went = False
walkfree = ['@', '.', 't', 'T', 'v', 'V', 'g']
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
            marx = player[1]
            marx += 0.6
            mary = player[2] + 0.8
            player = player[0]
            if not startsc:
                camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif not startsc:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    g_up = True
                if event.key == pygame.K_LEFT:
                    g_left = True
                if event.key == pygame.K_DOWN:
                    g_down = True
                if event.key == pygame.K_RIGHT:
                    g_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    g_up = False
                    player.stopped()
                if event.key == pygame.K_LEFT:
                    g_left = False
                    player.stopped()
                if event.key == pygame.K_DOWN:
                    g_down = False
                    player.stopped()
                if event.key == pygame.K_RIGHT:
                    g_right = False
                    player.stopped()
    if g_up:
        mary -= 0.08
        test = int(mary)
        if level[test][int(marx)] in walkfree:
            player.rect.y -= 8
            went = True
            reverse = True
        else:
            mary += 0.08
    if g_down:
        mary += 0.08
        test = int(mary)
        if level[test][int(marx)] in walkfree:
            player.rect.y += 8
            went = True
            reverse = False
        else:
            mary -= 0.08
    if g_right:
        marx += 0.08
        test = int(marx)
        if level[int(mary)][test] in walkfree:
            player.rect.x += 8
            went = True
            reverse = False
        else:
            marx -= 0.08
    if g_left:
        marx -= 0.08
        test = int(marx)
        if level[int(mary)][test] in walkfree:
            player.rect.x -= 8
            went = True
            reverse = True
        else:
            marx += 0.08
    if went:
        player.go()
        went = False
    if reverse:
        player.image = pygame.transform.flip(player.image, 1, 0)
        reverse = False
    if not startsc:
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
