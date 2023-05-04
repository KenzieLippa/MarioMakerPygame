import pygame, sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *

#origin is vector everything is relative to (x,y) can run later on
#tiles are always relative to the origin
#only have to move one point, everything else follows
class Editor:
    def __init__(self) -> None:
        #main setup
        self.display_surface = pygame.display.get_surface()

        #navigation
        self.origin = vector()
        self.pan_active = False
        #get an offset
        self.pan_offset = vector() #will calc a vec between us and origin

#input
    def event_loop(self):
        #event loop 
        #close the game
        #dt = self.clock.tick() /1000 #set up the ticks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)

           # self.editor.run(dt)
            #pygame.display.update()
    def pan_input(self, event):
        #middle mouse button pressed / released (maybe do left click?)
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[2]:
            self.pan_active = True
            self.pan_offset = vector(mouse_pos()) - self.origin
            #gets distance between mouse and self origin
            print('right mouse')
        if not mouse_buttons()[2]:
            self.pan_active = False

        if event.type == pygame.MOUSEWHEEL:
            print(event.y) #is up and down movement 
            #gets all keys currently being pressed
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50

        #panning update
        if self.pan_active:
            self.origin = vector(mouse_pos()) - self.pan_offset

    #drawing 
    def draw_tile_lines(self):
        #draw lots of grid lines relative to the origin
        cols = WINDOW_WIDTH//TILE_SIZE #tile size has to stay at 64 with th ones we using
        rows = WINDOW_HEIGHT//TILE_SIZE
        origin_offset = vector(
            x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
            y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE
        )

        for col in range(cols):
            #x pos is harder
            #x pos is the same in both
            x = origin_offset.x + col *TILE_SIZE #will iterate through the columns and then draw the next one 64 tiles away
            pygame.draw.line(self.display_surface, LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

    def run(self, dt):
        
        self.event_loop() #call while we run

        #drawing
        self.display_surface.fill('white') # to tell if we are here
        self.draw_tile_lines()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)