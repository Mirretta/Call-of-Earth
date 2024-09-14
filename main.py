import json
from settings import *
import ProvaBasket
import invasione_spazzatura
import invasione_spazzatura_parte_2
import auto_gioco
import eco_quiz
import introduzione
import achievements
import negozio
import statistiche

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SRCALPHA)
pygame.display.set_caption('Call of Earth')
score = game = current_best_score = 0
running = False
player_name = None

data = {}
try:
    with open(join('Salvataggio','saved_progress.txt')) as save_file:
        data = json.load(save_file)
except:
    data = {
        'best_score_1': 0,
        'best_score_2': 0,
        'best_score_3': 0,
        'best_score_4': 0,
        'best_score_5': 0,
        'basket_shots' : 0,
        'spazzatura_raccolta' : 0,
        'punteggio_perf' : 0,
        'spazzatura_distrutta' : 0,
        'name': None,
        'risp_giuste' : [],
        'test_fatti' : 0,
        'victory_counter' : 0,
        'coins' : 0,
        'skin' : 'julius',
        'macchina' : 'macchina_verde.png',
        'tempo_passato' : 0,
    }
    
player_name = data['name']

# suoni
high_score_sound = pygame.mixer.Sound(join('Audio','Punteggio','high_score.wav'))
bg_music = pygame.mixer.Sound(join('Audio','Sottofondo','menu_music.mp3'))
bg_music.play(loops=-1)

main_background = pygame.image.load(join('Grafiche','Background','background_principale.png')).convert()
moneta = pygame.image.load(join('Grafiche','Altro','moneta.png')).convert_alpha()
moneta_rect = moneta.get_frect(topleft=(730,10))
achivement_surf = pygame.image.load(join('Grafiche','Altro','trofeo.png')).convert_alpha()
achivement_rect = achivement_surf.get_frect(topleft=(30,20))
negozio_surf = pygame.image.load(join('Grafiche','Altro','shop_icon.png')).convert_alpha()
negozio_rect = negozio_surf.get_frect(topleft=(1,85))
titolo = pygame.image.load(join('Grafiche','Altro','titolo_2.png')).convert_alpha()
titolo_rect = titolo.get_frect(center = (370,100))
stat_icon = pygame.image.load(join('Grafiche','Altro','stat_icon.png')).convert_alpha()

minigame1_surface = test_font.render('Basket eco', False, 'black')
minigame2_surface = test_font.render('Cadono rifiuti!', False, 'black')
minigame3_surface = test_font.render('Invasione di spazzatura!', False, 'black')
minigame4_surface = test_font.render('Giustizia eco', False, 'black')
minigame5_surface = test_font.render('Quiz eco', False, 'black')

minigame1_score_surface = test_font.render(f'Best score: {data['best_score_1']}', False, 'black')
minigame2_score_surface = test_font.render(f'Best score: {data['best_score_2']}', False, 'black')
minigame3_score_surface = test_font.render(f'Best score: {data['best_score_3']}', False, 'black')
minigame4_score_surface = test_font.render(f'Best score: {data['best_score_4']}', False, 'black')
minigame5_score_surface = test_font.render(f'Best score: {data['best_score_5']}', False, 'black')

coordinate_surf = [(135, 230),(505, 230),(260, 330),(125, 430),(550, 430)]
coordinate_rect = [(117, 258),(500, 258),(330, 358),(117, 458),(517, 458)]

bg_rect1 = pygame.FRect(min(coordinate_surf[0][0],coordinate_rect[0][0])-10,min(coordinate_surf[0][1],coordinate_rect[0][1])-10,max(minigame1_surface.get_width(),minigame1_score_surface.get_width()) + 20,minigame1_surface.get_height() + minigame1_score_surface.get_height() + 20)
bg_rect2 = pygame.FRect(min(coordinate_surf[1][0],coordinate_rect[1][0])-10,min(coordinate_surf[1][1],coordinate_rect[1][1])-10,max(minigame2_surface.get_width(),minigame2_score_surface.get_width()) + 20,minigame2_surface.get_height() + minigame2_score_surface.get_height() + 20)
bg_rect3 = pygame.FRect(min(coordinate_surf[2][0],coordinate_rect[2][0])-10,min(coordinate_surf[2][1],coordinate_rect[2][1])-10,max(minigame3_surface.get_width(),minigame3_score_surface.get_width()) + 20,minigame3_surface.get_height() + minigame3_score_surface.get_height() + 20)
bg_rect4 = pygame.FRect(min(coordinate_surf[3][0],coordinate_rect[3][0])-10,min(coordinate_surf[3][1],coordinate_rect[3][1])-10,max(minigame4_surface.get_width(),minigame4_score_surface.get_width()) + 20,minigame4_surface.get_height() + minigame4_score_surface.get_height() + 20)
bg_rect5 = pygame.FRect(min(coordinate_surf[4][0],coordinate_rect[4][0])-10,min(coordinate_surf[4][1],coordinate_rect[4][1])-10,max(minigame5_surface.get_width(),minigame5_score_surface.get_width()) + 20,minigame5_surface.get_height() + minigame5_score_surface.get_height() + 20)

surfaces_name = [minigame1_surface,minigame2_surface,minigame3_surface,minigame4_surface,minigame5_surface]
rects = [bg_rect1,bg_rect2,bg_rect3,bg_rect4,bg_rect5]

victory = 0

current_game = None

previous_time = time.time()
start_time = pygame.time.get_ticks()

if __name__ == '__main__':
    running = True

while running:
    dt = previous_time - time.time()
    previous_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bg_rect1.collidepoint(event.pos):
                    current_game = ProvaBasket
                    game = 1
                if bg_rect2.collidepoint(event.pos):
                    current_game = invasione_spazzatura
                    game = 2
                if bg_rect3.collidepoint(event.pos):
                    current_game = invasione_spazzatura_parte_2
                    game = 3
                if bg_rect4.collidepoint(event.pos):
                    current_game = auto_gioco 
                    game = 4
                if bg_rect5.collidepoint(event.pos):
                    current_game = eco_quiz
                    game = 5
                if achievement_circle.collidepoint(event.pos): current_game = achievements
                if shpop_cirlce.collidepoint(event.pos): current_game = negozio
                if stats_cirlce.collidepoint(event.pos): current_game = statistiche

    if not player_name:
        player_name = introduzione.run()
        data['name'] = player_name
    
    passed_time = ((pygame.time.get_ticks() - start_time) / 1000) / 60
    
    surfaces_score = [minigame1_score_surface,minigame2_score_surface,minigame3_score_surface,minigame4_score_surface,minigame5_score_surface]
    
    screen.blit(main_background,(0, 0))
    screen.blit(titolo,titolo_rect)
    achievement_circle = pygame.draw.circle(screen,(173,216,230),achivement_rect.center,achivement_surf.get_width())
    pygame.draw.circle(screen,'black',achivement_rect.center,achivement_surf.get_width(),5)
    shpop_cirlce = pygame.draw.circle(screen,'light blue',negozio_rect.center,achivement_surf.get_width())
    pygame.draw.circle(screen,'black',negozio_rect.center,achivement_rect.width,5)
    stats_cirlce = pygame.draw.circle(screen,'light blue',negozio_rect.center - Vector2(0,-95),achivement_surf.get_width())
    pygame.draw.circle(screen,'black',negozio_rect.center - Vector2(0,-95),achivement_rect.width,5)
    screen.blit(achivement_surf,achivement_rect)
    screen.blit(negozio_surf,negozio_rect)
    stat_rect = stat_icon.get_frect(center = stats_cirlce.center)
    screen.blit(stat_icon,stat_rect)
    
    screen.blit(moneta,moneta_rect)
    coin_surf = test_font.render(f'{data['coins']}',False,'black')
    coin_rect = pygame.draw.rect(screen,'light blue',(moneta_rect.left - coin_surf.get_width() - 30,20,coin_surf.get_width() + 20,coin_surf.get_height() + 10),border_radius=12)
    screen.blit(coin_surf,(coin_rect.left+ 10, 30))
    
    for num in range(5):
        pygame.draw.rect(screen,(173,216,230),rects[num],border_radius=12)
        screen.blit(surfaces_name[num],coordinate_surf[num])
        screen.blit(surfaces_score[num],coordinate_rect[num])
    
    if current_game:
        bg_music.fadeout(500)
        if current_game == achievements: running, data['coins'] = current_game.run(data['basket_shots'],data['spazzatura_raccolta'],data['punteggio_perf'],data['victory_counter'],len(data['risp_giuste']),data['coins'])
        elif current_game == invasione_spazzatura_parte_2: running, score, data['punteggio_perf'] = current_game.run()
        elif current_game == eco_quiz: running, score, data['risp_giuste'] = current_game.run(data['risp_giuste'])
        elif current_game == auto_gioco: running, score, victory = current_game.run(data['macchina'])
        elif current_game == negozio: running, data['skin'], data['macchina'], data['coins'] = current_game.run(data['coins'], data['skin'], data['macchina'])
        elif current_game == invasione_spazzatura or current_game == ProvaBasket: running, score = current_game.run(data['skin'])
        else: running, data['tempo_passato'] = current_game.run(data['name'],data['skin'],data['basket_shots'],data['spazzatura_raccolta'],data['spazzatura_distrutta'],data['victory_counter'],data['test_fatti'],data['tempo_passato'],passed_time); start_time = pygame.time.get_ticks()
        bg_music.play(loops=-1)

    if game == 1:
        current_best_score = data['best_score_1']
        data['best_score_1'] = max(score, data['best_score_1'])
        minigame1_score_surface = test_font.render(f'Best score: {data['best_score_1']}', False, 'black')
        data['basket_shots'] += score
        data['coins'] += score 
    elif game == 2:
        current_best_score = data['best_score_2']
        data['best_score_2'] = max(score, data['best_score_2'])
        minigame2_score_surface = test_font.render(f'Best score: {data['best_score_2']}', False, 'black')
        data['spazzatura_raccolta'] += score
        data['coins'] += score // 2
    elif game == 3:
        current_best_score = data['best_score_3']
        data['best_score_3'] = max(score, data['best_score_3'])
        data['spazzatura_distrutta'] += score
        minigame3_score_surface = test_font.render(f'Best score: {data['best_score_3']}', False, 'black')
        data['coins'] += score 
    elif game == 4:
        current_best_score = data['best_score_4']
        data['best_score_4'] = max(score, data['best_score_4'])
        minigame4_score_surface = test_font.render(f'Best score: {data['best_score_4']}', False, 'black')
        data['victory_counter'] += victory
        if victory >= 1:
            data['coins'] += 50
        data['coins'] += score // 2
    elif game == 5:
        current_best_score = data['best_score_5']
        data['best_score_5'] = max(score, data['best_score_5'])
        minigame5_score_surface = test_font.render(f'Best score: {data['best_score_5']}', False, 'black')
        data['coins'] += score * 3
        data['test_fatti'] += 1
        
    if score > current_best_score:
        high_score_sound.play()   
    
    current_game = None
    score = game = victory = current_best_score = 0
   
    for index, rect in enumerate(rects):
        rect.width = max(surfaces_score[index].get_width(), surfaces_name[index].get_width()) + 20
    
    pygame.display.update()

data['tempo_passato'] += passed_time
with open(join('Salvataggio','saved_progress.txt'), 'w') as save_file:
    json.dump(data, save_file)
pygame.quit()
sys.exit()
