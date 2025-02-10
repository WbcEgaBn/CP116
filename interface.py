import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import simulate
import planets
from random import randint

pg.init()
screen = pg.display.set_mode((1200, 800))
clock = pg.time.Clock()

system = simulate.Simulate()

planet_list = []
planet_count = 0
running_simulation = False

draw_lines = []

def create_planet(pos_x, pos_y):
    global planet_count
    planet_count += 1
    mass = 1
    color = (randint(100, 255), randint(100, 255), randint(100, 255))
    math_planet = planets.Planets(position=[pos_x - (mass/2), pos_y - (mass/2)], mass=mass)
    system.addBodies(math_planet)
    planet = pg.Rect(pos_x - (mass/2), pos_y - (mass/2), mass*10, mass*10)
    planet_list.append([planet, color])

def clear_screen():
    global planet_list
    global planet_count
    planet_list = []
    system.deleteBodies()
    planet_count = 0
    screen.fill((0, 0, 0))
    stop_simulation()

def start_simulation():
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
    return (v0_x, v0_y)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

set_v0 = Toggle(screen, 925, 180, 50, 25)
show_trail = Toggle(screen, 925, 230, 50, 25)
grav_const = TextBox(screen, 905, 300, 50, 50, fontSize=20)
grav_slider = Slider(screen, 975, 320, 200, 25, min=1, max = 1000, step=10)
grav_const.disable() 
start = Button(screen, 900, 0, 300, 50, text="Start", inactiveColour=(50, 200, 50), hoverColour=(50, 200, 50), onClick=lambda: start_simulation())
stop = Button(screen, 900, 50, 300, 50, text="Stop", inactiveColour=(255, 0, 0), hoverColour=(255, 0, 0), onClick=lambda: stop_simulation())
reset = Button(screen, 900, 100, 300, 50, text="Reset", inactiveColour=(150, 150, 150), hoverColour=(150, 150, 150), onClick=lambda: clear_screen())


frames = 0

while True:
    if show_trail.value == False:
        screen.fill((0, 0, 0))

    clock.tick(60)
    pg.draw.rect(screen, (255, 255, 255), [900, 0, 300, 900], 0) # change 4th num

    draw_text("Set v0 = 0", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 180)
    draw_text("Show planet trail", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 230)
    draw_text("Gravitational constant ↓ ", pg.font.SysFont("Arial", 20), (0, 0, 0), 970, 280)
    grav_const.setText(grav_slider.getValue())
    frames += 1

    if frames < 150:
        draw_text("Click and drag to add planets and set v0.", pg.font.SysFont("Arial", 20), (255, 255, 255), 300, 50)
        draw_text("Magnitude of v0 is determined by distance dragged, not by speed dragged at.", pg.font.SysFont("Arial", 20), (255, 255, 255), 150, 100)

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
        int = 0
        planet_list_math = system.getBodies()

        for planet in planet_list_math: 
            planet_x = planet.get_position()[0]
            planet_y = planet.get_position()[1]
            planet_list[int] = [pg.Rect(planet_x, planet_y, 10, 10), planet_list[int][1]]
            int += 1

    for i in range(len(planet_list)):
        curr_planet = pg.draw.rect(screen, planet_list[i][1], planet_list[i][0], border_radius=3)
    
    pygame_widgets.update(events)
    pg.display.update()