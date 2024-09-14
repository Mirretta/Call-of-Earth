from settings import *
from math import sqrt
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, type, y, minigioco,player_frames = None,player_stand = None):
        super().__init__()
        self.gioco = minigioco
        self.value = type
        self.momentum = 200
        self.player_index = 0
        if type == 1:
            self.player_stand = player_stand
            self.image = player_stand
            self.frames = player_frames
            self.rect = self.image.get_frect(midbottom=(400, 500))
        if type == 3:
            self.image = pygame.image.load('Grafiche/Player/giocatore_cestino.png').convert_alpha()
            self.rect = self.image.get_frect(center=(400, 525))
        if type == 2:
            self.image = pygame.image.load('Grafiche/Player/cestino.png')
            self.rect = self.image.get_frect(midbottom=(370, 480))

        if type == 4:
            self.image = player_stand
            self.rect = self.image.get_frect(center=(150, y))
        if type == 5:
            self.image = pygame.image.load('Grafiche/Macchine/macchina_nemico.png').convert_alpha()
            self.rect = self.image.get_frect(center=(700, y))

    def player_movement(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 150:
            self.rect.left -= 600 * dt
        if self.value == 1 or self.value == 3:
            if keys[pygame.K_d] and self.rect.right <= WIDTH - 150:
                self.rect.right += 600 * dt
        if self.value == 2:
            if keys[pygame.K_d] and self.rect.right <= WIDTH - 210:
                self.rect.right += 600 * dt
            
        return self.rect.center

    def car_player_movement(self, lane):
        keys = pygame.key.get_just_pressed()
        if self.gioco == 4:
            self.rect.centery = lane
        if keys[pygame.K_LEFT] and self.value == 4:
            self.rect.x = -5

    def change_position(self, max_pos,dt):
        if self.gioco == 4:
            pos = max_pos
            self.rect.centerx += self.momentum * dt
            if self.rect.centerx >= max_pos:
                self.rect.centerx = pos
          
    def animate(self,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d]:
            if self.value == 1:
                self.player_index += 6 * dt
                if self.player_index >= len(self.frames): self.player_index = 0
                self.image = self.frames[int(self.player_index)]
            if keys[pygame.K_a]:
                if self.value == 1:
                    self.image = pygame.transform.flip(self.image,True,False)
        else:
            if self.value == 1:
                self.image = self.player_stand
        
    def update(self,dt):
        self.player_movement(dt)
        self.animate(dt)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, y, minigioco):
        super().__init__()
        y_pos = 10
        self.gioco = minigioco
        self.right_collision = False
        self.screen = pygame.display.get_surface()

        if type == 1 or type == 2 or type == 3 or type == 7:
            num = randint(0, 4)
            if minigioco == 4:
                if type == 3:
                    self.image = pygame.image.load(join('Grafiche','Macchine','pietra.png')).convert_alpha()
                else:
                    bad_obstacle = ['fazzoletto.png', 'mozzicone.png', 'bottiglietta_plastica.png', 'bottiglia_vetro.png', 'buccia_banana.png']
                    self.image = pygame.image.load(join('Grafiche','Rifiuti','Cattivi',f'{bad_obstacle[num]}')).convert_alpha()
            else:
                bad_obstacle = ['fazzoletto.png', 'mozzicone.png', 'bottiglietta_plastica.png', 'bottiglia_vetro.png', 'buccia_banana.png']
                self.image = pygame.image.load(join('Grafiche','Rifiuti','Cattivi',f'{bad_obstacle[num]}')).convert_alpha()
                if self.gioco == 1:
                    if num == 0:
                        self.value = 1
                    elif num == 1:
                        self.value = 2
                    elif num == 2:
                        self.value = 3
                    elif num == 3:
                        self.value = 4
                    else:
                        self.value = 5
        if type == 1:
            self.rect = self.image.get_frect(center=(120, 450))  # ProvaBasket

        if type == 4 or type == 5:
            num = randint(0, 1)
            good_obstacle = ['goccia_acqua.png', 'piantina.png']
            self.image = pygame.image.load(join('Grafiche','Rifiuti','Buoni',f'{good_obstacle[num]}')).convert_alpha()
        if type == 2 or type == 5:
            self.rect = self.image.get_frect(center=(randint(180, 605), y_pos))  # Prova e Gioco

        if type == 6:
            self.image = pygame.image.load(join('Grafiche','Rifiuti','Buoni','fungo.png')).convert_alpha()
        if type == 3 or type == 4 or type == 6 or type == 7:
            self.rect = self.image.get_frect(center=(700, y))  # Gioco auto
            
        self.bg_surf = pygame.Surface((self.rect.width + 5, self.rect.height + 5))
        if type == 4 or type == 5:
            self.bg_surf.fill((183, 204, 235))
        self.bg_rect = self.bg_surf.get_frect(center=(self.rect.center + Vector2(2,-2)))
        self.bg_surf.set_alpha(180)
    
    def destroy(self):
        if self.gioco == 4:
            if self.rect.centerx <= -150:
                self.kill()
        if self.gioco == 2:
            if self.rect.y >= 525:
                self.kill()

    def check_throw(self, posizionex):
        if self.gioco == 1:
            self.rect.x = posizionex
            if (
                (self.value == 1 and posizionex >= 400 and posizionex < 480)
                or (self.value == 2 and posizionex >= 480 and posizionex < 560)
                or (self.value == 3 and posizionex >= 560 and posizionex < 640)
                or (self.value == 4 and posizionex >= 640 and posizionex <= 720)
                or (self.value == 5 and posizionex >= 320 and posizionex < 400)
            ):
                self.right_collision = True

        return self.right_collision
    
    def lower_semicircle_equation(self,x1, y1, x2, y2):
        h = (x1 + x2) / 2
        k = (y1 + y2) / 2
        
        r = sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2
        
        return k,r,h
    
    def throw(self,current_normal_size,throwing,k,r,h,current_pos):
        speed = 0
        if throwing:
            if current_normal_size >= 500:
                speed = 10
            else:
                speed = 8
            try:
                self.rect.center = self.bg_rect.center = (current_pos,k - sqrt(r**2 - (current_pos-h)**2))
            except:
                throwing = False
                
        return throwing, speed

    def update(self, velocity,dt):
        if self.gioco == 4:
            self.rect.x -= 400 * dt
            self.bg_rect.x -= 400 * dt
        if self.gioco == 2 or 3:
            self.rect.y += velocity * dt
            self.bg_rect.y += velocity * dt
            
        self.screen.blit(self.bg_surf,self.bg_rect)
        
        self.destroy()


class Trash(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 1:
            self.image = pygame.image.load(join('Grafiche','Cestini','cestino_carta.png')).convert_alpha()
            self.rect = self.image.get_frect(topleft=(400, 410))
        elif type == 2:
            self.image = pygame.image.load(join('Grafiche','Cestini','cestino_indifferenziata.png')).convert_alpha()
            self.rect = self.image.get_frect(topleft=(480, 410))
        elif type == 3:
            self.image = pygame.image.load(join('Grafiche','Cestini','cestino_plastica.png')).convert_alpha()
            self.rect = self.image.get_frect(topleft=(560, 410))
        elif type == 4:
            self.image = pygame.image.load(join('Grafiche','Cestini','cestino_vetro.png')).convert_alpha()
            self.rect = self.image.get_frect(topleft=(640, 410))
        else:
            self.image = pygame.image.load(join('Grafiche','Cestini','cestino_umido.png')).convert_alpha()
            self.rect = self.image.get_frect(topleft=(320, 410))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(join('Grafiche','Player','cestino.png'))
        self.rect = self.image.get_frect(center=(x, y))

    def update(self,dt):
        if self.rect.centery < -40:
            self.kill()
        self.rect.y -= 400 * dt


class Line(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 1:
            self.image = pygame.surface.Surface((10, 400))
            self.rect = self.image.get_frect(topleft=(-40, 100))
        else:
            self.image = pygame.surface.Surface((500, 10))
            self.image.fill('orange')
            self.rect = self.image.get_frect(topleft=(150, 525))


class Road(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.surface.Surface((80, 20))
        self.image.fill('white')
        self.rect = self.image.get_frect(topleft=(x, y))

    def update(self,dt):
        self.rect.x -= 400 * dt
        if self.rect.right <= 0:
            self.rect.left = 800


class Button:
    def __init__(self,text,width,height,pos,elevation):
        # core attributes
        self.screen = pygame.display.get_surface()
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]
        
        # top rect
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77' 
        
        # bottom rect
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'
        
        # text
        self.text_surf = test_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_frect(center = self.top_rect.center)
        
    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        
        pygame.draw.rect(self.screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(self.screen,self.top_color,self.top_rect,border_radius=12)
        self.screen.blit(self.text_surf,self.text_rect)
        self.check_click()
        
    def check_click(self):
        pressed = False
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
                pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77' 
            
        return pressed