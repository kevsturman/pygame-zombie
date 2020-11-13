import pygame
import random

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

def create_world():
    world = [[0] * w for i in range(h)]
    # Set Value at 1,1
    for i in range(0,len(world[7])):
        world[9][i] = 1
        for y in range(10,14):
            world[y][i] = 2
    return world

def random_bush(world):
    w = len(world[0])-20
    x = random.randint(20,w-1)
    if world[8][x] == 0 and world[8][x+1] == 0:
        world[8][x] = 4
        world[8][x+1] = 3
    return world

def random_cloud(world):
    y = random.randint(0,4)
    w = len(world[0])-20
    x = random.randint(20,w-1)
    if world[y][x] == 0 and world[y][x+1] == 0:
        world[y][x] = random.randint(5,6)
    return world

if __name__ == "__main__":
    w = 100
    wx = 0
    h = 14
    bx = 0
    by = 0
    timer = 0
    r = 0
    spd_min = 1  # set min speed
    spd_max = 30 # set max speed
    spd_up_acc = 0.1
    spd_down_acc = 0.08
    spd = spd_min
    
    
    # Create 2d List
    world = create_world()
    for i in range(0,5):
        world = random_bush(world)
        world = random_cloud(world)
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    font = pygame.font.SysFont("monospace", 20)
    done = False
    tiles = [pygame.transform.scale(pygame.image.load('png/Tiles/2.png'), (32, 32)),
             pygame.transform.scale(pygame.image.load('png/Tiles/5.png'), (32, 32)),
             pygame.transform.scale(pygame.image.load('png/Tiles/19.png'), (32, 32)),
             pygame.transform.scale(pygame.image.load('png/Tiles/20.png'), (32, 32)),
             pygame.image.load('png/Tiles/21.png'),
             pygame.image.load('png/Tiles/22.png')]
    bike = [pygame.image.load('png/bike/bike1.png'),
            pygame.image.load('png/bike/bike2.png'),
            pygame.image.load('png/bike/bike3.png'),
            pygame.image.load('png/bike/bike4.png'),
            pygame.image.load('png/bike/bike5.png'),
            pygame.image.load('png/bike/bike6.png'),
            pygame.image.load('png/bike/bike7.png'),
            pygame.image.load('png/bike/bike8.png')]
    x = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            r = r + 1
        screen.fill((0,150,255))
        
        if keys[pygame.K_RIGHT]:
            if spd + spd_up_acc <= spd_max:
                spd = spd + spd_up_acc
            else:
                spd = spd_max
        
        if keys[pygame.K_LEFT]:
            if spd - spd_down_acc >= spd_min:
                spd = spd - spd_down_acc
            else:
                spd = spd_min

        for vy in range(0,14):
            for vx in range(0,20):
                if world[vy][vx+wx] != 0:
                    text = font.render(str(world[vy][vx+wx]),True,(255,255,255))
                    screen.blit(tiles[world[vy][vx+wx]-1], (x + (vx * 32), vy * 32))
                    #screen.blit(text,(x + (vx * 32), vy * 32))
        # for wy,row in enumerate(world):
        #     for wx,col in enumerate(row):
        #         if col is not 0:
        #             screen.blit(tiles[col-1],(x+(wx*32),wy*32))
        #         text = font.render(str(col), True, (255, 255, 255))
        #         screen.blit(text,(x+(wx*32),wy*32))
        #rbike = pygame.transform.rotate(bike[bx],r)
        #screen.blit(rbike,(180,167-by))
        blitRotateCenter(screen,bike[bx],(230,230),r)
        pygame.display.flip()
        x = x - int(spd)
        if x < -32:
            x = 0
            wx = wx + 1
        if wx > 80:
            wx = 0
            world = create_world()
            for i in range(0, random.randint(1,10)):
                world = random_bush(world)
            for i in range(0,4):
                world = random_cloud(world)
        timer = timer + 1
        if timer > 20:
            bx = bx + 1
            timer = 0
        if bx > 7:
            bx = 0
        if r > 360:
            r = 0
