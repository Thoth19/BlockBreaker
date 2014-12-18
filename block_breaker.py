import math, os, pygame, random
from wall import*
from paddle import*
from ball import*

lives  = 3
level = 1
# plan is to allow three instances of balls going off of the board. if a board is cleared 
# the player will get an extra life, and be moved to a new board. That can take place via command lines
# in order to give the player a break 
while lives > 0:
    #Init

    pygame.init()
    screen = pygame.display.set_mode([1024,768])
    clock = pygame.time.Clock()

    ball_group=pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()

    p1 = PaddleSprite((512,768-64-32))
    paddle_group.add(p1)
    all_sprites_group.add(p1)
    ball = BallSprite((400,320),(random.randint(-3,3),random.randint(1,3)))
    ball_group.add(ball)
    all_sprites_group.add(ball)
    for i in range(16):
        for j in range(12):
            if i == 0 or i == 15 or j == 0 or j == 11:
                wall = WallSprite((i*64,j*64))
                wall_group.add(wall)
                all_sprites_group.add(wall)
        #creates walls around the game board
    #each level gets more lucrative, and the colors should get more interesting
    for i in range(12):
        block1 = BlockSprite((i*64+128,2*64),(00,255,00),level * 3)
        block2= BlockSprite((i*64+128,3*64),(100,255,0),level * 2)
        block3 = BlockSprite((i*64+128,4*64),(0,255,100),level * 1)
        block_group.add(block1)
        block_group.add(block2)
        block_group.add(block3)
        all_sprites_group.add(block1)
        all_sprites_group.add(block2)
        all_sprites_group.add(block3)
    done = False #done with this game board
    while not(done):
        clock.tick(60)
        screen.fill((255,0,0))
        all_sprites_group.update()
        all_sprites_group.draw(screen)
        
        pygame.display.flip()
