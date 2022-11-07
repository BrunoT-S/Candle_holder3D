import pygame as pg, sys
from settings_0 import *
from map_0 import *
from jogador_0 import *
from ray_caster_0 import *
from obj_renderer_0 import *

icone_jogo = pg.image.load("candle.png")
icone_jogo = pg.transform.scale(icone_jogo, (16,8))
pg.display.set_icon(icone_jogo)

#CBM
def vertical(size, startcolor, endcolor):
    """
    Draws a vertical linear gradient filling the entire surface. Returns a
    surface filled with the gradient (numeric is only 2-3 times faster).
    """
    height_ = size[1]
    bigSurf = pg.Surface((1,height_)).convert_alpha()
    dd = 1.0/height_
    sr, sg, sb, sa = startcolor
    er, eg, eb, ea = endcolor
    rm = (er-sr)*dd
    gm = (eg-sg)*dd
    bm = (eb-sb)*dd
    am = (ea-sa)*dd
    for y in range(height):
        bigSurf.set_at((0,y),
                        (int(sr + rm*y),
                         int(sg + gm*y),
                         int(sb + bm*y),
                         int(sa + am*y))
                      )
    return pg.transform.scale(bigSurf, size)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        

        

        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRender(self)
        self.raycasting = RayCasting(self)
        

    def update(self):
#        self.player.update()
        self.raycasting.update()
        self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'Candle Holder 3D (FPS:{self.clock.get_fps() : .2f})')
        

    def draw(self):
        self.screen.fill('black')
        #pg.draw.rect(self.screen, (111,111,33),(0, height/2, width, height/2))
        #pg.draw.rect(self.screen, (111,11,11),(0, 0, width, height/2))
        self.screen.blit(vertical((width,(height//5)*2),(233,133,11,100),(10,10,5,100)),(0,0))
        self.screen.blit(vertical((width,(height//5)*2),(15,0,5,100),(233,53,11,100)),(0,(height//5)*3))
        
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

        
   

if __name__ == '__main__':
    game = Game()
    game.run()
    print('O°O')
