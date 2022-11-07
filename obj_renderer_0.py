import pygame as pg
from settings_0 import *

class ObjectRender:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.object_to_render
        for depth, image, pos in list_objects:
            image.set_alpha(255//(0.005 + depth//1.5))#CBM
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res = (TEXTURE_SIZE,TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
        
    def load_wall_textures(self):
        return {
        2: self.get_texture('textures\wall_2.png'),
        1: self.get_texture('textures\wall_1.png'),
        3: self.get_texture('textures\wall_3.png'),
        }
