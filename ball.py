#This file contains the ball class which will hold the data on the ball in pong
import os, pygame
from math import *
MAX_SPEED = 5
class BallSprite(pygame.sprite.Sprite):
    ''' Is the ball in a game of Pong '''
    # GRAVITY = -0.5
    def __init__(self,position, velocity):
        ''' This funcion takes position and velocity as tuples. of the form x,y '''
        pygame.sprite.Sprite.__init__(self)
        # self.src_image = pygame.image.load(os.path.join("pics","ball.jpg")).convert()
        self.image = pygame.Surface([16,16])
        self.image.fill((0,0,0))
        # self.image.set_colorkey((0,0,0))
        # pygame.draw.circle(self.image,(0,255,0), position, 8)
        # Unclear why making it a circle doesn't work. 
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velocity = abs(velocity[0]),abs(velocity[1])
        # velocity is actually speed
        self.vel_dir = copysign(1,velocity[0]),copysign(1,velocity[1])
    def reset(self, position, velocity):
        '''
        resets the ball to position
        '''
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velocity = abs(velocity[0]),abs(velocity[1])
        self.vel_dir = copysign(1,velocity[0]),copysign(1,velocity[1])
    def update(self):
        '''
        moves ball based on velocity and keeps velocity below maximum
        '''
        self.velocity = min(self.velocity[0],MAX_SPEED),min(self.velocity[1],MAX_SPEED)
        # velocity cannot go above maximum
        self.rect.x += self.velocity[0] * self.vel_dir[0]
        self.rect.y += self.velocity[1] * self.vel_dir[1]
    def x_dir(self):
        '''
        Changes direction of x velocity
        '''
        self.vel_dir = self.vel_dir[0] * -1, self.vel_dir[1]
        self.velocity = self.velocity[0] + 1, self.velocity[1]
    def y_dir(self):
        '''
        Changes direction of y velocity
        '''
        self.vel_dir = self.vel_dir[0], self.vel_dir[1] * -1
        self.velocity = self.velocity[0], self.velocity[1] + 1

