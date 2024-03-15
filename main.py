#The creator of this file is: James H
#2/28 is when github has started always watching
#imported in items of python located here
import pygame as pg
from random import randint
from settings import *
from sprites import *
import sys
from os import path
from uttility import *
'''
personal ideas
        
rules: get high score, don't die, do not exit map(yet)
eatable enimes by a power up
To do
Add comments(difficulty: medium)


No brainer priotrity
time (difficuly:hard)

3 things I need to "add":
kill wall (difficuly:easy)
invisible wall (difficuly:easy)
health power up  (difficuly:easy)

3 things I should add (very real)
sprint (difficulty:easy)
randomness(difficulty:medium)
more maps(difficulty:medium)

menu(stat and pause)(difficulty:medium)
gambling(very much want when more maps is added)
pick up stuff(difficulty:hard)
gun(difficulty:hard)
proximity spike wall(difficulty:medium)



Bugs fixed
Kill wall now only kills you once
'''




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
        self.pov = None
        Pause = False
    # def start_screen(self):
    #     running = True
    #     while running:
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 running = False
    #                 pg.quit()
    #                 sys.exit()
    #             elif event.type == pg.KEYDOWN:
    #                 if event.key == pg.K_SPACE:
    #                     running = False 

    #         self.screen.fill(BGCOLOR)

    #         # Draw your start screen elements here
    #         self.draw_text("Silly Game", 48, WHITE, WIDTH // 2, HEIGHT // 4)
    #         self.draw_text("Hit space to PLAY THE GAME", 24, WHITE, WIDTH // 2, HEIGHT // 2)

    #         pg.display.flip()
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
    #These define the groups
        #I need to add to it (almost)everytime I add a feture that needs to be loaded in the game 
        print("create new game...")
        self.cooldown = Timer(self)
        self.pov = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.healup = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.speed = pg.sprite.Group()
        self.kill_wall = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.nosee_wall = pg.sprite.Group()
        self.sprinting = pg.sprite.Group()
        self.keys = pg.sprite.Group()
        self.keywall = pg.sprite.Group()
        self.lookskeywall = pg.sprite.Group()
        # self.player1 = Player(self, 1, 1)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
               #this defines each and every map item in the #map area
                if tile == '1':
                    # print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.pov = Pov(self, col, row)
                    self.Prow = row
                    self.Pcol = col
               
                if tile == 'C':
                    Coins(self, col, row)
                if tile == 'S':
                    Speed(self, col, row)
                if tile == '2':
                    # print("a kill wall at", row, col)
                    KillWall(self, col, row)
                if tile == 'M':
                    Mob2(self, col, row)
                # if tile == 'M':
                #     Mob(self, col, row)
                if tile == 'H':
                    HealUp(self, col, row)
                if tile == 'k':
                    Key(self, col, row)
                if tile == 'K':
                    LooksKeyWall(self, col, row)
                    KeyWall(self, col, row)
                if tile == '3':
                    print("shhhhhhhh", row, col)
                    MobWall(self, col, row)
    #making it so the game can close when requested
    

    #able to quit whenever
    def quit(self):
        pg.quit()
        sys.exit()

   #not defining sprites all I think
    def update(self):
        self.all_sprites.update()
        self.ready_to_pause()
        self.cooldown.ticking()
    
    def draw_grid(self):
         for x in range(0, WIDTH, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
         for y in range(0, HEIGHT, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #this was defined by the amazing Mr Cozord
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
            #at 0 until I work it out                                         base 24 ^    this was 2


            self.draw_text(self.screen, "Coin " + str(self.pov.moneybag), 24, WHITE, 2, 17)           
            self.draw_text(self.screen, "Lives " + str(self.pov.health), 24, WHITE, 2, 3)
            self.draw_text(self.screen, "Speed " + str(self.pov.speed), 24, WHITE, 2, 35)
            # self.draw_text(self.screen, str(self.test_timer.countdown(60)), 24, WHITE, WIDTH/2 - 32, 2)
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
    #                 self.player1.movssssssse(dx=1)
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
            
#this is mr cozort start screen
    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen,"THE SILLY OF GAMES ", 24, WHITE, 24, 35)
        self.draw_text(self.screen,"Made by James with C ", 24, WHITE, 24, 70)
        pg.display.flip()
        self.wait_for_key()
        
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False
                    
    def ready_to_pause(self):
    
        # self.clock.tick(FPS)
        if Pause == False:
            for event in pg.event.get():
                if event.type == pg.K_p:
                    Pause = True
                    self.show_pause_screen()
    def show_pause_screen(self):        
            self.screen.fill(BGCOLOR)
            self.draw_text(self.screen,"THE SILLY OF GAMES ", 24, WHITE, 24, 35)
            self.draw_text(self.screen,"Made by James with C ", 24, WHITE, 24, 70)
            pg.display.flip()
        


g = Game()
# g.show_start_screen()
g.show_start_screen()
while True:
    g.new()
    g.run()
    
    #g.show_go_screen()
    