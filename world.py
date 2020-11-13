import pygame
import random

def blitRotateCenter(surf, image, topleft, angle):
	# take sprite and blit it to surface at the centre with given rotation
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

def create_world():
	# create empty 2d world. 0 is sky; 1 is grass; 3 is soil
    world = [[0] * width for i in range(height)]
    for i in range(0,len(world[7])):
        world[9][i] = 1
        for y in range(10,14):
            world[y][i] = 2
    return world

def random_bush(world):
	# add random bush to world
    w = len(world[0])-20
    x = random.randint(20,w-1)
    if world[8][x] == 0 and world[8][x+1] == 0:
        world[8][x] = 4
        world[8][x+1] = 3
    return world

def random_cloud(world):
	# add random cloud to world
    y = random.randint(0,4)
    w = len(world[0])-20
    x = random.randint(20,w-1)
    if world[y][x] == 0 and world[y][x+1] == 0:
        world[y][x] = random.randint(5,6)
    return world

if __name__ == "__main__":
	# Initialise Defaults
    width = 100 # width of the world in 8x8 squares
    height = 14 # height of the world
    world_x = 0 # current world x offset
    bike_frame = 0 
    bike_y = 0
    timer = 0
    rotation = 0
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
    
    # Game Loop Starts
    while not done:
		
		# check pygame events for keypress events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if window closes, exit game
                done = True
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            rotation = rotation + 1 # rotate is space is pressed
        
        screen.fill((0,150,255)) # clear screen and fill it with a blue colour 0,150,255
		
		# draw tiles to the world
        for vy in range(0,14):
            for vx in range(0,20):
                if world[vy][vx+world_x] != 0:
                    text = font.render(str(world[vy][vx+world_x]),True,(255,255,255))
                    screen.blit(tiles[world[vy][vx+world_x]-1], (x + (vx * 32), vy * 32))

        blitRotateCenter(screen,bike[bike_frame],(230,230),rotation)
        pygame.display.flip()
        x = x - 1
        
        if x < -32: # after 32 frames move the world 1 pixel forward
            x = 0
            world_x = world_x + 1
        
        # when world gets near the end. Reset to the start. Create a new world with random bushes
        if world_x > 80: 
            world_x = 0
            world = create_world()
            for i in range(0, random.randint(1,10)):
                world = random_bush(world)
            for i in range(0,4):
                world = random_cloud(world)
        
        timer = timer + 1
        if timer > 20:
            bike_frame = bike_frame + 1
            timer = 0
        if bike_frame > 7:
            bike_frame = 0
        if rotation > 360:
            rotation = 0
