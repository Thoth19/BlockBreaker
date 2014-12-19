import math, os, pygame, random
from wall import*
from paddle import*
from ball import*
score = 0 
lives  = 2
level = 0

# plan is to allow three instances of balls going off of the board. if a board is cleared 
# the player will get an extra life, and be moved to a new board. That can take place via command lines
# in order to give the player a break 

pygame.init()
while lives > 0:
    #Init
    level += 1
    lives += 1

    screen = pygame.display.set_mode([1024,768])
    clock = pygame.time.Clock()

    ball_group=pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    non_ball_sprites_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()

    p1 = PaddleSprite((512,768-64-32),(True, False))
    paddle_group.add(p1)
    all_sprites_group.add(p1)
    non_ball_sprites_group.add(p1)
    ball = BallSprite((400,320),(random.randint(-3,3),random.randint(1,3)))
    ball_group.add(ball)
    all_sprites_group.add(ball)
    for i in range(16):
        for j in range(12):
            if i == 0 or i == 15: 
                wall = WallSprite((i*64,j*64),(False,True))
            if j == 0 or j == 11:
                wall = WallSprite((i*64,j*64),(True, False))
            wall_group.add(wall)
            all_sprites_group.add(wall)
            non_ball_sprites_group.add(wall)

        #creates walls around the game board
    #each level gets more lucrative, and the colors should get more interesting
    for i in range(12):
        block1 = BlockSprite((i*64+128,2*64),(00,max(0,255-10*level),00),level * 3, (False, False))
        block2 = BlockSprite((i*64+128,3*64),(100,max(0,255-10*level),0),level * 2, (False, False))
        block3 = BlockSprite((i*64+128,4*64),(0,max(0,255-10*level),100),level * 1, (False, False))
        block_group.add(block1)
        block_group.add(block2)
        block_group.add(block3)
        all_sprites_group.add(block1)
        all_sprites_group.add(block2)
        all_sprites_group.add(block3)
        non_ball_sprites_group.add(block1)
        non_ball_sprites_group.add(block2)
        non_ball_sprites_group.add(block3)
    done = False #done with this game board
    while not(done) and lives >0:
        clock.tick(30)
        screen.fill((255,0,0))
        all_sprites_group.update()

        for event in pygame.event.get():
            if event.type != pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                p1.move(mouse_pos)

        #We have to check if the ball goes off screen, hits a block, hits a wall, or hits a paddle
        #Paddle code can come from pong
        #wall code probably needs fixing
        #off screen might break it as well because there will be a powerup that increases ball#

        if len(ball_group) == 0:
            lives -= 1
            ball = BallSprite((400,320),(random.randint(-3,3),random.randint(1,3)))
            ball_group.add(ball)
            all_sprites_group.add(ball)
            print "lives: ",lives
        for b in ball_group:
            if b.rect.y > p1.rect.y:
                #you can't catch it so delete it
                ball_group.remove(b)
                all_sprites_group.remove(b)
            else:
                # check collisions
                new_rect_x = b.rect
                new_rect_y = b.rect
                new_rect_x.x =new_rect_x.x+b.velocity[0]*b.vel_dir[0]
                new_rect_y.y =new_rect_y.y+b.velocity[1]*b.vel_dir[1]
                for p in non_ball_sprites_group:
                    if b.velocity[0] != 0:
                        if new_rect_x.colliderect(p.rect):
                            if not(p.orient[0]):
                                b.x_dir()
                            if p in block_group:
                                b.velocity = b.velocity[0],b.velocity[1]+random.randint(-1,1)
                                score += p.value * level
                                all_sprites_group.remove(p)
                                non_ball_sprites_group.remove(p)
                                block_group.remove(p)
                                if random.randint(0,level) == 0:
                                    ball = BallSprite((400,320),(random.randint(-3,3),random.randint(1,3)))
                                    ball_group.add(ball)
                                    all_sprites_group.add(ball)
                            b.velocity = b.velocity[0]+1,b.velocity[1]
                            
                    if b.velocity[1] != 0:
                        if new_rect_y.colliderect(p.rect):
                            if not(p.orient[1]):
                                b.y_dir()
                            if p in block_group:
                                b.velocity = b.velocity[0]+random.randint(-1,1),b.velocity[1]
                                score += p.value * level
                                all_sprites_group.remove(p)
                                non_ball_sprites_group.remove(p)
                                block_group.remove(p)
                            b.velocity = b.velocity[0],b.velocity[1]+1
                            
                if b.velocity[0] ==0:
                    b.velocity = random.randint(1,3),b.velocity[1]
                if b.velocity[1] ==0:
                    b.velocity = b.velocity[0],random.randint(1,3)
            #print b.rect.x, b.rect.y

        if len(block_group) == 0:
            done = True
            score += 10*level

        all_sprites_group.draw(screen)
        pygame.display.flip()
    pygame.display.quit()
    if lives >0:
        print "Good Job! You beat stage %d." %level
        print "Your score is %d" %score
        print "You still have %d lives left. Plues you get a free one for beating the level" %lives
        x = raw_input("Enter anything to continue: ")
print "Well you finally lost with a final score of %d" %score
print "And you made it to level %d" %level