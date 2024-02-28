#The creator of this file is: James H
#
#imported in items of python located here
import pygame as pg
from random import randint
from settings import *
from sprites import *
import sys
from os import path
from sprites import Pov

class Game:
   
   #the game engine is here
    def __init__(self,):
       #using pygame here
        pg.init()
        #oppening the screen
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        #making the clock self sustaning if it wants to
        self.clock = pg.time.Clock()
        self.load_data()
    def load_data(self):
                #the following code under game_flder until self.map_data was given to us from mr CoZart fully
        game_folder = path.dirname(__file__)
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
    def new(self):

        print("create new game...")
        self.pov = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        # self.player1 = Player(self, 1, 1)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.pov = Pov(self, col, row)
                #I strongly dislike the next 2 lines
                if tile == 'C':
                    Coins(self, col, row)
                if tile == 'p':
                    PowerUp(self, col, row)
   
    #making it so the game can close when requested
    

    #able to quit whenever
    def quit(self):
        pg.quit()
        sys.exit()
   #not defining sprites all I think
    def update(self):
         self.all_sprites.update()
  
    def draw_grid(self):
         for x in range(0, WIDTH, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
         for y in range(0, HEIGHT, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('Time New Roman')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)  
    def draw(self):
            self.screen.fill(BGCOLOR)
            self.draw_grid()
            self.all_sprites.draw(self.screen)
            #at 0 until I work it out                                         base 24 ^
            self.draw_text(self.screen, "Coin Amount " + str(self.pov.moneybag), 24, WHITE, WIDTH/5 - 32, 2)
            pg.display.flip()
#some more events instead of event                              commented out this
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_LEFT:
    #                 self.player1.move(dx=-1)
    #             if event.key == pg.K_RIGHT:
    #                 self.player1.move(dx=1)
    #             if event.key == pg.K_UP:
    #                 self.player1.move(dy=-1)
    #             if event.key == pg.K_DOWN:
    #                 self.player1.move(dy=1)
    def run(self,):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
                #need to run these things
g = Game()
# g.show_start_screen()
while True:
    g.new()
    g.run()
    
    #g.show_go_screen()
    