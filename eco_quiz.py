from settings import *
from classi import Button
from pygame.math import Vector2

pygame.init()

domande = {
    'Qual e\' il principale gas responsabile \ndell\'effetto serra?': 3, 'Qual e\' l\'organo delle piante \nresponsabile della fotosintesi?': 2, 'Qual e\' il processo attraverso cui \ngli organismi decompongono \nla materia organica?': 3, 'Qual e\' una causa dell\'acidificazione \ndegli oceani?': 4, 'Qual e\' una fonte rinnovabile \ndi energia?': 3,
    'Qual e\' un esempio di \necosistema marino?': 3, 'Qual e\' un effetto \ndell\'inquinamento luminoso?': 2, 'Qual e\' un metodo per \nconservare la biodiversita\'?': 3, 'Qual e\' un esempio di energia \nnon rinnovabile?': 3, 'Qual e\' un esempio di inquinamento \ndell\'aria?': 1,
    'Qual e\' un fattore che contribuisce \nalla perdita di habitat?': 2, 'Qual e\' un effetto del surriscaldamento \nglobale sugli oceani?': 2, 'Qual e\' un metodo per ridurre \nl\'impronta ecologica?': 2, 'Qual e\' un esempio di \nspecie invasive?': 4, 'Qual e\' un beneficio \ndell\'agricoltura biologica?': 2,
    'Qual e\' una causa dell\'erosione \ndel suolo?': 1, 'Qual e\' un effetto dell\'inquinamento \ndei fiumi?': 3, 'Qual e\' un vantaggio dell\'energia \nsolare?': 3, 'Qual e\' un modo per ridurre \nla produzione di rifiuti?': 2, 'Qual e\' un impatto dell\'inquinamento \nidrico?': 3,
}

opzioni = [
    ['Ossigeno', 'Azoto', 'Anidride Carbonica', 'Idrogeno'], ['Radici', 'Foglie', 'Fiori', 'Steli'], ['Fotosintesi', 'Fermentazione', 'Decomposizione', 'Respirazione'], ['Aumento del pH', 'Diminuzione \nemissioni CO2', 'Assorbimento \ndi CO2', 'Scarichi industriali'], ['Petrolio', 'Carbone', 'Vento', 'Gas naturale'],
    ['Deserto', 'Prateria', 'Barriera \ncorallina', 'Foresta \npluviale'], ['Riduzione dell\' \ninquinamento \ndell\'aria', 'Disturbo degli \nanimali notturni', 'Aumento della \nbiodiversita\'', 'Miglioramento della \nvista notturna umana'], ['Deforestazione', 'Urbanizzazione', 'Creazione \ndi aree protette', 'Estrazione \nmineraria intensiva'], ['Energia solare', ' Energia eolica', 'Petrolio', 'Biomassa'], ['Smog', 'Acidificazione \ndegli oceani', 'Inquinamento luminoso', 'Inquinamento acustico'],
    ['Conservazione \ndelle risorse', 'Urbanizzazione', 'Rimboschimento', 'Riduzione \ndell\'inquinamento'], ['Aumento della salinita\'', 'Aumento della T \ndell\'acqua', 'Diminuzione dell\'acidita\'', 'Riduzione del livello \ndegli oceani'], ['Aumentare il consumo \ndi risorse', 'Ridurre il consumo \ndi energia', 'Aumentare lo spreco \nalimentare', 'Aumentare l\'uso \ndi plastica monouso'], ['Piante locali', 'Animali migratori', 'Specie native', 'Cane di prateria'], ['Utilizzo intensivo \ndi pesticidi', 'Minore impatto \nambientale', 'Aumento dell\' \ninquinamento \ndel suolo', 'Riduzione della \nbiodiversita\''],
    ['Deforestazione', 'Afforestation', 'Ricerca di nuove specie', 'Riciclaggio'], ['Aumento della \nbiodiversita\' acquatica', 'Riduzione della \ntossicita\' dell\'acqua', 'Moria di pesci', 'Miglioramento della \nqualita\' dell\'acqua'], ['Produzione di emissioni \nnocive', 'Costi elevati \ndi installazione', 'Riduzione dell\' \ninquinamento \natmosferico', 'Dipendenza da \ncombustibili fossili'], ['Utilizzare piu\' imballaggi \nmonouso', 'Praticare il \ncompostaggio', 'Aumentare l\'uso \ndi plastica', 'Sprecare cibo'], ['Aumento della \nbiodiversita\' acquatica', 'Riduzione della \ntossicita\' dell\'acqua', 'Morte di organismi \nacquatici', 'Aumento della qualita\' \ndell\'acqua']
]


def run(risp_giuste):
    global score

    screen = pygame.display.get_surface()
    start_game = False
    score_surface = test_font.render(f'Score: {score}', False, 'black')
    score_rect = score_surface.get_frect(center=(100, 100))
    grade_surf = pygame.image.load(join('Grafiche','Altro','thumbs_up.png')).convert_alpha()
    grade_rect = grade_surf.get_frect(center=(615, 100))
    score = 0

    answer_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(answer_timer, 10000)
    
    # sounds
    correct_sound = pygame.mixer.Sound(join('Audio','Punteggio','correct_ans.wav'))
    wrong_sound = pygame.mixer.Sound(join('Audio','Punteggio','wrong_ans.wav'))
    wrong_sound.set_volume(20)
    bg_sounds[4].set_volume(1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                risp_giuste = set(risp_giuste)
                risp_giuste = list(risp_giuste)
                return False, 0, risp_giuste
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if exit_rect.collidepoint(event.pos):
                        running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start_game:
                    start_game = True
                    bg_sounds[4].play(loops=-1)
                    value = num = score = num7 = score = start_time = passed_time = 0
                    score_surface = test_font.render(f'Score: {score}', False, 'black')

                    num1 = randint(0, 19)
                    num2 = randint(0, 19)
                    while num2 == num1:
                        num2 = randint(0, 19)
                    num3 = randint(0, 19)
                    while num3 == num1 or num3 == num2:
                        num3 = randint(0, 19)
                    num4 = randint(0, 19)
                    while num4 == num1 or num4 == num2 or num4 == num3:
                        num4 = randint(0, 19)
                    num5 = randint(0, 19)
                    while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                        num5 = randint(0, 19)

                    num1_diff = num2 - num1
                    num2_diff = num3 - num2
                    num3_diff = num4 - num3
                    num4_diff = num5 - num4

                    numeri = [num1_diff, num2_diff, num3_diff, num4_diff]

                    num1_key = list(domande.keys())[num1 - 1]
                    num1_value = domande[num1_key]
                    num2_key = list(domande.keys())[num2 - 1]
                    num2_value = domande[num2_key]
                    num3_key = list(domande.keys())[num3 - 1]
                    num3_value = domande[num3_key]
                    num4_key = list(domande.keys())[num4 - 1]
                    num4_value = domande[num4_key]
                    num5_key = list(domande.keys())[num5 - 1]
                    num5_value = domande[num5_key]
                    domande2 = [num1_key, num2_key, num3_key, num4_key, num5_key]
                    risp_corrette = [num1_value,num2_value,num3_value,num4_value,num5_value,]

                    num6 = num1

                    question_surface = test_font.render(domande2[num], False, 'black')
                    button1 = Button(opzioni[num1 - 1][0],300,150,(50,180),6)
                    question_rect = question_surface.get_frect(topleft=(button1.top_rect.left + 25, 60))
                    button2 = Button(opzioni[num1 - 1][1],300,150,(450,180),6)
                    button3 = Button(opzioni[num1 - 1][2],300,150,(50,370),6)
                    button4 = Button(opzioni[num1 - 1][3],300,150,(450,370),6)
                    buttons = [button1,button2,button3,button4]
                    
                    grade_surface = None

            if start_game:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        value = 0
                        
                        button1_active = button2_active = button3_active = button4_active = False
                        
                        button1_active = button1.check_click()
                        button2_active = button2.check_click()
                        button3_active = button3.check_click()
                        button4_active = button4.check_click()
                        
                        if button1_active: value = 1
                        if button2_active: value = 2
                        if button3_active: value = 3
                        if button4_active: value = 4
                        
                        
                        if value == risp_corrette[num]:
                            grade_surface = grade_surf
                            score += 1
                            risp_giuste.append(domande2[num])
                            correct_sound.play()
                        elif value != risp_corrette[num] and value != 0:
                            grade_surface = pygame.transform.flip(grade_surf,False,True)
                            wrong_sound.play()
                            
                        if value != 0:
                            pygame.time.set_timer(answer_timer, 10000)
                            start_time = pygame.time.get_ticks()

                if event.type == answer_timer or value != 0:
                    value = 0
                    if num <= 3:
                        num6 += numeri[num]
                    if num != 4:
                        num += 1
                    num7 += 1
                    question_surface = test_font.render(domande2[num], False, 'black')
                    button1 = Button(opzioni[num6 - 1][0],300,150,(50,180),6)
                    question_rect = question_surface.get_frect(topleft=(button1.top_rect.left + 25, 60))
                    button2 = Button(opzioni[num6 - 1][1],300,150,(450,180),6)
                    button3 = Button(opzioni[num6 - 1][2],300,150,(50,370),6)
                    button4 = Button(opzioni[num6 - 1][3],300,150,(450,370),6)
                    buttons = [button1,button2,button3,button4]

        screen.fill('light blue')

        if start_game:
            
            for button in buttons:
                button.draw()
                
            pygame.draw.rect(screen,'light gray',((question_rect.topleft + Vector2(-20,-20)),(question_rect.width + 40, question_rect.height + 40)))
                
            screen.blit(question_surface, question_rect)
            if num7 >= 5:
                start_game = False
                
            if start_time != 0:
                passed_time = (pygame.time.get_ticks() - start_time) / 1000
                
            if passed_time < 0.75 and grade_surface:
                screen.blit(grade_surface, grade_rect)
                

        else:
            introduction_surface = test_font2.render('Quanto ne sai?', False, 'black')
            introduction_rect = introduction_surface.get_frect(center=(400, 300))
            screen.blit(exit_surface, exit_rect)
            screen.blit(introduction_surface, introduction_rect)
            bg_sounds[4].fadeout(750)
            if score > 0:
                score_text = test_font4.render(f'Punteggio: {score}',False,'black')
                score_rect = score_text.get_frect(center=(400,100))
                screen.blit(score_text,score_rect)
            grade_surface = None
            screen.blit(instruction_surf,instruction_rect)

        pygame.display.update()
        clock.tick(FPS)
        
    risp_giuste = set(risp_giuste)
    risp_giuste = list(risp_giuste)

    return True, score, risp_giuste
