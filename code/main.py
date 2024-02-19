import pygame
from pygame.image import load
from settings import *
from editor import Editor

class Main:
    def __init__(self):
        
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #will be set up in the settings prob
        self.clock = pygame.time.Clock()

        #made as a property
        #needs its own event loop, need to check keyboard input for both, have also a third event loop from main
        #so we not gonna do a main loop, only have one open at the same time
        self.editor = Editor() #makes a new instance thingy

        #need a cursor
        surf = load('graphics/cursors/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0,0),surf) #first arg is clickable area, origin
        pygame.mouse.set_cursor(cursor)
    alphabet = {
    "a":{
        "s":{
            "s": "ass"
        }
    }
}
    print(alphabet["a"]["s"]["s"])

#we have a main and then we need a editor mode and a level mode
#need to figure out how to switch between them
#this runs the file
    def run(self):
        while True:
            dt = self.clock.tick() /1000 #set up the ticks
            self.editor.run(dt)
            pygame.display.update()




if __name__ == '__main__':
    #set main equal to new instance of class main
    main = Main()
    main.run() #run main