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
    intro_text = ['pre-alpha v0.1']
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 24)
    text_coord = 22
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    font = pygame.font.SysFont('Bauhaus 93', 30)
    string_rendered = font.render("CONTINUE", 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 300
    intro_rect.x = 580
    text_x = intro_rect.x
    text_y = intro_rect.top
    text_w = string_rendered.get_width()
    text_h = string_rendered.get_height()
    pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 15), 2)
    screen.blit(string_rendered, intro_rect)
    string_rendered = font.render("NEW GAME", 1, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 350
    intro_rect.x = 576
    text_x = intro_rect.x
    text_y = intro_rect.top
    text_w = string_rendered.get_width()
    text_h = string_rendered.get_height()
    pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 15), 2)
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
                if level_name == '6':
                    Tile('walklandleft', x, y)
                elif level_name == '5':
                    Tile('walklandleft', x, y)
                elif level_name == '4':
                    Tile('walklandup', x, y)
                elif level_name == '2':
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
            elif level[y][x] == 'B':
                Tile('walldown', x, y)
                Tile('walldown', x+1, y)
                Tile('wallbaryg', x+0.5, y+1)
                Tile('walltorg2', x, y)
            elif level[y][x] == '|':
                Tile('walldown', x, y)
            elif level[y][x] == "/":
                Tile('walldown', x, y+0.7)
            elif level[y][x] == "'":
                Tile('wallleft', x, y)
            elif level[y][x] == '"':
                Tile('wallleft', x+0.7, y)
            elif level[y][x] == '{':
                Tile('wallleftup', x, y)
            elif level[y][x] == '}':
                Tile('wallrightup', x, y)
            elif level[y][x] == '[':
                Tile('walldownleft', x, y)
            elif level[y][x] == ']':
                Tile('walldownright', x, y)
            elif level[y][x] == '<':
                Tile('wallvipit', x, y-0.5)
            elif level[y][x] == '>':
                Tile('wallpripravy', x, y-0.5)
            elif level[y][x] == 'M':
                Tile('wallmeshok', x, y)
            elif level[y][x] == '#':
                Tile('walldecor_2!', x, y)
            elif level[y][x] == "F":
                Tile('wallbuilding_9', x, y)
            elif level[y][x] == "u":
                Tile('walldecor_16', x, y)
            elif level[y][x] == "U":
                Tile('walldecor_4', x, y)
    new_player = Player(xx, yy)
    return new_player, xx, yy


player_image = load_image('character', 'DLE', 'png')
loading_image = load_image('fon', 'loading', 'jpg')
player_image = pygame.transform.scale(player_image, (100, 100))
tile_width = tile_height = 100
pygame.init()
size = width, height = 1240, 768
fon = pygame.transform.scale(load_image('fon', 'fon', 'jpg'), (width, height))
screen = pygame.display.set_mode(size)
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
marx2 = None
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
        elif event.type == pygame.MOUSEBUTTONUP and startsc:
            x, y = pygame.mouse.get_pos()
            if 567 <= x <= 700 and 341 <= y <= 375:
                my_file = open('load_saving.txt', 'w')
                level_name = '1'
                intro = True
                my_file.write('1')
            elif 570 <= x <= 700 and 290 <= y <= 325:
                with open('load_saving.txt', 'r') as mapFile:
                    level_map = [line.strip() for line in mapFile]
                    level_name = level_map[0][0]
            screen.fill((255, 255, 255))
            startsc = False
            level = load_level(level_name)
            screen.blit(loading_image, (0, 0))
            pygame.display.flip()
            player = generate_level(level)
            marx = player[1]
            marx += 0.6
            marx2 = marx - 0.2
            mary = player[2] + 0.8
            player = player[0]
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
                if event.key == pygame.K_e:
                    if level[int(mary-1)][int(marx)] == 'Z':
                        level_name = level_name + '_taverna'
                        level = load_level(level_name)
                        all_sprites = pygame.sprite.Group()
                        wall_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        screen.blit(loading_image, (0, 0))
                        pygame.display.flip()
                        player = generate_level(level)
                        marx = player[1]
                        marx += 0.6
                        marx2 = marx - 0.2
                        mary = player[2] + 0.8
                        player = player[0]
                    elif level[int(mary+1)][int(marx)] == 'Z':
                        level_name = level_name[0]
                        level = load_level(level_name)
                        all_sprites = pygame.sprite.Group()
                        wall_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        screen.blit(loading_image, (0, 0))
                        pygame.display.flip()
                        player = generate_level(level)
                        marx = player[1]
                        mary = player[2]
                        player = player[0]
                        if level_name == '6':
                            marx += 0.6 - 42
                            marx2 = marx - 0.2
                            mary = mary + 0.8 - 6
                            player.rect.x -= 4200
                            player.rect.y -= 600
                        elif level_name == '2':
                            marx += 0.6 - 30
                            marx2 = marx - 0.2
                            mary = mary + 0.8
                            player.rect.x -= 3000
                    elif level[int(mary - 1)][int(marx)] == 'y' or level[int(mary + 1)][int(marx)] == 'y' or\
                            level[int(mary)][int(marx+1)] == 'y' or level[int(mary)][int(marx - 1)] == 'y':
                        if level_name == '6':
                            level_name = '5'
                            level = load_level(level_name)
                            all_sprites = pygame.sprite.Group()
                            wall_group = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            screen.blit(loading_image, (0, 0))
                            pygame.display.flip()
                            player = generate_level(level)
                            marx = player[1]
                            marx += 0.6
                            marx2 = marx - 0.2
                            mary = player[2] + 0.8
                            player = player[0]
                        elif level_name == '5':
                            if level[int(mary)][int(marx - 1)] == 'y':
                                level_name = '6'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary)][int(marx + 1)] == 'y':
                                level_name = '7'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary - 1)][int(marx)] == 'y':
                                level_name = '4'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                        elif level_name == '4':
                            if level[int(mary+1)][int(marx)] == 'y':
                                level_name = '5'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6
                                mary = player[2] + 0.8 - 7
                                player = player[0]
                                marx += 25
                                player.rect.x += 2500
                                player.rect.y -= 700
                                marx2 = marx - 0.2
                            elif level[int(mary)][int(marx-1)] == 'y':
                                level_name = '2'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                        elif level_name == '2':
                            if level[int(mary)][int(marx+1)] == 'y':
                                level_name = '4'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level)
                                marx = player[1]
                                marx += 0.6 - 16
                                mary = player[2] + 0.8 - 6
                                player = player[0]
                                player.rect.x -= 1600
                                player.rect.y -= 600
                                marx2 = marx - 0.2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    g_up = False
                    player.stopped()
                    reverse = True
                if event.key == pygame.K_LEFT:
                    g_left = False
                    player.stopped()
                    reverse = True
                if event.key == pygame.K_DOWN:
                    g_down = False
                    player.stopped()
                if event.key == pygame.K_RIGHT:
                    g_right = False
                    player.stopped()
    if g_up:
        mary -= 0.06
        test = int(mary)
        if level[test][int(marx)] in walkfree and level[test][int(marx2)] in walkfree:
            player.rect.y -= 6
            went = True
            reverse = True
        else:
            mary += 0.06
    if g_down:
        mary += 0.06
        test = int(mary)
        if level[test][int(marx)] in walkfree and level[test][int(marx2)] in walkfree:
            player.rect.y += 6
            went = True
            reverse = False
        else:
            mary -= 0.06
    if g_right:
        marx += 0.06
        marx2 += 0.06
        test2 = int(marx2)
        test = int(marx)
        if level[int(mary)][test] in walkfree and level[int(mary)][test2] in walkfree:
            player.rect.x += 6
            went = True
            reverse = False
        else:
            marx -= 0.06
            marx2 -= 0.06
    if g_left:
        marx -= 0.06
        marx2 -= 0.06
        test2 = int(marx2)
        test = int(marx)
        if level[int(mary)][test] in walkfree and level[int(mary)][test2] in walkfree:
            player.rect.x -= 6
            went = True
            reverse = True
        else:
            marx += 0.06
            marx2 += 0.06
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
        screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
