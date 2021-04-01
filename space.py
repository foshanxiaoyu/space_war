import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("shot")

# Load images
# RED_SPACE_SHIP = pygame.image.load(os.path.join("res",1.png))
# GREEN_SPACE_SHIP = pygame.image.load(os.path.join("res",2.png))
# BULE_SPACE_SHIP = pygame.image.load(os.path.join("res",3.png))

# Play_SHIP
# YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("res","4.png"))
Player_SPACE_SHIP = pygame.transform.scale(pygame.image.load(os.path.join("res", "4_1.gif")),(30,30))

# Lasers
# RED_SPACE_Lasers_SHIP = pygame.image.load(os.path.join("res",1.png))
# GREEN_SPACE_Lasers_SHIP = pygame.image.load(os.path.join("res",1.png))
# BULE_SPACE_Lasers_SHIP = pygame.image.load(os.path.join("res",3.png))

# YELLOW_SPACE_Lasers_SHIP = pygame.image.load(os.path.join("res",4.png))

# Background
# BG = pygame.image.load(os.path.join("res", "BG.png"))
BG = pygame.transform.scale(pygame.image.load(os.path.join("res", "BG.png")),(WIDTH,HEIGHT))

# Ship class
class Ship:
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.leaser_img = None
        self.cool_down_count = 0

    
    def draw(self,window):
        # pygame.draw.rect(window,(255,134,123),(self.x,self.y,30,30),0,-1,-1,-1,-1,-1)
        window.blit(self.ship_img,(self.x,self.y))
class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.max_health = health
        self.ship_img = Player_SPACE_SHIP
        self.mask = pygame.mask.from_surface(self.ship_img)
        

def main():
    run = True
    FPS = 50
    player_vel = 5
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans",30)
    player = Player(300,400)
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG,(0,0))
        # draw text
        level_label = main_font.render(f"level:{level}",1,(255,255,255))
        lives_label = main_font.render(f"lives:{lives}",1,(255,0,222))
        WIN.blit(level_label,(20,20))
        WIN.blit(lives_label,(WIDTH-lives_label.get_width()-20,20))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and player.x+player_vel>0:
            player.x -= player_vel 
        if keys[pygame.K_RIGHT] and player.x+player_vel+30<WIDTH:
            player.x += player_vel 
        if keys[pygame.K_UP] and player.y+player_vel>0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y+player_vel+20<HEIGHT:
            player.y += player_vel
        
main()
