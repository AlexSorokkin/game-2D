import pygame
import sys


def load_image(pack, name, png, colorkey=None):  # Загрузка уровня
    fullname = 'data/' + pack + '/' + name + '.' + png
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


def terminate():  # Выход из игры
    pygame.quit()
    sys.exit()


def load_level(filename):  # Выгрузка карты
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


def start_screen(screen, fon):  # Main menu
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


def generate_level(level, Tile, level_name, Player, all_sprites, wall_group, load_image, player_group):
    new_player, xx, yy = None, None, None  # Генерация уровня
    for y in range(len(level)):
        for x in range(len(level[y])):
            Tile('walkgrass', x, y, all_sprites, wall_group, load_image, level_name)
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 's':
                Tile('wallstone', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '@':
                if level_name == '6':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '5':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '4':
                    Tile('walklandup', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '2':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '3':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '1':
                    Tile('walklandup', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '7':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '10':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '9':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                elif level_name == '8':
                    Tile('walklandup', x, y, all_sprites, wall_group, load_image, level_name)
                xx = x
                yy = y
            elif level[y][x] == 'S':
                Tile('wallstones_7', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'p':
                Tile('walldecor_1', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'l':
                Tile('walllake', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'b':
                Tile('walldecor_6', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'd':
                Tile('walldecor_5', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'y':
                if level[y][x-1] == 't' or level[y][x-1] == '@':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                else:
                    Tile('walklandup', x, y, all_sprites, wall_group, load_image, level_name)
                Tile('walldecor_3', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'r':
                Tile('walldecor_8', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'z':
                Tile('walldecor_2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'k':
                Tile('walldecor_7', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'f':
                Tile('wallbuilding_3', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'w':
                Tile('wallbuilding_2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'W':
                Tile('wallbuilding_1', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'O':
                Tile('wallbuilding_5', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'P':
                Tile('wallbuilding_4', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '1':
                Tile('walktree_1', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '2':
                Tile('walktree_2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '3':
                Tile('walktree_3', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '4':
                Tile('walktree_4', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '5':
                Tile('walktree_5', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '6':
                Tile('walktree_6', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '7':
                Tile('walktree_7', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '8':
                Tile('walktree_8', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '9':
                Tile('walktree_9', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'J':
                Tile('wallstones_2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'K':
                if level_name == '3':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                Tile('walkgreenery_1', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'L':
                Tile('walkgreenery_2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'D':
                Tile('walkgreenery_4', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'E':
                Tile('walkgreenery_5', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'Q':
                Tile('walkgreenery_9', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'g':
                Tile('walkgreenery_10', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 't':
                Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'T':
                Tile('walklandup', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'V':
                Tile('walklandupper', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'v':
                Tile('walklandlefter', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'F':
                Tile('wallzdanie', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'B':
                Tile('walldown', x, y, all_sprites, wall_group, load_image, level_name)
                Tile('walldown', x+1, y, all_sprites, wall_group, load_image, level_name)
                Tile('wallbaryg', x+0.5, y+1, all_sprites, wall_group, load_image, level_name)
                Tile('walltorg2', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '|':
                Tile('walldown', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "/":
                Tile('walldown', x, y+0.7, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "'":
                Tile('wallleft', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '"':
                Tile('wallleft', x+0.7, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '{':
                Tile('wallleftup', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '}':
                Tile('wallrightup', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '[':
                Tile('walldownleft', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == ']':
                Tile('walldownright', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '<':
                Tile('wallvipit', x, y-0.5, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '>':
                Tile('wallpripravy', x, y-0.5, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == 'M':
                Tile('wallmeshok', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == '#':
                Tile('walldecor_2!', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "F":
                Tile('wallbuilding_9', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "u":
                Tile('walldecor_16', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "U":
                Tile('walldecor_4', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "$":
                Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
            elif level[y][x] == "Y":
                if level_name == '10':
                    Tile('walklandleft', x, y, all_sprites, wall_group, load_image, level_name)
                Tile('walldecor_33', x, y, all_sprites, wall_group, load_image, level_name)
    new_player = Player(xx, yy, all_sprites, player_group, load_image)
    return new_player, xx, yy
