import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 640, 480
# WIN = pygame.display.set_mode((0, 0))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# WIN = pygame.display.set_mode((1920, 1080),vsync=1)
pygame.display.set_caption("太空大战")

# Load images
RED_SPACE_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "1.png")), (30, 30))
GREEN_SPACE_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "2.png")), (30, 30))
BULE_SPACE_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "3.png")), (30, 30))

# Play_SHIP
# YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("res","4.png"))
Player_SPACE_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "4_11.gif")), (30, 30))

# Lasers
RED_SPACE_Lasers_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "1-l.png")), (30, 30))
GREEN_SPACE_Lasers_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "2-l.png")), (30, 30))
BULE_SPACE_Lasers_SHIP = pygame.transform.scale(
    pygame.image.load(os.path.join("res", "3-l.png")), (30, 30))

# YELLOW_SPACE_Lasers_SHIP = pygame.image.load(os.path.join("res",4.png))

# Background
# BG = pygame.image.load(os.path.join("res", "BG.png"))
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("res", "BG.png")), (WIDTH, HEIGHT))



# Ship class include Player and Enemy common attibutes
class Ship:
    COOLDOWN = 30
    
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_count = 0

    def draw(self, window):
        # pygame.draw.rect(window,(255,134,123),(self.x,self.y,30,30),0,-1,-1,-1,-1,-1)
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self,val,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):




    
    def cooldown(self):
        if self.cool_down_count >= self.COOLDOWN:
            self.cool_down_count = 0
        elif self.cool_down_count>0:
            self.cool_down_count += 1

    def shoot(self):
        if self.cool_down_count == 0:
            laser = Laser(x,y,self.laser_img)
            self.lasers.append(laser)
            self.cool_down_count = 1

    def getWidth(self):
        return self.ship_img.get_width()

    def getHeight(self):
        return self.ship_img.get_height()

# Players ship inherit Ship class attributes
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.max_health = health
        self.ship_img = Player_SPACE_SHIP
        self.mask = pygame.mask.from_surface(self.ship_img)

# Enemys ship inherit Ship class attributes
class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_SPACE_Lasers_SHIP),
        "green": (GREEN_SPACE_SHIP, GREEN_SPACE_Lasers_SHIP),
        "blue": (BULE_SPACE_SHIP, BULE_SPACE_Lasers_SHIP),
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.leaser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

# Laser define class 
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, val):
        self.y += val

    def off_screen(self, height):
        return self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(self, obj)

######## collide ###########
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2, (offset_x, offset_y)) != None


def main():
    FPS = 50
    player_vel = 5
    ##########################
    level = 1
    lives = 5
    ##########################
    enemies = []
    enemy_vel = 1
    wave_length = 5
    ##########################
    run = True
    lost = False
    lost_count = 0
    #####################
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 60)

    #####################
    player = Player(300, 400)
    clock = pygame.time.Clock()

    def redraw_window():

        WIN.blit(BG, (0, 0))
    # draw text
        level_label = main_font.render(f"level:{level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"lives:{lives}", 1, (255, 0, 222))
        WIN.blit(level_label, (20, 20))
        WIN.blit(lives_label, (WIDTH-lives_label.get_width()-20, 20))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)
        ############# Lost_label ##############
        if lost:
            lost_label = main_font.render("YOU ARE LOST", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH/2-lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS*3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x+player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x+player_vel+player.getWidth() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_UP] and player.y+player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y+player_vel+player.getHeight() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()



        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.getHeight() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)


main()
