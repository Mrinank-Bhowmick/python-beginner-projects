#A program to calculate the value of pi using buffons needle problem
import pygame
from math import pi,sin,cos
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
green=(0,255,0)

font = pygame.font.Font(None, 32)

t=60
l=47
n=6

root=pygame.display.set_mode((n*t,n*t+32))
# root=pygame.display.set_mode((n*t,n*t))
pygame.display.set_caption("Buffon's Needle Problem")
clock=pygame.time.Clock()

intersected=0
lines=0

done=False

root.fill(white)
while not done:
    for i in range(n):
        pygame.draw.line(root,black,(i*t,0),(i*t,n*t),2)

    x=(random.randrange(0,n*t))
    y=(random.randrange(0,n*t))
    theta=random.uniform(0,pi)

    is_intersecting=False
    p=x//t
    if theta<(pi/2):
        if (x+l*cos(theta))>=(p+1)*t:
            is_intersecting=True
    else:
        if (x+l*cos(theta))<=p*t:
            is_intersecting=True

    if is_intersecting:
        pygame.draw.line(root,green,(x,y),(x+l*cos(theta),y+l*sin(theta)),2)
        intersected+=1
    else:
        pygame.draw.line(root,black,(x,y),(x+l*cos(theta),y+l*sin(theta)))

    lines+=1

    pygame.draw.rect(root,black,pygame.Rect(0,n*t,n*t,n*t))

    try:
        text=font.render(f"{str((2/(intersected/lines))*(l/t))[0:4]}",True,white)
        root.blit(text,(0,n*t))
        print(f"{(2/(intersected/lines))*(l/t)}",end="\r")
    except ZeroDivisionError:
        pass

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                done=True

    pygame.display.update()

