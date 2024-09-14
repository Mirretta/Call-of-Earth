from settings import *
from classi import Player, Obstacle, Bullet, Line
from pygame.math import Vector2

pygame.init()


def update_score():
    screen = pygame.display.get_surface()
    global score, counter
    if pygame.sprite.groupcollide(bullet_group, bad_obstacle_group, True, True, pygame.sprite.collide_mask):
        score += 1
        counter += 1
    score_surface = test_font.render(f'Punteggio: {score}', False, 'black')
    pygame.draw.rect(screen,'light gray',(450 - 10, 50 - 10,score_surface.get_width() + 20,score_surface.get_height() + 10),border_radius=12)
    score_rect = score_surface.get_frect(topleft=(450, 50))
    screen.blit(score_surface, score_rect)


def check_collision(Player1, line1, max_counter):
    global strike, counter
    game_active = True
    cnt = 265
    screen = pygame.display.get_surface()
    bad_sound = pygame.mixer.Sound(join('Audio','Punteggio','wrong.wav'))
    strike_surface = pygame.image.load(join('Grafiche','Altro','red_cross.png')).convert_alpha()
    if pygame.sprite.spritecollide(Player1, bad_obstacle_group, True):
        strike += 1
        bad_sound.play()
        max_counter = counter if counter > max_counter else max_counter
        counter = 0
    elif pygame.sprite.spritecollide(line1, bad_obstacle_group, True):
        strike += 1
        bad_sound.play()
        max_counter = counter if counter > max_counter else max_counter
        counter = 0
    if strike == 3:
        game_active = False
        bad_obstacle_group.empty()
        bullet_group.empty()
        line_group.empty()
        player_group.empty()
    strike_text = test_font.render('Errori: ',False,'black')
    strike_surface = pygame.transform.scale(strike_surface,(30,strike_text.get_height()))
    pygame.draw.rect(screen,'light gray',(160,40,strike_text.get_width() + 110,strike_text.get_height() + 10),border_radius=12)
    for i in range(strike):
        strike_rect = strike_surface.get_frect(topleft=(cnt, 47))
        screen.blit(strike_surface, strike_rect)
        cnt += 30
    screen.blit(strike_text,(170,50))
    return game_active, max_counter


def run():
    global score, strike, start_game, counter
    x, y = 900, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Prova Gioco')
    
    score = counter = max_counter = 0

    bullet = Bullet(x, y)

    # background
    sky_surface = pygame.surface.Surface((500, 700))
    sky_surface.fill('light blue')
    game1_surface_void = pygame.surface.Surface((150, 700))
    
    # sounds
    num = randint(0,3)
    shoot_sound = pygame.mixer.Sound(join('Audio','Player','shoot.wav'))

    # timers
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 500)

    previous_time = time.time()
    running = True
    while running:
        dt = time.time() - previous_time
        previous_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return False, 0, 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos):
                        running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start_game:
                    start_game = True
                    bg_sounds[num].play(loops=-1)
                    score = strike = 0
                    pygame.time.set_timer(obstacle_timer, 750)
                    line1 = Line(2)
                    line_group.add(line1)
                    player1 = Player(3, 0, 3)
                    player_group.add(player1)
                    yVelocity = 500
            if start_game:
                if event.type == obstacle_timer:
                    obstacle = Obstacle(2, 0, 3)
                    bad_obstacle_group.add(obstacle)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and len(bullet_group.sprites()) <= 2:
                        x, y = player1.player_movement(dt)
                        shoot_sound.play()
                        bullet = Bullet(x, y)
                        bullet_group.add(bullet)

        if start_game:
            screen.fill('black')
            screen.blit(sky_surface, (150, 10))
            screen.blit(game1_surface_void, (650, 0))

            update_score()

            line_group.draw(screen)
            player_group.draw(screen)
            player_group.update(dt)

            bad_obstacle_group.update(yVelocity,dt)
            bad_obstacle_group.draw(screen)

            bullet_group.draw(screen)
            bullet_group.update(dt)

            start_game, max_counter = check_collision(player1, line1, max_counter)

            if bullet.rect.centery <= -40:
                bullet_group.remove(bullet)
                
        else:
            screen.fill('light blue')
            introduction_surface = test_font2.render('Elimina la spazzatura!', False, 'black')
            introduction_rect = introduction_surface.get_frect(center=(400, 300))
            screen.blit(introduction_surface, introduction_rect)
            screen.blit(exit_surface, exit_rect)
            bg_sounds[num].fadeout(750)
            if score > 0:
                score_text = test_font4.render(f'Punteggio: {score}',False,'black')
                score_rect = score_text.get_frect(center=(400,100))
                screen.blit(score_text,score_rect)
            screen.blit(instruction_surf,instruction_rect)

        pygame.display.flip()

    return True, score, max_counter
