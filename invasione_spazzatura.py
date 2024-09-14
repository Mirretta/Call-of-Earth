from settings import *
from classi import Player, Obstacle

pygame.init()


def update_score(player_hitbox):
    global score
    screen = pygame.display.get_surface()
    good_sound = pygame.mixer.Sound(join('Audio','Punteggio','good.wav'))
    if pygame.sprite.spritecollide(player_hitbox, good_obstacle_group, True):
        score += 1
        good_sound.play()
    score_surface = test_font.render(f'Punteggio: {score}', False, 'black')
    pygame.draw.rect(screen,'light gray',(450 - 10, 50 - 10,score_surface.get_width() + 20,score_surface.get_height() + 10),border_radius=12)
    screen.blit(score_surface, (450,50))


def check_collision(player_hitbox):
    global strike
    start_game = True
    cnt = 265
    bad_sound = pygame.mixer.Sound(join('Audio','Punteggio','wrong.wav'))
    strike_surface = pygame.image.load(join('Grafiche','Altro','red_cross.png')).convert_alpha()
    screen = pygame.display.get_surface()
    if pygame.sprite.spritecollide(player_hitbox, bad_obstacle_group, True):
        strike += 1
        bad_sound.play()
        if strike == 3:
            start_game = False
            good_obstacle_group.empty()
            bad_obstacle_group.empty()
            player_group.empty()
    strike_text = test_font.render('Errori: ',False,'black')
    strike_surface = pygame.transform.scale(strike_surface,(30,strike_text.get_height()))
    pygame.draw.rect(screen,'light gray',(160,40,strike_text.get_width() + 110,strike_text.get_height() + 10),border_radius=12)
    for i in range(strike):
        strike_rect = strike_surface.get_frect(topleft=(cnt, 47))
        screen.blit(strike_surface, strike_rect)
        cnt += 30
    screen.blit(strike_text,(170,50))
    return start_game


def run(skin):
    global score, strike, start_game

    screen = pygame.display.get_surface()
    
    score = wait_time = 0
    
    player_walk_1 = pygame.image.load(join('Grafiche','Player',f'{skin.capitalize()}',f'{skin}_walk_1.png')).convert_alpha()
    player_walk_2 = pygame.image.load(join('Grafiche','Player',f'{skin.capitalize()}',f'{skin}_walk_2.png')).convert_alpha()
    
    player_stand = pygame.image.load(join('Grafiche','Player',f'{skin.capitalize()}',f'{skin}_stand.png')).convert_alpha()
    player_frames = [player_walk_1,player_walk_2]
    
    # sounds
    num_sound = randint(0,3)
    
    # background
    sky_surface = pygame.image.load(join('Grafiche','Background','sky.png'))
    sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1.3)
    ground_surface = pygame.image.load(join('Grafiche','Background','ground.png'))
    game1_surface_void = pygame.surface.Surface((150, 700))
    extreme_mode = test_font.render('Modalita\' estrema', False, 'black')
    extreme_mode_rect = extreme_mode.get_frect(center=(400, 150))

    # timers
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 750)

    obstacle_difficulty_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(obstacle_difficulty_timer, 10000)
    
    start_time = time.time()
    
    previous_time = time.time()
    running = True
    while running:
        dt = time.time() - previous_time
        previous_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos):
                        running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start_game:
                    score = strike = wait_time = 0
                    start_time = time.time()
                    start_game = True
                    bg_sounds[num_sound].play(loops=-1)
                    obstacle_list = [5, 5, 5, 5, 5, 2]
                    yVelocity = 500
                    player1 = Player(1, 0, 2,player_stand=player_stand,player_frames=player_frames)
                    player_hitbox = Player(2, 0, 2)
                    player_group.add(player1, player_hitbox)
            if start_game:
                if event.type == obstacle_timer and wait_time > 1.5:
                    num = choice(obstacle_list)
                    if num == 5:
                        good_obstacle_group.add(Obstacle(2, 0, 2))
                    else:
                        bad_obstacle_group.add(Obstacle(5, 0, 2))
                if event.type == obstacle_difficulty_timer and obstacle_list.count(2) < 5:
                    obstacle_list.append(2)
                if event.type == obstacle_difficulty_timer and yVelocity < 700:
                    yVelocity += 100

        if start_game:
            screen.fill('black')
            screen.blit(sky_surface, (150, 0))
            screen.blit(ground_surface, (150, 500))
            screen.blit(game1_surface_void, (650, 0))

            player_group.draw(screen)
            player_group.update(dt)
            

            good_obstacle_group.update(yVelocity,dt)
            good_obstacle_group.draw(screen)
            bad_obstacle_group.update(yVelocity,dt)
            bad_obstacle_group.draw(screen)
            
            update_score(player_hitbox)
            start_game = check_collision(player_hitbox)
            
            if yVelocity == 700:
                screen.blit(extreme_mode, extreme_mode_rect)
                
            wait_time = time.time() - start_time

        else:
            screen.fill('light blue')
            introduction_surface = test_font2.render('Raccogli la spazzatura!', False, 'black')
            introduction_rect = introduction_surface.get_frect(center=(400, 300))
            screen.blit(introduction_surface, introduction_rect)
            screen.blit(exit_surface, exit_rect)
            bg_sounds[num_sound].fadeout(750)
            if score > 0:
                score_text = test_font4.render(f'Punteggio: {score}',False,'black')
                score_rect = score_text.get_frect(center=(400,100))
                screen.blit(score_text,score_rect)
            screen.blit(instruction_surf,instruction_rect)

        pygame.display.update()

    return True, score
