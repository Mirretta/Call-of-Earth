import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
base_font = pygame.font.Font(None,32)
user_text = ''

input_rect = pygame.FRect(200,200,140,32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('gray15')
color = color_passive

active = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        
    screen.fill((0,0,0))
    
    if active: color = color_active
    else: color = color_passive
    
    pygame.draw.rect(screen,color,input_rect,2)
    
    text_surf = base_font.render(user_text,True,(255,255,255))
    screen.blit(text_surf,(input_rect.x + 5,input_rect.y + 5))
    
    input_rect.w = max(140,text_surf.get_width() + 10)
    
    pygame.display.update()
    clock.tick(60)   
    
pygame.quit()
sys.exit()