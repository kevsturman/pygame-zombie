import pygame
import numpy as np
import itertools
pygame.init()
screen = pygame.display.set_mode((600, 400))
done = False
is_blue = True
rx = 40
x = 30
y = 30
bx = 0
power = 0
pt = 0
d = 3142
distance = 0
block = pygame.image.load('png/rectaplha.png')
block = pygame.transform.scale(block,(100,100))
grass = pygame.image.load('png/Tiles/2.png')
grass = pygame.transform.scale(grass, (32, 32))
soil = pygame.image.load('png/Tiles/5.png')
soil = pygame.transform.scale(soil, (32, 32))

bike = [pygame.image.load('png/bike/bike1.png'),
        pygame.image.load('png/bike/bike2.png'),
        pygame.image.load('png/bike/bike3.png'),
        pygame.image.load('png/bike/bike4.png'),
        pygame.image.load('png/bike/bike5.png'),
        pygame.image.load('png/bike/bike6.png'),
        pygame.image.load('png/bike/bike7.png'),
        pygame.image.load('png/bike/bike8.png')]

bush = [pygame.image.load('png/Object/Bush (1).png'),
        pygame.image.load('png/Object/Bush (2).png')]




def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)


def drawbike(x, y, rot):
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x + 90, y + 90, 40, 2))
    pygame.draw.line(screen, (255, 255, 255), (x + 90, y + 90), (x + 90 + 4, y + 90 - 20), 2)
    pygame.draw.line(screen, (255, 255, 255), (x + 130, y + 90), (x + 130 - 7, y + 90 - 30), 2)
    pygame.draw.line(screen, (255, 255, 255), (x + 90 + 4, y + 90 - 20), (x + 90, y + 90 - 24), 2)
    pygame.draw.line(screen, (255, 255, 255), (x + 90 + 4, y + 90 - 20), (x + 126, y + 90 - 20), 2)
    blitRotateCenter(screen, surf, (x + 60, y + 60), rot)
    blitRotateCenter(screen, surf, (x + 100, y + 60), rot)


def drawroad(x, y):
    for i in range(-2, 20):
        screen.blit(grass,(x+(i*32),205))
        #screen.blit(bush[0],(x+100,205))
        for y in range(1,6):
            screen.blit(soil,(x+(i*32),205+(y*32)))
    screen.blit(block,(200,240))


clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 40)

surf = pygame.Surface((60, 60), pygame.SRCALPHA)
pygame.draw.circle(surf, (100, 100, 100, 128), (30, 30), 15)
pygame.draw.rect(surf, (200, 200, 200, 128), pygame.Rect(23, 23, 5, 2))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        power = power + 0.08
    screen.fill((0, 150, 255))
    drawroad(rx,205)
    km = "{:.2f}".format(distance / 1000000)
    text = font.render(km + "km", True, (255, 255, 255))
    screen.blit(text, (20, 260))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    #drawbike(160, 100, x)
    screen.blit(bike[int(bx)],(160,150))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(0, 0, power * 20, 20))
    pygame.display.flip()
    pt = pt + 1
    if pt > 30:
        if power > 0:
            power = power - 0.1 * (power / 2)
        pt = 0
    x = x - int(power)
    if power > 0:
        rx = rx - 0.1 * power
        bx = bx + 0.005 * power
    if bx > 8:
        bx = 0
    if rx < 0:
        rx = 32
    if x < 0:
        x = 360
        distance = distance + d
