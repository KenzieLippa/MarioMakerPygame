import pygame
from settings import *
from pygame.image import load

class Menu:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        #needs to be first
        self.create_data()
        self.create_buttons()

    def create_data(self):
        self.menu_surfs = {}
        for key, value in EDITOR_DATA.items():
            #only need if theres a menu surface
            if value['menu']:
                #if there is a value key menu
                if not value['menu'] in self.menu_surfs:
                    #if not in dict then add
                    self.menu_surfs[value['menu']] = [(key, load(value['menu_surf']))]
                else:
                    self.menu_surfs[value['menu']].append((key, load(value['menu_surf'])))
        #print(self.menu_surfs)

            # print(key)
            # print(value)

    def create_buttons(self):

        #menu area general
        size = 180
        margin = 6
        topleft = (WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin)
        #make the rect size with the size var, then the margin is the space
        #between the box and th margin
        self.rect = pygame.Rect(topleft, (size, size))

        #button areas
        #we want 4 button rectangles
        generic_button_rect = pygame.Rect(self.rect.topleft, (self.rect.width/2, self.rect.height/ 2)) #need a rect 1/4 th size of th box
        button_margin = 5
        self.tile_button_rect = generic_button_rect.copy().inflate(-button_margin, -button_margin)
        self.coin_button_rect = generic_button_rect.move(self.rect.height /2, 0).inflate(-button_margin, -button_margin)
        self.enemy_button_rect = generic_button_rect.move(self.rect.height /2, self.rect.width/2).inflate(-button_margin, -button_margin)
        self.palm_button_rect = generic_button_rect.move(0, self.rect.width/ 2).inflate(-button_margin, -button_margin)

        #create the buttons
        self.buttons = pygame.sprite.Group()
        Button(self.tile_button_rect, self.buttons, self.menu_surfs['terrain'])
        Button(self.coin_button_rect, self.buttons, self.menu_surfs['coin'])
        Button(self.enemy_button_rect, self.buttons, self.menu_surfs['enemy'])
        Button(self.palm_button_rect, self.buttons, self.menu_surfs['palm fg'], self.menu_surfs['palm bg'])

    def click(self, mouse_pos, mouse_button):
        for sprite in self.buttons:
            if sprite.rect.collidepoint(mouse_pos):
                if mouse_button[0] and pygame.key.get_pressed()[pygame.K_LALT]:
                    #toggle but if it has no alt then will always be true
                    sprite.main_active = not sprite.main_active if sprite.items['alt'] else True #but only if has alt sprites
                if mouse_button[2]: #if right click want to select
                    pass
                return sprite.get_id() #return what the id is

    def display(self):
        #pygame.draw.rect(self.display_surface, 'red', self.rect)
        # pygame.draw.rect(self.display_surface, 'green', self.tile_button_rect)
        # pygame.draw.rect(self.display_surface, 'blue', self.coin_button_rect)
        # pygame.draw.rect(self.display_surface, 'yellow', self.palm_button_rect)
        # pygame.draw.rect(self.display_surface, 'purple', self.enemy_button_rect)
        self.buttons.update()
        self.buttons.draw(self.display_surface)

class Button(pygame.sprite.Sprite):
    #inherits from the sprite class
    def __init__(self, rect, group, items, items_alt = None):
        #some buttons have alt items
        super().__init__(group) #for inheritance reasons
        self.image = pygame.Surface(rect.size)
        self.rect = rect
        #items
        self.items = {'main': items, 'alt': items_alt}
        self.index = 0 #which item we are on
        self.main_active = True
        #will need to import a bunch of shit

    def get_id(self):
        #getting a key
        return self.items['main' if self.main_active else 'alt'][self.index][0] #either selection items or alt
    
    def update(self):
        self.image.fill(BUTTON_BG_COLOR)
        #from items or other items
        surf = self.items['main' if self.main_active else 'alt'][self.index][1] #only pick th graphic
        #returns a touple with index of the graphic and then the graphic
        #print(surf)
        #using local instead of global to setup the rect
        rect  = surf.get_rect(center = (self.rect.width/2, self.rect.height/2) ) # dont use self.rect.center
        #want to go half the width and half the width of the center
        #would get the global instead which wont work because of the shrink
        self.image.blit(surf, rect)


