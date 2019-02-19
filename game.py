import pygame
from functions import load_image, load_level, terminate, generate_level, start_screen
from classes import Character, Camera, Tile, Player
import json
from pathlib import Path


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
start_screen(screen, fon)
startsc = True
player = None
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
camera = Camera(width, height)
level = [[]]
marx = None
marx2 = None
mary = None
mario = None
level_name = "1"
image_grass = load_image(level_name, 'grass', 'png')
image_stone = load_image(level_name, 'stone', 'png')
g_right = False
g_left = False
g_up = False
g_down = False
reverse = False
went = False
brothrun = []
brothdie = []
secslash = []
magwalk = []
brothcount = 0
percount = 0
seccount = 0
thircount = 0
walk = True
per = None
sec = None
summa = 0
thir = None
mag = None
broth = None
dim = None
string1 = ''
string2 = ''
string3 = ''
seconds = 0
walk2 = False
font1 = load_image('fon', 'font', 'png')
font = pygame.font.SysFont('Bauhaus 93', 40)
font_1 = (336, 564)
font_2 = (336, 594)
font_3 = (336, 624)
checkpoint = ''
cutscene = False
cutloading = True
walkfree = ['@', '.', 't', 'T', 'v', 'V', 'g']
while True:  # Игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        elif event.type == pygame.MOUSEBUTTONUP and startsc:  # Заставка
            x, y = pygame.mouse.get_pos()
            if 567 <= x <= 700 and 341 <= y <= 375:
                path = Path('load_saving.json')
                data = json.loads(path.read_text(encoding='utf-8'))
                data['first']['checkpoint'] = 2
                path.write_text(json.dumps(data), encoding='utf-8')
                level_name = '1'
                startsc = False
                cutscene = True
                checkpoint = '1'
            elif 570 <= x <= 700 and 290 <= y <= 325:
                path = Path('load_saving.json')
                data = json.loads(path.read_text(encoding='utf-8'))
                checkpoint = data['first']['checkpoint']
                path.write_text(json.dumps(data), encoding='utf-8')
                if checkpoint == '2':
                    level_name = '2'
                startsc = False
            screen.fill((255, 255, 255))
            level = load_level(level_name)
            screen.blit(loading_image, (0, 0))
            pygame.display.flip()
            player = generate_level(level, Tile, level_name, Player, all_sprites, wall_group,
                                    load_image, player_group)
            marx = player[1]
            marx += 0.6
            marx2 = marx - 0.2
            mary = player[2] + 0.8
            player = player[0]
        elif not startsc and not cutscene:  # Управление персонажем и взаимодействия
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    g_up = True
                if event.key == pygame.K_LEFT:
                    g_left = True
                if event.key == pygame.K_DOWN:
                    g_down = True
                if event.key == pygame.K_RIGHT:
                    g_right = True
                if event.key == pygame.K_e:  # Прогрузка уровней
                    if level[int(mary-1)][int(marx)] == 'Z':
                        level_name = level_name + '_taverna'
                        level = load_level(level_name)
                        all_sprites = pygame.sprite.Group()
                        wall_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        screen.blit(loading_image, (0, 0))
                        pygame.display.flip()
                        player = generate_level(level, Tile, level_name, Player, all_sprites, wall_group,
                                                load_image, player_group)
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
                        player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                load_image, player_group)
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
                        elif level_name == '9':
                            marx += 0.6 - 26
                            marx2 = marx - 0.2
                            mary = mary + 0.8
                            player.rect.x -= 2600
                    elif level[int(mary - 1)][int(marx)].lower() == 'y' or\
                            level[int(mary + 1)][int(marx)].lower() == 'y' or\
                            level[int(mary)][int(marx+1)].lower() == 'y' or\
                            level[int(mary)][int(marx - 1)].lower() == 'y':
                        if level_name == '6':
                            level_name = '5'
                            level = load_level(level_name)
                            all_sprites = pygame.sprite.Group()
                            wall_group = pygame.sprite.Group()
                            player_group = pygame.sprite.Group()
                            screen.blit(loading_image, (0, 0))
                            pygame.display.flip()
                            player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                    load_image, player_group)
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
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
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
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
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
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
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
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                mary = player[2] + 0.8 - 7
                                player = player[0]
                                marx += 25
                                player.rect.x += 2500
                                player.rect.y -= 700
                                marx2 = marx - 0.2
                            elif level[int(mary-1)][int(marx)] == 'y':
                                level_name = '8'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary)][int(marx-1)] == 'y':
                                level_name = '2'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
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
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 - 16
                                mary = player[2] + 0.8 - 6
                                player = player[0]
                                player.rect.x -= 1600
                                player.rect.y -= 600
                                marx2 = marx - 0.2
                            elif level[int(mary)][int(marx-1)] == 'y':
                                level_name = '3'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary+1)][int(marx)] == 'y':
                                level_name = '1'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                        elif level_name == '3':
                            if level[int(mary)][int(marx+1)] == 'y':
                                level_name = '2'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 - 55
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                                player.rect.x -= 5500
                        elif level_name == '1':
                            if level[int(mary-1)][int(marx)] == 'y':
                                level_name = '2'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 - 28
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8 + 5
                                player = player[0]
                                player.rect.x -= 2800
                                player.rect.y += 500
                        elif level_name == '7':
                            if level[int(mary)][int(marx-1)] == 'y':
                                level_name = '2'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 - 50
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                                player.rect.x -= 5000
                        elif level_name == '10':
                            if level[int(mary)][int(marx + 1)].lower() == 'y':
                                level_name = '11'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            if level[int(mary)][int(marx - 1)] == 'y':
                                level_name = '8'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 + 14
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8 - 5
                                player = player[0]
                                player.rect.y -= 500
                                player.rect.x += 1400
                        elif level_name == '11':
                            if level[int(mary)][int(marx - 1)].lower() == 'y':
                                level_name = '10'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 + 10
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                                player.rect.x += 1000
                        elif level_name == '8':
                            if level[int(mary)][int(marx - 1)] == 'y':
                                level_name = '9'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary)][int(marx + 1)] == 'y':
                                level_name = '10'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8
                                player = player[0]
                            elif level[int(mary + 1)][int(marx)] == 'y':
                                level_name = '4'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8 - 12
                                player = player[0]
                                player.rect.y -= 1200
                        elif level_name == '9':
                            if level[int(mary)][int(marx+1)] == 'y':
                                level_name = '8'
                                level = load_level(level_name)
                                all_sprites = pygame.sprite.Group()
                                wall_group = pygame.sprite.Group()
                                player_group = pygame.sprite.Group()
                                screen.blit(loading_image, (0, 0))
                                pygame.display.flip()
                                player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group,
                                                        load_image, player_group)
                                marx = player[1]
                                marx += 0.6 - 12
                                marx2 = marx - 0.2
                                mary = player[2] + 0.8 - 5
                                player = player[0]
                                player.rect.y -= 500
                                player.rect.x -= 1200
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    g_up = False
                    player.stopped()
                    if level_name != '7':
                        reverse = True
                    else:
                        reverse = False
                if event.key == pygame.K_LEFT:
                    g_left = False
                    player.stopped()
                    reverse = True
                if event.key == pygame.K_DOWN:
                    g_down = False
                    player.stopped()
                    if level_name == '7':
                        reverse = True
                if event.key == pygame.K_RIGHT:
                    g_right = False
                    player.stopped()
    if g_up:  # Движение вверх(прям как фильм)
        mary -= 0.06
        test = int(mary)
        if level[test][int(marx)] in walkfree and level[test][int(marx2)] in walkfree:
            player.rect.y -= 6
            went = True
            if level_name != '7':
                reverse = True
            else:
                reverse = False
        else:
            mary += 0.06
    if g_down:  # Вниз
        mary += 0.06
        test = int(mary)
        if level[test][int(marx)] in walkfree and level[test][int(marx2)] in walkfree:
            player.rect.y += 6
            went = True
            if level_name != '7':
                reverse = False
            else:
                reverse = True
        else:
            mary -= 0.06
    if g_right:  # Вправо
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
    if g_left:  # Влево
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
    if reverse:  # Проверка на поворот гг
        player.image = pygame.transform.flip(player.image, 1, 0)
        reverse = False
    if not startsc and not cutscene:  # Апдейт положения всех спрайтов на экране
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
    if cutscene and checkpoint == '1':  # Первая катсцена
        if cutloading:
            player.rect.x = 500
            player.rect.y = 1400
            brothimage = load_image('characters2', 'broth', 'png')
            dimi = load_image('characters2', 'dim', 'png')
            dim = Character(dimi, wall_group, all_sprites)
            broth = Character(brothimage, wall_group, all_sprites)
            broth.rect.y = 1300
            broth.rect.x = 500
            peri = load_image('characters2', 'per', 'png')
            seci = load_image('characters2', 'sec', 'png')
            thiri = load_image('characters2', 'thir', 'png')
            per = Character(peri, wall_group, all_sprites)
            sec = Character(seci, wall_group, all_sprites)
            thir = Character(thiri, wall_group, all_sprites)
            magi = load_image('characters2', 'mag', 'png')
            mag = Character(magi, wall_group, all_sprites)
            for i in range(11):
                brothrun.append(load_image('characters2', 'runbroth\Running_0' + str(i + 1), 'png'))
            for i in range(14):
                brothdie.append(load_image('characters2', 'diebroth\Dying_0' + str(i + 1), 'png'))
            for i in range(11):
                secslash.append(load_image('characters2', 'secslash\Rogue_Slashing_0' + str(i + 1), 'png'))
            for i in range(11):
                magwalk.append(load_image('characters2', 'magwalk\Running_0' + str(i + 1), 'png'))
            cutloading = False
        if walk:
            brothcount = (brothcount + 1) % 11
            broth.image = brothrun[brothcount]
            player.go()
            player.rect.x += 3
            broth.rect.x += 3
            if seconds >= 30:
                walk = False
                player.stopped()
                broth.image = load_image('characters2', 'broth', 'png')
        if walk2:
            pass
        if seconds == 0:  # Пошла раскадровка
            string1 = font.render("Сэм: Артур, помнишь Джека?", 1, pygame.Color('black'))
            string2 = font.render("", 1, pygame.Color('black'))
            string3 = font.render("", 1, pygame.Color('black'))
        if seconds >= 5:
            string1 = font.render('Артут: Да,конечно, его не забыть.', 1, pygame.Color('black'))
            string2 = font.render("", 1, pygame.Color('black'))
            string3 = font.render("", 1, pygame.Color('black'))
        if seconds >= 10:
            string1 = font.render("Сэм: Так вот ,этот негодяй подбил ", 1, pygame.Color('black'))
            string2 = font.render("на одно дело.", 1, pygame.Color('black'))
        if seconds >= 15:
            string1 = font.render('Артут: Так, Сэм, во что ты ввязался ?', 1, pygame.Color('black'))
            string2 = font.render("", 1, pygame.Color('black'))
            string3 = font.render("", 1, pygame.Color('black'))
        if seconds >= 20:
            string1 = font.render("Сэм: Эх...Как только мы проникли в дом,", 1, pygame.Color('black'))
            string2 = font.render("нас заметили охранники. Началась ", 1, pygame.Color('black'))
            string3 = font.render("перестрелка, и... Джэк убил его сына", 1, pygame.Color('black'))
        if seconds >= 25:
            string1 = font.render('Артут: Что? Чёрт тебя подери ,', 1, pygame.Color('black'))
            string2 = font.render("что вы наделали ,Сэм?", 1, pygame.Color('black'))
            string3 = font.render("", 1, pygame.Color('black'))
        if seconds >= 30:
            string1 = font.render('Пшшшшшшшшш', 1, pygame.Color('black'))
            string2 = font.render("", 1, pygame.Color('black'))
            string3 = font.render("*Чпоньк*", 1, pygame.Color('black'))
            dim.rect.x = 673
            dim.rect.y = 234
        if seconds >= 32:
            dim.rect.x = 10000
            dim.rect.y = 10000
            sec.rect.x = 673
            sec.rect.y = 234
            per.rect.x = 723
            per.rect.y = 250
            thir.rect.x = 673
            thir.rect.y = 334
            string1 = font.render('Сэм(шёпотом): это те ребята.', 1, pygame.Color('black'))
            string2 = font.render("И похоже, что они пришли за мной.", 1, pygame.Color('black'))
            string3 = font.render("Сэм(громко): Что вам надо от нас?", 1, pygame.Color('black'))
        if seconds >= 37:
            string1 = font.render('На данный момент всё', 1, pygame.Color('black'))
            string2 = font.render("Можете 'наслаждаться' открытым миром", 1, pygame.Color('black'))
            string3 = font.render("Продолжение позже", 1, pygame.Color('black'))
        if seconds >= 42:
            cutscene = False
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        screen.blit(font1, (236, 534))
        screen.blit(string1, font_1)
        screen.blit(string2, font_2)
        screen.blit(string3, font_3)
        seconds += 0.04
        if not cutscene:
            level_name = '2'
            checkpoint = '2'
            level = load_level(level_name)
            all_sprites = pygame.sprite.Group()
            wall_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            screen.blit(loading_image, (0, 0))
            pygame.display.flip()
            player = generate_level(level,  Tile, level_name, Player, all_sprites, wall_group, load_image, player_group)
            marx = player[1]
            marx += 0.6 - 28
            marx2 = marx - 0.2
            mary = player[2] + 0.8 + 5
            player = player[0]
            player.rect.x -= 2800
            player.rect.y += 500
    if not startsc and not cutscene:
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
