from settings_0 import *
import pygame as pg, math

#dx, dy = 0,0

#create by me{
img = pg.image.load("candle.png")

img = pg.transform.scale(img, (100,200))

img_rect = img.get_rect()
#}
#pg.mixer.init()
#som_passos = pg.mixer.music.load('steps in wood floor.wav')
#som_passos.play(-1)

class Player:
    def __init__(self,game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE


        #created by me
        self.i, self.adder = 0, 1
        self.moving = False
    
    def moviment(self):
        
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0,0
        #global dx, dy
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        #CBM
        self.moving = False

        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin

            #CBM
            self.moving = True            

        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

            #CBM
            self.moving = True

        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos

            #CBM
            self.moving = True
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

            #CBM
            self.moving = True

        #CBM
        if self.moving == False:
            self.game.screen.blit(img, img_rect)
            img_rect.x = 500
            img_rect.y = 400
        else:
            self.move_candle()
            

        
        self.check_wall_collision(dx, dy)
        

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
            
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
            
        self.angle %= math.tau

    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx

        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
            
    def draw(self):
       # pg.draw.line(self.game.screen, 'pink', (self.x * 50, self.y * 50),
        #             (self.x * 50 + width * math.cos(self.angle),
         #             self.y * 50 + width * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 50 ,self.y * 50),15)

    def update(self):
        self.moviment()

    #CBM
    def passos(self):
        pass


    #create by me{
    def move_candle(self):
        self.game.screen.blit(img, img_rect)
        self.i += self.adder
        img_rect.x = 500 + self.i*5
        img_rect.y = 400 + int((1+2**self.i)/4)
        if self.i >= 10 or self.i <= -10:
            self.adder *= -1

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    
