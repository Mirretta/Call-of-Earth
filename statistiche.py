from settings import *

def run(name,skin,canestri,spazzatura,distrutta,vittorie,test,minuti,minuti_ora):
    screen = pygame.display.get_surface()
    
    name = name.split('\r')
    
    titolo_text = test_font2.render(f'Statistiche di {name[0]}',False,'black')
    titolo_rect = titolo_text.get_frect(center = (400,80))
    
    start_time = pygame.time.get_ticks()
    
    minuti += minuti_ora
    
    stat_1 = test_font.render(f'canestri fatti: {canestri}',False,'black')
    stat_2 = test_font.render(f'Spazzatura raccolta: {spazzatura}',False,'black')
    stat_3 = test_font.render(f'Spazzatura distrutta: {distrutta}',False,'black')
    stat_4 = test_font.render(f'Nemici distrutti: {vittorie}',False,'black')
    stat_5 = test_font.render(f'Test fatti: {test}',False,'black')
    stat_6 = test_font.render(f'Skin attuale: {skin}',False,'black')
    stat_7 = test_font.render(f'Minuti giocati: {int(minuti)}',False,'black')
    
    stats = [stat_1,stat_2,stat_3,stat_4,stat_5,stat_6,stat_7]
    
    music_timer = time.time()
    start_music = True
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, minuti
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos):
                        running = False
                        
        passed_time = ((pygame.time.get_ticks() - start_time) / 1000) / 60
        
        screen.fill('light blue')
        
        screen.blit(titolo_text,titolo_rect)
        stat_rect = pygame.draw.rect(screen,'black',(200,150,400,400),5,border_radius=12)
        
        screen.blit(exit_surface,exit_rect)
        
        for index, stat in enumerate(stats):
            screen.blit(stat,(220,(stat_rect.height / 7) * index + 170))
        
        end_timer = time.time() - music_timer
        
        if end_timer >= 0.5 and start_music:
            bg_sounds[5].play(loops=-1)
            start_music = False
            
        pygame.display.update()
        
    minuti += passed_time
    
    bg_sounds[5].fadeout(750)  
    return True, minuti