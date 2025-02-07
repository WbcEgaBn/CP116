import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
import Simulate

pg.init()
screen = pg.display.set_mode((1200, 800))
clock = pg.time.Clock()

running = False


# get circles done on screen, when clicked
# when run is clicked, location is updated

system = Simulate.Simulate()

planet_list = []
planet_count = 0

def create_planet(pos_x, pos_y):
    #planet = pg.draw.circle(screen, "blue", pos, 1)
    global planet_count
    planet_count += 1
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
    print(planet_count)
    if planet_count == 3:
        system.run(0)

while True:
    screen.fill((0, 0, 0))
    clock.tick(24)
    pg.draw.rect(screen, (255, 255, 255), [900, 0, 300, 300], 0)

    start = Button(screen, 900, 0, 300, 50, text="Start", inactiveColour=(50, 200, 50), hoverColour=(50, 200, 50), onClick=lambda: start_simulation())
    stop = Button(screen, 900, 50, 300, 50, text="Stop", inactiveColour=(255, 0, 0), hoverColour=(255, 0, 0))
    reset = Button(screen, 900, 100, 300, 50, text="Reset", inactiveColour=(150, 150, 150), hoverColour=(150, 150, 150), onClick=lambda: clear_screen())


    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONUP: 
            pos_x, pos_y = pg.mouse.get_pos()
            if pos_x < 900:
                create_planet(pos_x, pos_y)

    for i in range(len(planet_list)):
        if i == 0:
            curr_planet = pg.draw.rect(screen, "blue", planet_list[i])
        elif i == 1:
            curr_planet = pg.draw.rect(screen, "red", planet_list[i])
        elif i == 2:
            curr_planet = pg.draw.rect(screen, "yellow", planet_list[i])

    
    
    pygame_widgets.update(events)
    pg.display.update()