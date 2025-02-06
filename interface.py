import pygame as pg
import pygamepal as pgp

pg.init()
screen = pg.display.set_mode() 
screen_x, screen_y = 1200, 800
screen = pg.display.set_mode((screen_x, screen_y))
clock = pg.time.Clock()

while True:
    screen.fill((0, 0, 0))
    clock.tick(24)
    events = pg.event.get()
    pg.draw.rect(screen, (255, 255, 255), [900, 0, 300, 300], 0)

    start = pgp.Button(input = input, position = (900, 0), text = "Start", backgroundColor="green")
    stop = pgp.Button(input = input, position = (1000, 0), text = "Stop", backgroundColor="red")
    reset = pgp.Button(input = input, position = (1100, 0), text = "Reset", backgroundColor="gray")

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()

    start.draw(screen)
    stop.draw(screen)
    reset.draw(screen)

    pg.display.update()