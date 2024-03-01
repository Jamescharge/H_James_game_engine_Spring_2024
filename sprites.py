#This file is another file by James H 
# this code was inspired by Zelda and informed by Chris Bradfield (Very cool person)
import pygame as pg
from settings import *
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
        self.speed = 400
        self.health = 3
        
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
        for hit in hits:
            if isinstance(hit, Coins):
                self.moneybag += 1
            if isinstance(hit, Speed):
                self.speed += 200
                print("silly")
            if isinstance(hit, KillWall):               
                print("silly")
                self.kill()
            if isinstance(hit, HealUp):               
                self.health += 1
            if isinstance(hit, Mob):
                self.kill()


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
        # coin_hits = pg.sprite.spritecollide(self.game.coins, True)
        # if coin_hits:
        #     print("I got a coin")
    def kill(self):
        self.x = self.game.Pcol*TILESIZE
        self.y = self.game.Prow*TILESIZE
        self.health -= 1
        if self.health == 0:
            pg.quit()

        


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
#the following Mob code is made by Chris Cozort my wonderful computer science teacher
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
