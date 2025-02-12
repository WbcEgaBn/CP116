import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import simulate
import planets
from random import randint

#start program objects
pg.init()
screen = pg.display.set_mode((1200, 820))
clock = pg.time.Clock()

#base variables
system = simulate.Simulate()

planet_list = []
planet_count = 0
running_simulation = False

draw_lines = []
save_orbit_planet_list = []
mass = 1

#adds a planet to visual list and system
def create_planet(pos_x, pos_y):
    global planet_count
    planet_count += 1
    color = (randint(100, 255), randint(100, 255), randint(100, 255))
    math_planet = planets.Planets(position=[pos_x - (mass/2), pos_y - (mass/2)], mass=mass, color = color)
    system.addBodies(math_planet)
    planet = pg.Rect(pos_x - (mass/2), pos_y - (mass/2), mass*10, mass*10)
    planet_list.append([planet, color])

#remove all planets from screen
def clear_screen():
    global planet_list
    global planet_count
    planet_list = []
    system.deleteBodies()
    planet_count = 0
    screen.fill((0, 0, 0))
    stop_simulation()

#starts simulation
def start_simulation():
    global running_simulation
    running_simulation = True

#pauses simulation
def stop_simulation():
    global running_simulation
    running_simulation = False

#used to find the users input for initial velocity
def get_initial_velocity(body, pos_x0, pos_y0, pos_xf, pos_yf):
    if show_trail.value == False:
        pg.draw.line(screen, (255, 255, 255), (pos_x0, pos_y0), (pos_xf, pos_yf), 5)
    dx = pos_xf - pos_x0
    dy = pos_yf - pos_y0
    v0_x = dx * t_const.getValue()
    v0_y = dy * t_const.getValue()
    body.set_velocity([-v0_x, -v0_y])
    return (v0_x, v0_y)


def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

#preset orbit
def scalene():
    clear_screen()
    mass=1
    x1 = 283
    x2 = 518
    x3 = 606
    y1 = 484
    y2 = 533
    y3 = 248
    system.deleteBodies()
    system.addBodies(planets.Planets(position=[x1 - (mass/2), y1 - (mass/2)], mass=mass, color=(255, 0, 0)))
    system.addBodies(planets.Planets(position=[x2 - (mass/2), y2 - (mass/2)], mass=mass, color=(255, 255, 0)))
    system.addBodies(planets.Planets(position=[x3 - (mass/2), y3 - (mass/2)], mass=mass, color=(0, 0, 255)))
    planet_list.append([pg.Rect(x1 - (mass/2), y1 - (mass/2), mass*10, mass*10), (255, 0, 0)])
    planet_list.append([pg.Rect(x2 - (mass/2), y2 - (mass/2), mass*10, mass*10), (255, 255, 0)])
    planet_list.append([pg.Rect(x3 - (mass/2), y3 - (mass/2), mass*10, mass*10), (0, 0, 255)])

#preset orbit
def trapezoid():
    clear_screen()
    mass = 1
    x1 = 250
    y1 = 250
    x2 = 650
    y2 = 250
    x3 = 250
    y3 = 650
    x4 = 650 * 0.7
    y4 = 650 * 0.8
    system.deleteBodies()
    system.addBodies(planets.Planets(position=[x1 - (mass/2), y1 - (mass/2)], mass=mass, color=(255, 0, 0)))
    system.addBodies(planets.Planets(position=[x2 - (mass/2), y2 - (mass/2)], mass=mass, color=(255, 255, 0)))
    system.addBodies(planets.Planets(position=[x3 - (mass/2), y3 - (mass/2)], mass=mass, color=(0, 0, 255)))
    system.addBodies(planets.Planets(position=[x4 - (mass/2), y4 - (mass/2)], mass=mass, color=(0, 255, 0)))
    planet_list.append([pg.Rect(x1 - (mass/2), y1 - (mass/2), mass*10, mass*10), (255, 0, 0)])
    planet_list.append([pg.Rect(x2 - (mass/2), y2 - (mass/2), mass*10, mass*10), (255, 255, 0)])
    planet_list.append([pg.Rect(x3 - (mass/2), y3 - (mass/2), mass*10, mass*10), (0, 0, 255)])
    planet_list.append([pg.Rect(x4 - (mass/2), y4 - (mass/2), mass*10, mass*10), (0, 255, 0)])

#preset orbit
def two_body_orbit():
    clear_screen()
    mass = 4
    x1 = 300
    y1 = 400
    x2 = 600
    y2 = 400

    system.deleteBodies()
    planet_list.clear()
    system.addBodies(planets.Planets(position=[x1 - (mass/2), y1 - (mass/2)], mass=mass, velocity=[0, 2], color=(255, 0, 0)))
    system.addBodies(planets.Planets(position=[x2 - (mass/2), y2 - (mass/2)], mass=mass, velocity=[0,-2], color=(255, 255, 0)))
    planet_list.append([pg.Rect(x1 - (mass/2), y1 - (mass/2), mass*10, mass*10), (255, 0, 0)])
    planet_list.append([pg.Rect(x2 - (mass/2), y2 - (mass/2), mass*10, mass*10), (255, 255, 0)])

#saves a system
def save_orbit():
    save_orbit_planet_list.clear()
    if len(planet_list) > 0:
        for planet in system.getBodies():
            save_orbit_planet_list.append(planet)
    print(len(save_orbit_planet_list))

#resets system to a saved var
def load_saved_orbit():
    print(len(save_orbit_planet_list))
    clear_screen()
    if len(save_orbit_planet_list) > 0:
        for planet in save_orbit_planet_list:
            create_planet(planet.get_position()[0], planet.get_position()[1])

#create controls
set_v0_to_0 = Toggle(screen, 925, 180, 50, 25)

#tail
show_trail = Toggle(screen, 925, 230, 50, 25)

#gravity
grav_const = TextBox(screen, 905, 300, 50, 50, fontSize=20)
grav_const.disable()
grav_slider = Slider(screen, 975, 320, 200, 25, min=1, max = 1000, step=10)

#start stop reset
start = Button(screen, 900, 0, 300, 50, text="Start", inactiveColour=(50, 200, 50), hoverColour=(50, 200, 50), onClick=lambda: start_simulation())
stop = Button(screen, 900, 50, 300, 50, text="Stop", inactiveColour=(255, 0, 0), hoverColour=(255, 0, 0), onClick=lambda: stop_simulation())
reset = Button(screen, 900, 100, 300, 50, text="Reset", inactiveColour=(150, 150, 150), hoverColour=(150, 150, 150), onClick=lambda: clear_screen())

#velocity
t_const = Slider(screen, 975, 420, 200, 25, min=0.01, max = 0.1, step=0.01, initial=0.05)
t_const_display = TextBox(screen, 905, 400, 50, 50, fontSize=20)

#time step
t_step = Slider(screen, 975, 520, 200, 25, min=.1, max = 5.0, step = 0.25, initial = 1)
t_step_display = TextBox(screen, 905, 500, 50, 50, fontSize=20)

#mass
mass_slider = Slider(screen, 975, 620, 200, 25, min=.5, max = 5.0, step = .5, initial = 1)

#preloaded systems
design_1 = Button(screen, 900, 670, 100, 50, text="Triangle", inactiveColour=(255, 255, 0), hoverColour=(255, 255, 0), fontSize=18, onClick=lambda: scalene())
design_2 = Button(screen, 1000, 670, 100, 50, text="Trapezoid", inactiveColour=(255, 0, 255), hoverColour=(255, 0, 255), fontSize=20, onClick=lambda: trapezoid())
design_3 = Button(screen, 1100, 670, 100, 50, text="Orbit", inactiveColour=(0, 255, 255), hoverColout=(0, 255, 255), fontSize=18, onClick=lambda: two_body_orbit())

#save and load designs
save_design = Button(screen, 900, 720, 300, 50, text="Save Orbit", inactiveColour=(200, 200, 255), hoverColour=(200, 200, 255), fontSize=18, onClick=lambda: save_orbit())
load_saved_design = Button(screen, 900, 770, 300, 50, text="Load Saved Orbit", inactiveColour=(200, 255, 200), hoverColour=(200, 255, 200), fontSize=18, onClick=lambda: load_saved_orbit())
frames = 0

#show center of mass
cm_value = Toggle(screen, 250,25, 50,25)

last_event_mouse_down = False

mass_list = []
while True:
    #check and update controls on right hand side
    if show_trail.value == False:
        screen.fill((0, 0, 0))

    clock.tick(60 / system.get_time_step())
    pg.draw.rect(screen, (255, 255, 255), [900, 0, 300, 900], 0) # change 4th num

    draw_text("Set v0 = 0", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 180)
    draw_text("Show Planet Trail", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 230)
    draw_text("Gravitational Constant ↓ ", pg.font.SysFont("Arial", 20), (0, 0, 0), 970, 280)
    grav_const.setText(grav_slider.getValue())
    system.set_g_constant(grav_slider.getValue())

    #stuff for time_step
    draw_text("Time Step ↓ ", pg.font.SysFont("Arial", 20), (0, 0, 0), 1020, 485)
    t_step_display.setText(round(t_step.getValue(), 2))
    system.set_time_step(round(t_step.getValue(), 2))

    #add mass for planets
    draw_text("Mass ↓", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 585)
    mass_slider_display = TextBox(screen, 905, 600, 50, 50, fontSize=20)
    mass_slider_display.setText(round(mass_slider.getValue(), 2))
    mass = mass_slider.getValue()

    #update time
    time_display = TextBox(screen, 10, 10, 150, 40, fontSize=20, colour=(0, 0, 0), textColour=(255, 255, 255))
    time_display.setText(f'Time: {int(round(system.get_time(), 0))}')


    frames += 1

    if set_v0_to_0.value == False:
        draw_text("Yeet Constant ↓ ", pg.font.SysFont("Arial", 20), (0, 0, 0), 1000, 380)
        t_const_display.setText(t_const.getValue())
    if frames < 150:
        draw_text("Click and drag to add planets and set v0.", pg.font.SysFont("Arial", 20), (255, 255, 255), 300, 50)
        draw_text("Magnitude of v0 is determined by distance dragged, not by speed dragged at.", pg.font.SysFont("Arial", 20), (255, 255, 255), 150, 100)

    events = pg.event.get()

    #check for events
    for event in events:

        #quit program
        if event.type == pg.QUIT:
            pg.quit()

        #add new planet
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos_x0, pos_y0 = pg.mouse.get_pos()
            last_event_mouse_down = False
            if pos_x0 < 900:
                create_planet(pos_x0, pos_y0)
                #pdate for last event was a mouse down
                last_event_mouse_down = True

        #check to add velocity
        elif event.type == pg.MOUSEBUTTONUP:
            pos_xf, pos_yf = pg.mouse.get_pos()
            if set_v0_to_0.value == False and len(system.getBodies()) > 0 and last_event_mouse_down:
                #if last event was mousedown, and all others fufilled, add velocity
                get_initial_velocity(system.getBodies()[-1], pos_x0, pos_y0, pos_xf, pos_yf)


    #start moving planets
    if running_simulation == True:

        if system.run():
            #check run if collision occurs. updates list if so
            temp_planet_lis = []
            for body in planet_list:
                for body2 in system.lisBodies:
                    if body[1] == body2.get_color():
                        temp_planet_lis.append([body2, body2.get_color()])
            #add new planet from collision
            planet_list = temp_planet_lis[:]
            color = (randint(100, 255), randint(100, 255), randint(100, 255))
            planet_list.append([system.lisBodies[-1], color])
            system.lisBodies[-1].set_color(color)



        #keep track of index
        integer = 0
        planet_list_math = system.getBodies()

        #update positions of planets
        for planet in planet_list_math: 
            planet_x = planet.get_position()[0]
            planet_y = planet.get_position()[1]
            temp = [pg.Rect(planet_x, planet_y, planet.get_mass() * 10, planet.get_mass() * 10), planet_list[integer][1]]
            planet_list[integer] = temp
            integer += 1

        #
        # print('///sys')
        # print(system.getBodies())
        # print('///planet')
        # print(planet_list)

    #redraw system
    for i in range(len(planet_list)):
        pg.draw.rect(screen, planet_list[i][1], planet_list[i][0], border_radius= int((system.getBodies()[i].get_mass() * 3) ** 2))
        if cm_value.value:
            pg.draw.rect(screen, (255,255,255), pg.Rect(system.getCOM()[0], system.getCOM()[1],5,5), border_radius = 3)

    pygame_widgets.update(events)
    pg.display.update()

