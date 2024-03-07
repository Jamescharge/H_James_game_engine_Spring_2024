#This file is another file by James H 
# this code was inspired by Zelda and informed by Chris Bradfield (Very cool person)
import pygame as pg
from settings import *
from uttility import *

class Pov(pg.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.all_sprites , game.pov
        # init super class
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
    
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.moneybag = 0
        self.speed = 300
        self.health = 3
        self.revert_speed = False 
        self.invincible = False
      
        self.cooldownspeedread = 0

        

    # def move(self, dx=0, dy=0):
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -self.speed 
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = self.speed  
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -self.speed  
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = self.speed
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    # def speed_cooldown(self):
        
    #     # self.cooldownspeed.countdown(5) 
    #     if self.speed > 351:                           
    #         print("I was called/loved once")
            
    #         str(self.test_timer.countdown(5))
    #         if str(self.test_timer.countdown(5)) == 1 :
    #             print("and I was nieve to exspect this to work")
    #             self.speed += -200
    #             self.test_timer.event_reset()
                
    # def move(self, dx=0, dy=0):
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy

    # def collide_with_walls(self, dx=0, dy=0):
    #     for wall in self.game.walls:
    #         if wall.x == self.x + dx and wall.y == self.y + dy:
    #             return True
    #     return False
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y          
    # def kill_collide_with_walls(self, dir):   
    #     if dir == 'x':
    #         hits = pg.sprite.spritecollide(self, self.game.kill_wall, False)
    #         if hits:
    #             if self.vx > 0:
    #                 self.x = hits[0].rect.left - self.rect.width
    #             if self.vx < 0:
    #                 self.x = hits[0].rect.right
    #             self.vx = 0
    #             self.rect.x = self.x
    #     if dir == 'y':
    #         hits = pg.sprite.spritecollide(self, self.game.kill_wall, False)
    #         if hits:
    #             if self.vy > 0:
    #                 self.y = hits[0].rect.top - self.rect.height
    #             if self.vy < 0:
    #                 self.y = hits[0].rect.bottom
    #             self.vy = 0
    #             self.rect.y = self.y         
                
                
    # def collide_with_group(self, group, kill):
    #     hits = pg.sprite.spritecollide(self, group, kill)
    #     if hits:
    #         if str(hits[0].__class__.__name__) == Coins:
    #             self.moneybag += 1
    #             print("you got coined")
    #         if str(hits[0].__class__.__name__) == PowerUp:
    #             self.speed += 200
                                #   Solution
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        invincible  = False
        for hit in hits:
            if isinstance(hit, Coins):
                self.moneybag += 1
            if isinstance(hit, Speed):
                if self.speed == 300:
                    self.speed += 200
                    self.game.cooldown.cd = 5

                if self.speed == 350:
                    print("add sprint speed thing ability")
                    pass
            elif isinstance(hit, KillWall):
                print("silly")
                if not invincible:
                    self.kill()
                invincible = True
            elif isinstance(hit, HealUp):
                self.health += 1
            elif isinstance(hit, Mob):
                if not invincible:
                    self.kill()
                invincible = True 



    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        # add collision later
        self.collide_with_walls('x')
        self.rect.y = self.y
        # add collision later
        self.collide_with_walls('y')
        self.collide_with_group(self.game.coins, True)
        self.collide_with_group(self.game.speed, True)
        self.collide_with_group(self.game.healup, True)
        self.collide_with_group(self.game.kill_wall, False)
        self.collide_with_group(self.game.mobs, False)
  
        if self.health >= 5:
            self.health = 5
        
        # coin_hits = pg.sprite.spritecollide(self.game.coins, True)
        # if coin_hits:
        #     print("I got a coin")
        
        #cooldowns




    def kill(self):
        self.x = self.game.Pcol*TILESIZE
        self.y = self.game.Prow*TILESIZE
        if self.invincible == False:
            self.health -= 1
        if self.invincible == True:
            print("2 bird with one death")       
        if self.health == 0:
            pg.quit()
    
    
    def invincible(self):
        self.invincible = True
        if self.invincible == True:
            self.invinciblecount = str(self.test_timer.countdown(3))
            print("it did the thing")
            if self.invinciblecount == '0':
                self.invincible = False


        


# class Powerup(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.teleport
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(LIGHTGREY)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE
    
    #def collet_power_up()
        



    # def move(self, dx=0, dy=0):
#another class difined mainly by how Cozart went by
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class KillWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.kill_wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    # def death_cooldown(self):


class MobWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.nosee_wall
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # This makes transparancy
        self.image = pg.Surface((TILESIZE, TILESIZE), pg.SRCALPHA)
        # should invisible it 
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

#will use at furture date
# class ShootAbleWeapon (pg.sprite.Sprite):
#     def __init__ (self, game,x,y):
#         self.groups = game.all_sprite, game.gun
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(BLACK)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * self.pov
#         self.rect.y = y * self.pov

class Coins(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
#Original Power up
class Speed(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.speed
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class HealUp(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.healup
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
# MOB code made by amazing computer science teacher Mr Cozort
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100, 100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 1 
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls,False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
            hits2 = pg.sprite.spritecollide(self,self.game.kill_wall, False)
            if hits2:
                self.vx *= -1
                self.rect.x = self.x
            hits3 = pg.sprite.spritecollide(self,self.game.nosee_wall, False)
            if hits3:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y

            hits2 = pg.sprite.spritecollide(self,self.game.kill_wall, False)
            if hits2:
                self.vy *= -1
                self.rect.y = self.y
            hits3 = pg.sprite.spritecollide(self,self.game.nosee_wall, False)
            if hits3:
                self.vy *= -1
                self.rect.y = self.y
            

    def update(self):
        # self.rect.x += 1
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        
        if self.rect.x < self.game.pov.rect.x:
            self.vx = 100
        if self.rect.x > self.game.pov.rect.x:
            self.vx = -100    
        if self.rect.y < self.game.pov.rect.y:
            self.vy = 100
        if self.rect.y > self.game.pov.rect.y:
            self.vy = -100
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')