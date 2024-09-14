import pygame, sys, time
from random import randint, choice
from os.path import join
from pygame.math import Vector2

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

strike = score = 0
start_game = False

test_font = pygame.font.Font(join('Font','Pixeltype.ttf'), 40)
test_font2 = pygame.font.Font(join('Font','Pixeltype.ttf'), 90)
test_font3 = pygame.font.Font(join('Font','Pixeltype.ttf'), 130)
test_font4 = pygame.font.Font(join('Font','Pixeltype.ttf'),60)
test_font5 = pygame.font.Font(join('Font','Pixeltype.ttf'),35)
test_font6 = pygame.font.Font(join('Font','Pixeltype.ttf'),20)

player_group = pygame.sprite.Group()
good_obstacle_group = pygame.sprite.Group()
bad_obstacle_group = pygame.sprite.Group()
line_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
amazing_obstacle_group = pygame.sprite.Group()

exit_surface = pygame.image.load(join('Grafiche','Altro','red_cross.png'))
exit_rect = exit_surface.get_rect(center=(750, 50))

instruction_surf = test_font.render('Premere spazio per iniziare',False,'black')
instruction_rect = instruction_surf.get_frect(center=(400,500))

music_1 = pygame.mixer.Sound(join('Audio','Sottofondo','music_1.mp3'))
music_1.set_volume(10)

bg_sounds = {
    0 : music_1,
    1 : pygame.mixer.Sound(join('Audio','Sottofondo','music_2.mp3')),
    2 : pygame.mixer.Sound(join('Audio','Sottofondo','music_3.mp3')),
    3 : pygame.mixer.Sound(join('Audio','Sottofondo','music_4.mp3')),
    4 : pygame.mixer.Sound(join('Audio','Sottofondo','quiz_music.mp3')),
    5 : pygame.mixer.Sound(join('Audio','Sottofondo','shop_music.mp3'))
}

clock = pygame.time.Clock()
