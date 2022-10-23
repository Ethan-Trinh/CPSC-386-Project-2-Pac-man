import sys
import pygame as pg
from vector import Vector

movement = {pg.K_LEFT: Vector(-1, 0),   # dictionary to map keys to Vector velocities
            pg.K_RIGHT: Vector(1, 0),
            pg.K_UP: Vector(0, -1),
            pg.K_DOWN: Vector(0, 1),
            #pg.K_w: Vector(0, -1),
            #pg.K_a: Vector(-1, 0),
            #pg.K_s: Vector(0, 1),
            #pg.K_d: Vector(1, 0)
            }

  
def check_keydown_events(event, settings, pacman):
    key = event.key
    if key in movement.keys(): pacman.vel += settings.pac_speed * movement[key]
    elif key == pg.K_SPACE:
        pacman.shoot = True


def check_keyup_events(event, pacman):
    key = event.key
    if key in movement.keys(): pacman.vel = Vector()   # Lifting key should stop pacman
    elif key == pg.K_SPACE:
        pacman.shoot = False

def check_events(settings, pacman):
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN: 
            check_keydown_events(event=event, settings=settings, pacman=pacman)
        elif event.type == pg.KEYUP: check_keyup_events(event=event, pacman=pacman)


def clamp(posn, rect, settings):
    left, top = posn.x, posn.y
    width, height = rect.width, rect.height
    left = max(0, min(left, settings.screen_width - width))
    top = max(0, min(top, settings.screen_height - height))
    return Vector(x=left, y=top), pg.Rect(left, top, width, height)
