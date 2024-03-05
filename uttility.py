# utility.py
import pygame as pg
from math import floor

class Cooldown():
    def __init__(self):
        self.current_time = 20
        self.event_time = 0
        self.delta = 0
        self.test_timer = None

    def ticking(self):
        self.current_time = floor((pg.time.get_ticks()) / 1000)
        self.delta = self.current_time - self.event_time

    def countdown(self, x):
        x = x - self.delta
        if x > 0:
            return x
        else:
            return 0

    def event_reset(self):
        self.event_time = floor((pg.time.get_ticks()) / 1000)

    def set_timer(self, timer_instance):
        self.test_timer = timer_instance
    
