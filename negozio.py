from settings import *
from pygame.math import Vector2
import json
from classi import Button

def run(coins, skin, car):
    
    data = {}
    
    try:
        with open(join('Salvataggio','negozio.txt')) as shop_file:
            data = json.load(shop_file)
    except:
        data = {
            'bought_1' : False,
            'bought_2' : False,
            'bought_3' : False,
            'bought_4' : False,
            'bought_5' : False,
            'bought_6' : False,
            'color_1' : 'white',
            'color_2' : (57, 69, 110),
            'color_3' : (57, 69, 110),
            'color_4' : (57, 69, 110),
            'color_5' : 'white',
            'color_6' : (57, 69, 110),
            'color_7' : (57, 69, 110),
            'color_8' : (57, 69, 110), 
        }
    screen = pygame.display.get_surface()
    
    # imports
    kobe = pygame.image.load(join('Grafiche','Player','Kobe','kobe_stand.png')).convert_alpha()
    lebron = pygame.image.load(join('Grafiche','Player','Lebron','lebron_stand.png')).convert_alpha()
    jordan = pygame.image.load(join('Grafiche','Player','Jordan','jordan_stand.png')).convert_alpha()
    julius = pygame.image.load(join('Grafiche','Player','Julius','julius_stand.png')).convert_alpha()
    green_car = pygame.image.load(join('Grafiche','Macchine','macchina_verde.png')).convert_alpha()
    light_blue_car = pygame.image.load(join('Grafiche','Macchine','macchina_azzurra.png')).convert_alpha()
    red_car = pygame.image.load(join('Grafiche','Macchine','macchina_rossa.png')).convert_alpha()
    ferrari = pygame.image.load(join('Grafiche','Macchine','ferrari.png')).convert_alpha()
    ferrari = pygame.transform.scale(ferrari,(80,80))
    lock = pygame.image.load(join('Grafiche','Altro','closed_lock.png'))
    lock_2 = pygame.transform.scale(lock,(90,100))
    moneta = pygame.image.load(join('Grafiche','Altro','moneta.png')).convert_alpha()
    moneta_rect = moneta.get_frect(topleft=(20,30))
    
    coin_text = test_font.render(f'{coins}',False,'black')
    
    green_car = pygame.transform.rotozoom(green_car,90,1)
    red_car = pygame.transform.rotozoom(red_car,90,1)
    light_blue_car = pygame.transform.rotozoom(light_blue_car,90,1)
    ferrari = pygame.transform.rotozoom(ferrari,90,1)
    
    players = [julius,kobe,lebron,jordan,green_car,light_blue_car,red_car,ferrari]
    
    julius_rect = pygame.FRect(WIDTH / 4 - 170,160,julius.get_width() + 15,julius.get_height() + 30)
    kobe_rect = pygame.FRect(WIDTH / 4 * 2 - 170,160,kobe.get_width() + 15,kobe.get_height() + 30)
    lebron_rect = pygame.FRect(WIDTH / 4 * 3 - 170,160,lebron.get_width() + 15,lebron.get_height() + 30)
    jordan_rect = pygame.FRect(WIDTH / 4 * 4 - 170,160,jordan.get_width() + 15,jordan.get_height() + 30)
    
    outline_rect_1 = pygame.FRect(WIDTH / 4 - 170,160,julius.get_width() + 15,julius.get_height() + 30)
    outline_rect_2 = pygame.FRect(WIDTH / 4 * 2 - 170,160,kobe.get_width() + 15,kobe.get_height() + 30)
    outline_rect_3 = pygame.FRect(WIDTH / 4 * 3 - 170,160,lebron.get_width() + 15,lebron.get_height() + 30)
    outline_rect_4 = pygame.FRect(WIDTH / 4 * 4 - 170,160,jordan.get_width() + 15,jordan.get_height() + 30)
    
    green_car_rect = pygame.FRect(WIDTH / 4 - 160,425,green_car.get_width() + 20, green_car.get_height() + 40)
    light_blue_car_rect = pygame.FRect(WIDTH / 4 * 2 - 160,425,light_blue_car.get_width() + 20, light_blue_car.get_height() + 40)
    red_car_rect = pygame.FRect(WIDTH / 4 * 3- 160,425,red_car.get_width() + 20, red_car.get_height() + 40)
    ferrari_rect = pygame.FRect(WIDTH / 4 * 4- 160,425,ferrari.get_width() + 20, ferrari.get_height() + 40)
    
    outline_car_1 = pygame.FRect(WIDTH / 4 - 160,425,green_car.get_width() + 20, green_car.get_height() + 40)
    outline_car_2 = pygame.FRect(WIDTH / 4 * 2 - 160,425,light_blue_car.get_width() + 20, light_blue_car.get_height() + 40)
    outline_car_3 = pygame.FRect(WIDTH / 4 * 3- 160,425,red_car.get_width() + 20, red_car.get_height() + 40)
    outline_car_4 = pygame.FRect(WIDTH / 4 * 4- 160,425,ferrari.get_width() + 20, ferrari.get_height() + 40)
    
    title_rect = pygame.FRect(0,0,WIDTH,100)
    
    text_surf = test_font2.render('Negozio',False,'black')
    
    names = ['Julius','Kobe Bryant','Lebron James','Michael Jordan','Verde','Azzurra','Rossa','Ferrari']
    colors = [data['color_1'],data['color_2'],data['color_3'],data['color_4'],data['color_5'],data['color_6'],data['color_7'],data['color_8']]
    rects = [julius_rect,kobe_rect,lebron_rect,jordan_rect,green_car_rect,light_blue_car_rect,red_car_rect,ferrari_rect]
    prezzi_rects = [(kobe_rect,kobe),(lebron_rect,lebron),(jordan_rect,jordan),(light_blue_car_rect,light_blue_car),(red_car_rect,red_car),(ferrari_rect,ferrari)]
    outline_rects = [outline_rect_1,outline_rect_2,outline_rect_3,outline_rect_4,outline_car_1,outline_car_2,outline_car_3,outline_car_4]
    prezzi = ['750','750','750','350','350','500']
    buy_rect = []
    buying = False
    
    buy_sound = pygame.mixer.Sound(join('Audio','Negozio','buy.wav'))
    locked_item_sound = pygame.mixer.Sound(join('Audio','Negozio','locked_item.wav'))
    
    bg_surf = pygame.Surface((WIDTH,HEIGHT))
    bg_surf.set_alpha(200)
    
    confirm_surf = test_font2.render('Confermi?',False,'black')
    not_enough = False
    not_enough_text = test_font4.render('Non hai abbatanza monete!',False,'black')
    button1 = Button('Si',225,100,(150,220),6)
    button2 = Button('No',225,100,(425,220),6)
    
    music_timer = time.time()
    start_music = True
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(join('Salvataggio','negozio.txt'), 'w') as shop_file:
                    json.dump(data, shop_file)
                return False, skin, car, coins
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos) and not buying:
                        running = False
                    if not buying:
                        if julius_rect.collidepoint(event.pos):
                            data['color_2'] = data['color_3'] = data['color_4'] = (57, 69, 110)
                            data['color_1'] = 'white'
                            skin = 'julius'
                        if kobe_rect.collidepoint(event.pos) and data['bought_1']:
                            data['color_1'] = data['color_3'] = data['color_4'] = (57, 69, 110)
                            data['color_2'] = 'white'
                            skin = 'kobe'
                        if lebron_rect.collidepoint(event.pos) and data['bought_2']:
                            data['color_1'] = data['color_2'] = data['color_4'] = (57, 69, 110)
                            data['color_3'] = 'white'
                            skin = 'lebron'
                        if jordan_rect.collidepoint(event.pos) and data['bought_3']:
                            data['color_1'] = data['color_2'] = data['color_3'] = (57, 69, 110)
                            data['color_4'] = 'white'
                            skin = 'jordan'
                        if green_car_rect.collidepoint(event.pos):
                            data['color_6'] = data['color_7'] = data['color_8'] = (57, 69, 110)
                            data['color_5'] = 'white'
                            car = 'macchina_verde.png'
                        if light_blue_car_rect.collidepoint(event.pos) and data['bought_4']:
                            data['color_5'] = data['color_7'] = data['color_8'] =(57, 69, 110)
                            data['color_6'] = 'white'
                            car = 'macchina_azzurra.png'
                        if red_car_rect.collidepoint(event.pos) and data['bought_5']:
                            data['color_5'] = data['color_6'] = data['color_8'] = (57, 69,110)
                            data['color_7'] = 'white'
                            car = 'macchina_rossa.png'
                        if ferrari_rect.collidepoint(event.pos) and data['bought_6']:
                            data['color_5'] = data['color_6'] = data['color_7'] = (57, 69,110)
                            data['color_8'] = 'white'
                            car = 'ferrari.png'
                            
                        if buy_rect[0].collidepoint(event.pos) and not data['bought_1']:
                            buying = True
                            selected_skin = 1
                        if buy_rect[1].collidepoint(event.pos) and not data['bought_2']:
                            buying = True
                            selected_skin = 2
                        if buy_rect[2].collidepoint(event.pos) and not data['bought_3']:
                            buying = True
                            selected_skin = 3
                        if buy_rect[3].collidepoint(event.pos) and not data['bought_4']:
                            buying = True
                            selected_skin = 4
                        if buy_rect[4].collidepoint(event.pos) and not data['bought_5']:
                            buying = True
                            selected_skin = 5
                        if buy_rect[5].collidepoint(event.pos) and not data['bought_6']:
                            buying = True
                            selected_skin = 6
                            
                    if buying:
                        button1_active, button2_active = button1.check_click(), button2.check_click()
                        
                        if button1_active:
                            if coins >= int(prezzi[selected_skin - 1]):
                                coins -= int(prezzi[selected_skin - 1])
                                data[f'bought_{selected_skin}'] = True
                                buy_sound.play()
                                buying = False
                                coin_text = test_font.render(f'{coins}',False,'black')
                            else:
                                not_enough = True
                                locked_item_sound.play()
                        if button2_active:
                                buying = False
                                not_enough = False
                            
                    colors = [data['color_1'],data['color_2'],data['color_3'],data['color_4'],data['color_5'],data['color_6'],data['color_7'],data['color_8']]
                
        screen.fill((209, 227, 237))    
        
        pygame.draw.rect(screen,(59, 116, 140),title_rect)
        pygame.draw.line(screen,'white',(0,370),(800,370),5)
        screen.blit(text_surf,(300,30))
        
        screen.blit(moneta,moneta_rect)
        screen.blit(coin_text,(moneta_rect.right + 10,45))
        
        for rect in rects:
            pygame.draw.rect(screen,(57, 69, 110),rect,border_radius=12)
        
        for index, outline_rect in enumerate(outline_rects):
            pygame.draw.rect(screen,colors[index],outline_rect,5,border_radius=12)
        
        for index, player in enumerate(players):
            player_rect = player.get_frect(center = rects[index].center)
            screen.blit(player,player_rect)
        
        for i in range(len(players) - 2):
            if not data[f'bought_{i + 1}']:
                prezzi_rects[i][1].set_alpha(100)
                if i <= 2:
                    screen.blit(lock,prezzi_rects[i][0].topleft + Vector2(16,15))
                else:
                    screen.blit(lock_2,prezzi_rects[i][0].topleft + Vector2(5,5))
            else:
                prezzi_rects[i][1].set_alpha(255)
            text = test_font5.render('Compra',False,'black')
            text_rect = text.get_frect(center = (prezzi_rects[i][0].centerx, prezzi_rects[i][0].bottom + 30))
            e = i
            e = pygame.FRect(((text_rect.topleft + Vector2(-5,-5)),(text_rect.width + 10, text_rect.height + 10)))
            buy_rect.append(e)
            if not data[f'bought_{i + 1}']:
                pygame.draw.rect(screen,'light gray',e,border_radius=12)
                screen.blit(text,text_rect)
        
        for index, name in enumerate(names):
            name_surf = test_font.render(name,False,'black')
            if index <= 3:
                name_rect = name_surf.get_frect(center = (rects[index].center + Vector2(0,-100)))
            else:
                name_rect = name_surf.get_frect(center = (rects[index].center + Vector2(0,-85)))
            pygame.draw.rect(screen,'gray',((name_rect.topleft) + Vector2(-6,-6),(name_rect.width + 10,name_rect.height + 8)),border_radius=12)
            screen.blit(name_surf,name_rect)
                
        screen.blit(exit_surface,exit_rect)
        
        if buying:
            screen.blit(bg_surf,(0,0))
            rect_confirm = pygame.draw.rect(screen,'light blue',(100,100,600,320),border_radius=12)
            screen.blit(confirm_surf,(270,120))
            button1.draw()
            button2.draw()
            if not_enough:
                screen.blit(not_enough_text,(rect_confirm.centerx - not_enough_text.get_width() / 2,350))
            else:
                cost_text = test_font4.render(f'Costo: {prezzi[selected_skin - 1]}',False,'black')
                screen.blit(cost_text,(rect_confirm.centerx - cost_text.get_width() / 2,350))
                
        end_timer = time.time() - music_timer
        
        if end_timer >= 0.5 and start_music:
            bg_sounds[5].play(loops=-1)
            start_music = False
                         
        pygame.display.update()
     
    bg_sounds[5].fadeout(500)  
    with open(join('Salvataggio','negozio.txt'), 'w') as shop_file:
        json.dump(data, shop_file)
        
    return True, skin, car, coins