from settings import *
from classi import Player, Obstacle, Road, Line

pygame.init()


def check_collision(Player1, enemy, line2):
    global strike
    game_active = True
    vicotry = False
    cnt = 175
    bad_sound = pygame.mixer.Sound(join('Audio','Punteggio','wrong.wav'))
    screen = pygame.display.get_surface()
    strike_surface = pygame.image.load(join('Grafiche','Altro','red_cross.png')).convert_alpha()
    if pygame.sprite.spritecollide(line2, good_obstacle_group, True) or pygame.sprite.spritecollide(Player1, bad_obstacle_group, True):
        strike += 1
        bad_sound.play()
    if strike == 3:
        game_active = False
        player_group.empty()
        good_obstacle_group.empty()
        bad_obstacle_group.empty()
        amazing_obstacle_group.empty()
    if Player1.rect.right >= 540:
        vicotry = True
    strike_text = test_font.render('Errori: ',False,'black')
    strike_surface = pygame.transform.scale(strike_surface,(30,strike_text.get_height()))
    pygame.draw.rect(screen,'light gray',(70,30,strike_text.get_width() + 110,strike_text.get_height() + 10),border_radius=12)
    for i in range(strike):
        strike_rect = strike_surface.get_frect(topleft=(cnt, 37))
        screen.blit(strike_surface, strike_rect)
        cnt += 30
    screen.blit(strike_text,(80,40))

    return game_active, vicotry


def update_score(max_pos, Player1):
    global strike, score
    power_up = pygame.mixer.Sound(join('Audio','power_up.wav'))
    good_sound = pygame.mixer.Sound(join('Audio','Punteggio','good.wav'))
    screen = pygame.display.get_surface()
    if pygame.sprite.spritecollide(Player1, good_obstacle_group, True):
        score += 1
        good_sound.play()
    if pygame.sprite.spritecollide(Player1, amazing_obstacle_group, True):
        max_pos += 75
        power_up.play()
    score_surface = test_font.render(f'Punteggio: {score}', False, 'black')
    pygame.draw.rect(screen,'light gray',(480 - 10, 40 - 10, score_surface.get_width() + 20, score_surface.get_height() + 10),border_radius=12)
    score_rect = score_surface.get_frect(topleft=(480, 40))
    screen.blit(score_surface, score_rect)
    return max_pos


def run(car):
    global score, strike, start_game
    screen = pygame.display.get_surface()
    lane = 299
    road_y = 156
    counter = road_x = score = cnt = victory_counter = 0
    max_pos = 150
    
    victory = False
    
    player = pygame.image.load(join('Grafiche','Macchine',f'{car}')).convert_alpha()
    
    tint_surf = pygame.Surface((WIDTH,HEIGHT))
    tint_surf.set_alpha(cnt)
    
    # sounds
    victory_sound = pygame.mixer.Sound(join('Audio','victory.wav'))
    num_sound = randint(0,3)

    road_surface = pygame.surface.Surface((800, 400))
    road_surface.fill((104,108,94))
    road1_rect = road_surface.get_frect(topleft=(0, 100))

    road_group = pygame.sprite.Group()
    for i in range(3):
        for j in range(5):
            road = Road(road_x, road_y)
            road_group.add(road)
            road_x += 180
        road_y += 133.5
        road_x = 0

    obstacle_frequency = 800
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, obstacle_frequency)

    obstacle_diffculty_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(obstacle_diffculty_timer, 8000)

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
                    if not victory:
                        start_game = True
                        bg_sounds[num_sound].play(loops=-1)
                        score = strike = counter = passed_time = 0
                        start_time = pygame.time.get_ticks()
                        max_pos = 150
                        player1 = Player(4, 299, 4,player_stand=player)
                        enemy = Player(5, 299, 4)
                        player_group.add(player1, enemy)
                        line2 = Line(1)
                        line_group.add(line2)
                        good_timer_start = pygame.time.get_ticks()
                        time_num = randint(15,25)
            if start_game:
                if event.type == obstacle_diffculty_timer:
                    if obstacle_frequency > 500:
                        obstacle_frequency -= 100
                        pygame.time.set_timer(obstacle_timer, obstacle_frequency)
                if event.type == obstacle_timer and passed_time > 0.75:
                    num = choice([166, 299, 432])
                    enemy.car_player_movement(num)
                    if good_timer_end >= time_num:
                        good_obstacle = Obstacle(6, num, 4)
                        amazing_obstacle_group.add(good_obstacle)
                        counter = 0
                        good_timer_start = pygame.time.get_ticks()
                        time_num = randint(15,25)
                    else:
                        num2 = choice([1, 1, 1, 3])
                        if num2 == 1:
                            obstacle = Obstacle(7, num, 4)
                            good_obstacle_group.add(obstacle)
                        else:
                            bad_obstacle = Obstacle(3, num, 4)
                            bad_obstacle_group.add(bad_obstacle)
                    counter += 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        lane -= 133
                        if lane <= 166:
                            lane = 166
                    if event.key == pygame.K_DOWN:
                        lane += 133
                        if lane >= 432:
                            lane = 432
                    player1.car_player_movement(lane)

        if start_game:

            screen.fill('light blue')
            line_group.draw(screen)
            screen.blit(road_surface, road1_rect)

            pygame.draw.line(screen, 'white', (0, 100), (800, 100), 5)
            pygame.draw.line(screen, 'white', (0, 233), (800, 233), 5)
            pygame.draw.line(screen, 'white', (0, 366), (800, 366), 5)
            pygame.draw.line(screen, 'white', (0, 500), (800, 500), 5)

            if not victory:
                max_pos = update_score(max_pos, player1)
                start_game, victory = check_collision(player1, enemy, line2)

            road_group.draw(screen)
            road_group.update(dt)

            amazing_obstacle_group.update(0,dt)
            amazing_obstacle_group.draw(screen)
            good_obstacle_group.update(0,dt)
            good_obstacle_group.draw(screen)
            bad_obstacle_group.update(0,dt)
            bad_obstacle_group.draw(screen)
                
            if start_time != 0:
                passed_time = (pygame.time.get_ticks() - start_time) / 1000
            
            player_group.draw(screen)
            player1.change_position(max_pos,dt)
            
            good_timer_end = (pygame.time.get_ticks() - good_timer_start) / 1000
            
            if victory:
                tint_surf.set_alpha(cnt)
                cnt += 140 * dt
                if cnt >= 255: start_game = False; victory_sound.play()
                
            screen.blit(tint_surf,(0,0))

        else:
            screen.fill('light blue')
            introduction_surface = test_font2.render('Elimina il nemico!', False, 'black') if not victory else test_font2.render('Hai Vinto!', False, 'black')
            introduction_rect = introduction_surface.get_frect(center=(400, 300))
            screen.blit(introduction_surface, introduction_rect)
            screen.blit(exit_surface, exit_rect)
            bg_sounds[num_sound].fadeout(750)
            if score > 0:
                score_text = test_font4.render(f'Punteggio: {score}',False,'black')
                score_rect = score_text.get_frect(center=(400,100))
                screen.blit(score_text,score_rect)
            victory_counter = 1 if victory else 0
            if not victory:
                screen.blit(instruction_surf,instruction_rect)

        pygame.display.update()

    return True, score, victory_counter
