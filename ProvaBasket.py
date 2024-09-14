from settings import *
from classi import Trash, Obstacle

pygame.init()


def update_score(start_game, start_time):
    global score
    screen = pygame.display.get_surface()
    score_surface = test_font4.render(f'Punteggio: {score}', False, 'black')
    pygame.draw.rect(screen,'light gray',(400 - 10,100 - 10,score_surface.get_width() + 20, score_surface.get_height() + 10),border_radius=12)
    screen.blit(score_surface, (400,100))
    if start_game:
        time = int((pygame.time.get_ticks() - start_time) / 1000)
        time_text = test_font4.render('Tempo: ',False,'black')
        time_surface = test_font4.render(f'{time}', False, 'black')
        if time >= 15:
            time_surface = test_font4.render(f'{time}', False, 'yellow')
        if time >= 25:
            time_surface = test_font4.render(f'{time}', False, 'red')
        pygame.draw.rect(screen,'light gray',(90,90,time_surface.get_width() + time_text.get_width() + 20, time_surface.get_height() + 10),border_radius=12)
        screen.blit(time_text,(100,100))
        screen.blit(time_surface, (100 + time_text.get_width(),100))


def run(skin):
    global score, start_game
    screen = pygame.display.get_surface()
    player_gravity = 0
    size_increase = 7
    normal_size = 290
    right_collison = rule_check = False
    
    rules = ['Cestino azzuro: Carta','Cestino grigio: Indifferenziata','Cestino giallo: Plastica','Cestino marrone: Umido','Cestino verde: Vetro']
    
    tint_surf = pygame.Surface((WIDTH,HEIGHT))
    tint_surf.set_alpha(200)
    
    score = 0
    
    # sounds
    jump_sound = pygame.mixer.Sound(join('Audio','Player','jump.wav'))
    good_sound = pygame.mixer.Sound(join('Audio','Punteggio','good.wav'))
    bad_sound = pygame.mixer.Sound(join('Audio','Punteggio','wrong.wav'))
    num = randint(0,3)

    sky_surface = pygame.image.load(join('Grafiche','Background','sky.png')).convert()
    sky_surface = pygame.transform.rotozoom(sky_surface, 0, 1.3)
    ground_surface = pygame.image.load(join('Grafiche','Background','ground.png')).convert()
    reaction_surf = pygame.image.load(join('Grafiche','Altro','thumbs_up.png')).convert_alpha()
    info_surf = pygame.image.load(join('Grafiche','Altro','info.png')).convert_alpha()
    info_rect = info_surf.get_frect(topleft=(10,25))
    reaction_rect = reaction_surf.get_frect(center=(520, 300))
    
    title_text = test_font2.render('Cestini',False,'black')
    title_rect = title_text.get_frect(center=(400,100))
    
    player_stand = pygame.image.load(join('Grafiche','Player',f'{skin.capitalize()}',f'{skin}_stand.png')).convert_alpha()
    player_jump = pygame.image.load(join('Grafiche','Player',f'{skin.capitalize()}',f'{skin}_jump.png')).convert_alpha()
    player_surface = player_stand
    player_rect = player_surface.get_frect(center=(100, 470))
    
    rules_rect = pygame.FRect((100,50),(600,500))

    balls = pygame.sprite.Group()

    trash_can_group = pygame.sprite.Group()
    trash_can1 = Trash(1)
    trash_can2 = Trash(2)
    trash_can3 = Trash(3)
    trash_can4 = Trash(4)
    trash_can5 = Trash(5)
    trash_can_group.add(trash_can1, trash_can2, trash_can3, trash_can4, trash_can5)

    game_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(game_timer, 30000)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return False, 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos) and not rule_check:
                        running = False
                    if exit_rect.collidepoint(event.pos) and rule_check:
                        rule_check = False
                    if info_rect.collidepoint(event.pos):
                        rule_check = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start_game and not rule_check:
                    start_game = True
                    bg_sounds[num].play(loops=-1)
                    throwing = False
                    start_time = pygame.time.get_ticks()
                    score = reaction_timer = passed_time = k = h = r = speed = 0
                    reaction_surface = None 
                    current_pos = current_normal_size = 120
                    ball = Obstacle(1, 0, 1)
                    balls.add(ball)
                    player_rect.bottom = 500
                if start_game:
                    if event.key == pygame.K_UP:
                        if player_rect.bottom == 500 and pygame.K_SPACE:
                            player_gravity = -20
                            jump_sound.play()
                            current_normal_size = normal_size + 110
                            k, r, h = ball.lower_semicircle_equation(120,500,current_normal_size,450)
                            throwing = True
                        normal_size = 100
            if event.type == game_timer and start_game:
                start_game = False
                bg_sounds[num].fadeout(750)
                balls.empty()

        if start_game:
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 500))
            screen.blit(player_surface, player_rect)

            player_gravity += 1
            player_rect.y += player_gravity 
            if player_rect.bottom >= 500:
                player_rect.bottom = 500
                player_surface = player_stand
                
            if player_rect.bottom < 500:
                player_surface = player_jump

            if keys[pygame.K_SPACE] and player_rect.bottom == 500:
                pygame.draw.arc(screen, 'green', ((120, 200), (normal_size, 500)), 0, 3.14,3)
                normal_size += size_increase 
            
            if not keys[pygame.K_SPACE]:
                normal_size = 100
                
            if normal_size > 680 or normal_size < 100:
                size_increase *= -1
                
            throwing, speed = ball.throw(current_normal_size,throwing,k,r,h,current_pos)
            
            current_pos += speed 
            
            if current_pos > current_normal_size:
                throwing = False
                reaction_timer = pygame.time.get_ticks()
                right_collison = ball.check_throw(current_pos)
                current_pos = 120
                ball.kill()
                ball = Obstacle(1, 0, 1)
                balls.add(ball)
                if right_collison:
                    score += 1
                    reaction_surface = reaction_surf
                    good_sound.play()
                else:
                    reaction_surface = pygame.transform.flip(reaction_surf,False,True)
                    bad_sound.play()
                    
            if reaction_timer != 0:
                passed_time = (pygame.time.get_ticks() - reaction_timer) / 1000
                    
            if passed_time < 0.5 and reaction_surface:
                screen.blit(reaction_surface, reaction_rect)
                
            right_collison = False

            balls.update(0,1)
            balls.draw(screen)

            update_score(start_game, start_time)

            trash_can_group.draw(screen)
            trash_can_group.update()

        else:
            screen.fill('light blue')
            introduction_surface = test_font2.render('Fai piu\' canestri che puoi!', False, 'black')
            introduction_rect = introduction_surface.get_frect(center=(400, 300))
            screen.blit(introduction_surface, introduction_rect)
            screen.blit(info_surf,info_rect)
            if score > 0:
                score_text = test_font4.render(f'Punteggio {score}',False,'black')
                score_rect = score_text.get_frect(center=(400,100))
                screen.blit(score_text,score_rect)
            
            if rule_check:
                screen.blit(tint_surf,(0,0))
                pygame.draw.rect(screen,'light blue',rules_rect,border_radius=12)
                screen.blit(title_text,title_rect)
                for index, rule in enumerate(rules):
                    rule_text = test_font.render(rule,False,'black')
                    screen.blit(rule_text,(150,((rules_rect.width / 5 - 40) * index + 160)))
                    pygame.draw.circle(screen,'black',(125,((rules_rect.width / 5 - 40) * index + 170)),5)
                    
            screen.blit(exit_surface, exit_rect)
            screen.blit(instruction_surf,instruction_rect)

        clock.tick(FPS)
        pygame.display.update()
        
    return True, score
