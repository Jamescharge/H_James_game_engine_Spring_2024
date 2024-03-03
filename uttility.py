import pygame as pg
from settings import *
from math import floor

class Cooldown():
    def __init__(self):
        self.current_time = 20
        self.event_time = 0
        self.delta = 0
        self.test_timer = None  # Initialize test_timer as None

    def ticking(self):
        self.current_time = floor((pg.time.get_ticks()) / 1000)
        self.delta = self.current_time - self.event_time

    def countdown(self, x):
        x = x - self.delta
        if x is not None:
            return x

    def event_reset(self):
        self.event_time = floor((pg.time.get_ticks()) / 1000)

    def timer(self):
        self.current_time = floor((pg.time.get_ticks()) / 1000)

    def set_timer(self, timer_instance):
        self.test_timer = timer_instance

    def player_cooldown(self, pov_instance):
        if self.test_timer is not None:
            if pov_instance.speed > 400:
                print("Too fast for school")
                self.cooldownspeed = str(self.test_timer.countdown(5))
                if self.cooldownspeed == '0':
                    pov_instance.speed = 400
                    print("police came so I slowed down")
