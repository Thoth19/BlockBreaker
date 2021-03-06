import pygame, os, math
class WallSprite(pygame.sprite.Sprite):
    ''' This class is a 16 by 16 blue block to serve as the border of game'''
    def __init__(self, position, orient):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([64,64])
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.orient = orient
        # x orient means you do not change x direction 
class BlockSprite(pygame.sprite.Sprite):
    ''' This class is the general block to break'''
    def __init__(self, position, color, points, orient):
        ''' position is a 2-tuple, color isa 3-tuple in RGB
        points is the value of destroying the block, integer. ''' 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([64,64])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.value = points
        self.orient = orient
        