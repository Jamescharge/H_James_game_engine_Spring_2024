#The creator of this file is: James H
#2/28 is when github has started always watching
#imported in items of python located here
import pygame as pg
from tipslist import *
from settings import *
from sprites import *
from random import *
from random import choice
import sys
from os import path
from uttility import *

#beta is 
#Adding a boss fight
#more levels

'''
personal ideas
        
rules: get high score, don't die, do not exit map(yet)
eatable enimes by a power up

Done
sprint (difficulty:easy)
kill wall (difficuly:easy)
invisible wall (difficuly:easy)
health power up  (difficuly:easy)
To do


Add comments(difficulty: medium)


3 things I should add (very real)

#MAKE THEM MOVE AT DIFFERNT SPEEDS

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

'''
5 Elements of fun
Avoiding enemys
Collecting coins
Finding glitchs in the mobs ai
Reading the Custom messages
Using sprint to give the feeling of more control
'''



LEVEL1 = "level1.txt"
LEVEL2 = "level2.txt"
tips = [
            "There are 69 very helpful and fun tips",
            "Do not hit the wall twice(I patched it silly)",
            "I probaly fixed a glitch",  
            "If you find a glitch report it(or please exsploit it)",
            "I engourage finding a way to break the game",
            "1/69 chance of seeing this message",
            "custimizing messages is boring(this is message :)  )",
            "I do not have a lot of fetures - 3/25/24",
            "Inspired by minecraft - in the next game",
            "sounds are silly(next on the list of things to add)",
            "This is a no yap zone(have good listennig ears)",
            "should call this a demo(it is not even out of beta)",
            "These texts arn't meta, they are factural",
            "You got this (maybe idk)",
            "hit w, a or d and s because something might happen",
            "I should make a mode that just breaks the game oh wait I already did that",
            "Hold shift to sprint because if you don't, it might be rough world out there",
            "it would be funny if the mob speed was random",
            "No message is meta unless it comments on non meta messages",
            "These won't be boring one day",
            "Is it game devolopment if the only thing you are devoloping is a healthy google search history",
            "hitting the q button does nothing",
            "What if ninja got a low taper fade",
            "who_asked_you're_opinion.png",
            "I hope anchient historians read this and go ' hey thats me ' ",
            "no one reads the secret tips and tricks",
            "I only write these when the schools internet during lunch is down",
            "Do this instead of hk (hollow knight)",
            "[insert a refrence to canadians]",
            "[404 yap session uncalled for]",
            "1/20 of these have something to do with the game",
            "press arrow keys instead of wasd to feel special(your not unique)",
            "why have you not left clicked already",
            "to lazy to know how to move this to a seperat txt file",
            "when did you learn the alphabet?",
            "we all have skill issues every once in a while, yours is just ongoing indeffinitly",
            "I have 7 reasons to not be silly but the other 412 say other whys",
            "someone infront of me tried to use burp to load a bot token on discord(they are so silly)",
            "it would be meta to say 'does anyone read these' but like everyone does that so the meta thing is to point it out",
            "[Insert Chiper the lead to it here] is Parrotx2's real name",
            "I am a kindergardener",
            "all these messages are silly and if you are offended all complaints go to the bin on the left side of the Deans office",
            "Are you silly, then spell it",
            " 'I don't even know who you are' this silly guy",
            "I hate physics",
            "I do not remeber what I was gonna say",
            "I have bad memory",
            "ERB is the best youtube channel",
            "pain of writing",
            "[101 did not know anyone care]",
            "I am glad that someone clicked left click in a bit",
            "red, orange , puple yellow, blue",
            "you guys think I am funny right?!",
            "Robert J chess is silly",
            "refrencing alt acounts in here",
            "big silly terificance is just Big T",
            "would be funnier but some do not allow true creative genius",
            "I still have bugs",
            "I probaly fixed a glitch",
                ]

gameover = False
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
        self.povhasakey = 0
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
        self.on_level = 1
        if self.on_level == 1 :
            currentlevel = LEVEL1 
        if self.on_level == 2:
            currentlevel = LEVEL2 
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, currentlevel), 'rt') as f:
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
        self.next_level_wall = pg.sprite.Group()
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
                if tile == '4':
                    NextLevelWall(self, col, row)
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
                if tile == 'S':
                    sidetoside(self, col, row, speed=100)
                if tile == 'k':
                    Key(self, col, row)
                if tile == 'K':
                    #defined it twice so 2 walls were placed so that when one wall is killed it looks like noting has changed (kind of)
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
 
   
    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        #might revamp if we move on
        r = Random() 
        selected_tip = r.choice(tips)
        tip_text = (selected_tip )
        self.draw_text(self.screen,"THE SILLY OF GAMES ", 24, WHITE, 24, 35)
        self.draw_text(self.screen,"Made by James with C ", 24, WHITE, 24, 70)
        self.draw_text(self.screen,"Left click to begin ", 24, WHITE, 24, 115)
        self.draw_text(self.screen,"Secret Tip: ", 24, WHITE, 24, 270)
        self.draw_text(self.screen,tip_text, 24, WHITE, 24, 305)
        pg.display.flip()
        self.wait_for_key()
    startquit = False 
    #not defining sprites all I think
    def update(self):
        self.all_sprites.update()
        self.ready_to_pause()
        self.cooldown.ticking()
        if self.pov.health == 0:
            g.show_gameover_screen
            self.playing = False
    #drawing the grey grid on the bored
    def draw_grid(self):
         for x in range(0, WIDTH, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
         for y in range(0, HEIGHT, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #this was made by Corzort
    #this is defining text outline for draw
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
            #drwing coins, lives, and Speed
            self.draw_text(self.screen, "Coin " + str(self.pov.moneyamount), 24, WHITE, 2, 17)           
            self.draw_text(self.screen, "Lives " + str(self.pov.health), 24, WHITE, 2, 3)
            self.draw_text(self.screen, "Speed " + str(self.pov.speed), 24, WHITE, 2, 31)
            if self.povhasakey == 1:
                self.draw_text(self.screen, "YOU HAVE A KEY " + str(self.pov.speed), 24, WHITE, 20, 31)
            # self.draw_text(self.screen, str(self.test_timer.countdown(60)), 24, WHITE, WIDTH/2 - 32, 2)
            pg.display.flip()
#flip display after everything
    
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
   #this starts up the game 
    def run(self,):
        
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
                #need to run these things
            
#this is mr cozort start screen

    
      #when you click the start screen goes  
    def wait_for_key(self):
        waiting = True
        restarting = False
        while waiting:
            
            # print("testing it")
            self.clock.tick(FPS)
            if restarting == True :
                g.show_start_screen
                restarting = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit = False
                #mouse button left click
                if event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False

        
        #MY ATEMPT at pause screen
                    #will revamp if more time            
    def ready_to_pause(self):
        # Pause = False
        # # self.clock.tick(FPS)
        # if Pause == False:
            for event in pg.event.get():
                if event.type == pg.K_p:
                    Pause = True
                 
   #same idea

   
    def show_gameover_screen(self):        
            self.screen.fill(BGCOLOR)
            self.draw_text(self.screen,"Game Over ", 24, WHITE, 24, 35)
            self.draw_text(self.screen,"You Tried blud ", 24, WHITE, 24, 70)
            pg.display.flip()
            
    # def restart(self):
        # if gameover == True:            
        #     for event in pg.event.get():
        #         if event.type == pg.MOUSEBUTTONDOWN:
                    



#defines game as G
g = Game()
# g.show_start_screen()
    
g.show_start_screen()
#runs game fully with new and run
while True:
    g.new()
    g.run()
