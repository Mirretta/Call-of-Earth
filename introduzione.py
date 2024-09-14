from settings import *


def run():
    screen = pygame.display.get_surface()

    player_name = ''
    text_surf = test_font2.render('Qual e\' il tuo nickname?',False,'black')
    text_rect = text_surf.get_frect(center=(400,150))
    active = False
    line_x = 110
    
    cursor_visible = True
    cursor_last_blink = pygame.time.get_ticks()
    cursor_blink_rate = 500
    
    input_rect = pygame.FRect(100,300,600,100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        if len(player_name) < 10:
                            player_name += event.unicode
                        
                if event.key == pygame.K_RETURN:
                    running = False

        screen.fill('light blue')
        
        if active:
            if cursor_visible: line = pygame.draw.line(screen,'black',(line_x,310),(line_x,390),5)
            current_time = pygame.time.get_ticks()
            if current_time - cursor_last_blink >= cursor_blink_rate:
                cursor_visible = not cursor_visible
                cursor_last_blink = current_time
            
        user_text = test_font3.render(player_name,False,'black')
        user_rect = user_text.get_frect(topleft=(input_rect.x + 10,input_rect.y + 15))
        max_text = test_font.render(f'Caratteri utilizzati {len(player_name)} / 10',False,'black')
        max_rect = max_text.get_frect(center=(400,500))
        screen.blit(max_text,max_rect)
        line_x = user_rect.right
        screen.blit(user_text,user_rect)
        
        screen.blit(text_surf,text_rect)
        pygame.draw.rect(screen,'black',input_rect,5)
        

        clock.tick(60)
        pygame.display.update()

    return player_name
