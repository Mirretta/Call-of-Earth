import pygame, sys, time
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

test_rect = pygame.FRect(0,310,100,100)
test_speed = 200

previous_time = time.time()
running = True
while running:
    dt = clock.tick() / 1000
    # dt = time.time() - previous_time
    # previous_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    screen.fill('white')
    
    test_rect.x += test_speed * dt
    pygame.draw.rect(screen,'red',test_rect)
            
    debug(dt)
    pygame.display.update()
    
pygame.quit()
sys.exit()