import math, os, pygame
X_MAX = 1024
class PaddleSprite(pygame.sprite.Sprite):
    '''
    This is the user controlled paddle in a game of Pong
    '''
    def __init__(self, position, orient):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([128,16])
        self.rect = self.image.get_rect()
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.orient = orient
    def move(self, position):
        ''' moves to given position'''
        if position[0] + 128 > X_MAX:
            # The paddle itself is 128 pixels long
            self.rect.x = X_MAX -128
        else:
            self.rect.x = position[0]
    def update(self):
        '''
        Empty function so that all sprite groups can be updated
        '''
        pass
