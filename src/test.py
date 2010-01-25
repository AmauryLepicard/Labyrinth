import pygame, sys, random

pygame.init()

class EventGenerator:
    def __init__(self):
        pass

    def run(self):
        if random.random() > 0.999:
            print "creating and sending event"
            pygame.event.post(pygame.event.Event(42, {"test number" : 10}))


size = 200, 200
screen = pygame.display.set_mode(size)

eg = EventGenerator()

while 1:
    for event in pygame.event.get():
        print event.type, pygame.event.event_name(event.type)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    print "exiting..."
                    sys.exit()
    eg.run()
    pygame.display.flip()

