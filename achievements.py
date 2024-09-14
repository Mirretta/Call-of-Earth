from settings import *
import json
from classi import Button

pygame.init()

def update_progress(num1,num2,num3,num4,num5):
    achv_progression = [[15,30,50],[50,75,100],[10,15,20],[1,2,3],[5,10,20]]
    
    n1 = n2 = n3 = n4 = n5 = None
    
    for index, achv in enumerate(achv_progression[0]):
        if num1 < achv:
            n1 = index 
            break
        
    if n1 == None: n1 = 3
    
    for index, achv in enumerate(achv_progression[1]):
        if  num2 < achv:
            n2 = index 
            break
    
    if n2 == None: n2 = 3
     
    for index, achv in enumerate(achv_progression[2]):
        if num3 < achv:
            n3 = index 
            break

    if n3 == None: n3 = 3
    
    for index, achv in enumerate(achv_progression[3]):
        if num4 < achv:  
            n4 = index 
            break
        
    if n4 == None: n4 = 3
    
    for index, achv in enumerate(achv_progression[4]):
        if num5 < achv:
            n5 = index 
            break
        
    if n5 == None: n5 = 3
        
    return n1,n2,n3,n4,n5
    

def run(num1,num2,num3,num4,num5,coins):
    screen = pygame.display.get_surface()
    title = test_font2.render('Obiettivi', False, 'black')
    title_rect = title.get_frect(center=(400, 60))
    achv1_progress = 25
    achv2_progress = 50
    achv3_progress = 10
    achv4_progress = 1
    achv5_progress = 5
    
    data = {}
    try:
        with open(join('Salvataggio','achievement_riscattato.txt')) as save_file:
            data = json.load(save_file)
    except:
        data = {'reward_1' : False, 'reward_2' : False, 'reward_3' : False, 'reward_4' : False, 'reward_5' : False}
    
    if num1 >= 15: achv1_progress = 30
    if num1 >= 30: achv1_progress = 50
    
    if num2 >= 50: achv2_progress = 75
    if num2 >= 75: achv2_progress = 100
    
    if num3 >= 10: achv3_progress = 15
    if num3 >= 15: achv3_progress = 20
    
    if num4 >= 1: achv4_progress = 2
    if num4 >= 2: achv4_progress = 3
    
    if num5 >= 5: achv5_progress = 10
    if num5 >= 10: achv5_progress = 20
    
    a, b, c, d, e = update_progress(num1,num2,num3,num4,num5)
    
    rule_check = False
    
    info_surf = pygame.image.load(join('Grafiche','Altro','info.png'))
    info_rect = info_surf.get_frect(topleft=(10,25))
    
    achievement_done_sound = pygame.mixer.Sound(join('Audio','achievement_complete.wav'))
    not_unlocked_sound = pygame.mixer.Sound(join('Audio','Negozio','locked_item.wav'))
    
    tint_surf = pygame.Surface((WIDTH,HEIGHT))
    tint_surf.set_alpha(200)
    
    rules_rect = pygame.FRect((100,50),(600,500))
    
    rule_title = test_font2.render('Regole',False,'black')
    rule_title_rect = rule_title.get_frect(center = (400,100))
    
    rules = ['Fai 75 canestri IN TUTTO!',
             'Raccogli 200 rifiuti IN TUTTO!',
             'Distruggi 15 rifiuti SENZA ERRRORI!',
             'Abbatti il nemico 5 VOLTE!',
             'Rispondi a TUTTE le domande correttamente!'
            ]
    
    achv1_surf = test_font4.render('Superstar del basket ' + 'I ' * a,False,'black')
    achv2_surf = test_font4.render('Raccoglitore folle ' + 'I ' * b,False,'black')
    achv3_surf = test_font4.render('Occhio di falco ' + 'I ' * c,False,'black')
    achv4_surf = test_font4.render('Guidatore provetto ' + 'I ' * d,False,'black')
    achv5_surf = test_font4.render('Ecologista sapiente ' + 'I ' * e,False,'black')
    
    progress_game1 = test_font5.render(f'Canestri fatti: {num1 if num1 <= 50 else 50} / {achv1_progress}',False,'black')
    progress_game2 = test_font5.render(f'Spazzatura raccolta: {num2 if num2 <= 100 else 100} / {achv2_progress}',False,'black')
    progress_game3 = test_font5.render(f'Spazzatura distrutta: {num3 if num3 <= 20 else 20} / {achv3_progress}',False,'black')
    progress_game4 = test_font5.render(f'Vittorie: {num4 if num4 <= 3 else 3} / {achv4_progress}',False,'black')
    progress_game5 = test_font5.render(f'Risposte corrette: {num5 if num5 <= 20 else 20} / {achv5_progress}',False,'black')
    
    surfaces = [achv1_surf,achv2_surf,achv3_surf,achv4_surf,achv5_surf]
    
    progress_surf = [progress_game1,progress_game2,progress_game3,progress_game4,progress_game5]
    
    button1 = Button('Ricompensa: 175',200,70,(550,120),6)
    button2 = Button('Ricompensa: 150',200,70,(550,220),6)
    button3 = Button('Ricompensa: 150',200,70,(550,320),6)
    button4 = Button('Ricompensa: 200',200,70,(550,420),6)
    button5 = Button('Ricompensa: 150',200,70,(550,520),6)
    
    buttons = [button1,button2,button3,button4,button5]
    
    bg_rect = pygame.Surface((WIDTH, 500))
    bg_rect.fill('light gray')
    bg_rect.set_alpha(100)
    
    num = bg_rect.get_height() / 5

    music_timer = time.time()
    start_music = True
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(join('Salvataggio','achievement_riscattato.txt'), 'w') as save_file:
                    json.dump(data, save_file)
                return False, coins
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos) and not rule_check: running = False 
                    elif exit_rect.collidepoint(event.pos) and rule_check: rule_check = False
                    
                    if info_rect.collidepoint(event.pos):
                        rule_check = True

                    if not rule_check and not exit_rect.collidepoint(event.pos):
                        button1_active = button2_active = button3_active = button4_active = button5_active = False
                        
                        button1_active = button1.check_click()
                        button2_active = button2.check_click()
                        button3_active = button3.check_click()
                        button4_active = button4.check_click()
                        button5_active = button5.check_click()
                        
                        if button1_active and a >= 3 and not data['reward_1']: coins += 175; data['reward_1'] = True; achievement_done_sound.play()
                        elif button2_active and b >= 3 and not data['reward_2']: coins += 150; data['reward_2'] = True; achievement_done_sound.play()
                        elif button3_active and c >= 3 and not data['reward_3']: coins += 150; data['reward_3'] = True; achievement_done_sound.play()
                        elif button4_active and d >= 3 and not data['reward_4']: coins += 200; data['reward_4'] = True; achievement_done_sound.play()
                        elif button5_active and e >= 3 and not data['reward_5']: coins += 150; data['reward_5'] = True; achievement_done_sound.play()
                        else: not_unlocked_sound.play()

        screen.fill('light blue')

        screen.blit(title, title_rect)
        screen.blit(bg_rect, (0, 100))
        
        screen.blit(info_surf,info_rect)
        
        pygame.draw.line(screen,'black',(500,100),(500,600),5)
        pygame.draw.rect(screen,'black',(0,100,WIDTH,500),5,border_radius=12)
        
        for surf in surfaces:
            screen.blit(surf,(20,num + 110))
            num += bg_rect.get_height() / 5
            
        num = bg_rect.get_height() / 5
        
        for progress in progress_surf:
            screen.blit(progress,(20,num + 50))
            num += bg_rect.get_height() / 5
            
        for button in buttons:
            if not rule_check:
                button.draw()
                
        end_timer = time.time() - music_timer
        
        if end_timer >= 0.5 and start_music:
            bg_sounds[5].play(loops=-1)
            start_music = False
            
        num = 0
        
        if rule_check:
            screen.blit(tint_surf,(0,0))
            pygame.draw.rect(screen,'light blue',rules_rect,border_radius=12)
            screen.blit(rule_title,rule_title_rect)
            for index, rule in enumerate(rules):
                rule_text = test_font.render(rule,False,'black')
                screen.blit(rule_text,(150,((rules_rect.width / 5 - 40) * index + 160)))
                pygame.draw.circle(screen,'black',(125,((rules_rect.width / 5 - 40) * index + 170)),5)
            
        screen.blit(exit_surface,exit_rect)

        pygame.display.update()
    
    
    bg_sounds[5].fadeout(500)
    with open(join('Salvataggio','achievement_riscattato.txt'), 'w') as save_file:
        json.dump(data, save_file)
        
    return True, coins

