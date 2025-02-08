import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
import Simulate
from math import tan

pg.init()
screen = pg.display.set_mode((1200, 800))
clock = pg.time.Clock()

system = Simulate.Simulate()

planet_list = []
planet_count = 0
running_simulation = False

draw_lines = []

def create_planet(pos_x, pos_y):
    global planet_count
    if planet_count < 3 : planet_count += 1
    mass = 10
    if planet_count < 4:
        planet = pg.Rect(pos_x - (mass/2), pos_y - (mass/2), mass, mass)
        planet_list.append(planet)
        system.addBodies(planet)

def clear_screen():
    global planet_list
    global planet_count
    planet_list = []
    planet_count = 0
    screen.fill((0, 0, 0))

def start_simulation():
    if planet_count == 3:
        global running_simulation
        running_simulation = True

def stop_simulation():
    global running_simulation
    running_simulation = False

def get_initial_velocity(pos_x0, pos_y0, pos_xf, pos_yf):
    line = pg.draw.line(screen, "purple", (pos_x0, pos_y0), (pos_xf, pos_yf), 5)
    t = 1 #  1 pixel = 10k m/s or smth
    dx = pos_xf - pos_x0
    dy = pos_yf - pos_y0
    v0_x = dx / t
    v0_y = dy / t
    return v0_x, v0_y

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

set_v0 = Toggle(screen, 925, 200, 50, 25)

frames = 0

while True:
    screen.fill((0, 0, 0))
    clock.tick(24)
    pg.draw.rect(screen, (255, 255, 255), [900, 0, 300, 300], 0)

    draw_text("Set v0 = 0", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 200)

    frames += 1

    if frames < 24*6:
        draw_text("Click and drag to add planets and set v0.", pg.font.SysFont("Arial", 20), (255, 255, 255), 300, 50)
        draw_text("Magnitude of v0 is determined by distance dragged, not by speed dragged at.", pg.font.SysFont("Arial", 20), (255, 255, 255), 150, 100)

    start = Button(screen, 900, 0, 300, 50, text="Start", inactiveColour=(50, 200, 50), hoverColour=(50, 200, 50), onClick=lambda: start_simulation())
    stop = Button(screen, 900, 50, 300, 50, text="Stop", inactiveColour=(255, 0, 0), hoverColour=(255, 0, 0), onClick=lambda: stop_simulation())
    reset = Button(screen, 900, 100, 300, 50, text="Reset", inactiveColour=(150, 150, 150), hoverColour=(150, 150, 150), onClick=lambda: clear_screen())

    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN: 
            pos_x0, pos_y0 = pg.mouse.get_pos()
            print(pos_x0, pos_y0)
            if pos_x0 < 900:
                create_planet(pos_x0, pos_y0)

        if event.type == pg.MOUSEBUTTONUP:
            pos_xf, pos_yf = pg.mouse.get_pos()
            print(pos_xf, pos_yf)
            if set_v0.value == False:
                get_initial_velocity(pos_x0, pos_y0, pos_xf, pos_yf)

    if running_simulation == True:
        system.run(0)

    for i in range(len(planet_list)):
        if i == 0:
            curr_planet = pg.draw.rect(screen, "blue", planet_list[i])
        elif i == 1:
            curr_planet = pg.draw.rect(screen, "red", planet_list[i])
        elif i == 2:
            curr_planet = pg.draw.rect(screen, "yellow", planet_list[i])
    
    pygame_widgets.update(events)
    pg.display.update()