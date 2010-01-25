import pygame

pygame.init()

class EventGenerator:
    def __init__(self):
        pass

    def run(self):
        pygame.event.post(pygame.event.Event(42, {"test number" : 10}))



eg = EventGenerator()

while 1:
    for event in pygame.event.get():
        print event.type, pygame.event.event_name(event.type)
        eg.run()

