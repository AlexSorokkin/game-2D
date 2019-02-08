import pygame


class Camera:  # Класс камеры, нужен для повышения производительности
    def __init__(self, width, height):  # Ибо без неё не больше 1 кадра в 5 секунд
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.x = 1240 / 2
        self.y = 768 / 2

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.width // 2)
        self.x -= self.dx
        self.dy = -(target.rect.y + target.rect.h // 2 - self.height // 2)
        self.y -= self.dy


class Character(pygame.sprite.Sprite):  # Класс персонажей
    def __init__(self, images, wall_group, all_sprites):
        group = wall_group
        super().__init__(group, all_sprites)
        self.image = images
        self.rect = self.image.get_rect()
        self.rect.x = 7000
        self.rect.y = 7000


class Tile(pygame.sprite.Sprite):  # Класс всех спрайтов(домов, деревьев, дрог и т.д.)
    def __init__(self, tile_type, pos_x, pos_y, all_sprites, wall_group, load_image, level_name):
        group = wall_group
        super().__init__(group, all_sprites)
        if tile_type == 'walkgrass':
            self.image = load_image(level_name, 'grass', 'png')
        elif tile_type == 'wallstone':
            self.image = load_image(level_name, 'stone', 'png')
        self.image = load_image(level_name, tile_type[4:], 'png')
        self.rect = self.image.get_rect().move(
            100 * pos_x, 100 * pos_y)


class Player(pygame.sprite.Sprite):  # Класс ГГ
    def __init__(self, pos_x, pos_y, all_sprites, player_group, load_image):
        super().__init__(player_group, all_sprites)
        self.load = load_image
        self.image = load_image('character', 'DLE', 'png')
        self.images = []
        self.count = 0
        for i in range(11):
            self.images.append(load_image('character', 'Run\Running_0' + str(i + 1), 'png'))
        self.rect = self.image.get_rect().move(
            100 * pos_x, 100 * pos_y)

    def stopped(self):  # Остановка
        self.image = self.load('character', 'DLE', 'png')
        self.count = 0

    def go(self):  # Анимация бега
        self.image = self.images[self.count]
        self.count = (self.count + 1) % 11
