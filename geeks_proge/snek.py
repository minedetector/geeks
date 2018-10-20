import sys, pygame
import time
from pygame.locals import*
import random


pygame.init()
#pygame initalize aka algab

font = pygame.font.SysFont(None, 25)


def snake(block, snakelist):
    for xny in snakelist:
        pygame.draw.rect(screen, black, [xny[0], xny[1], block, block])


def text_obj(text, color):
    textsurf = font.render(text, True, color)
    return textsurf, textsurf.get_rect()

def message(msg,color):
    textsurf, textrect = text_obj(msg, color)
    textrect.center = (width/2), (height/2)
    screen.blit(textsurf, textrect)


black = 0,0,0
white = 255,255,255
red = 255,0,0

width= 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("sneak")



clock = pygame.time.Clock()

block = 20
FPS = 30


def gameloop():
    gameexit = False
    gameover = False

    lead_x = width/2
    lead_y = height/2

    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakelength = 1

    x_way = 0
    y_way = 0

    randapplex = round(random.randrange(0, width-block)/10.0)*10.0
    randappley = round(random.randrange(0, height-block)/10.0)*10.0
    
    while not gameexit:

        while gameover:
            screen.fill(white)
            message("game over, press c to play again or q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                gameexit=True
            #  tuvastab sündmuse
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and x_way != 1:
                    lead_x_change = -block
                    lead_y_change = 0
                    x_way = -1
                    y_way = 0
                    #  kindel sündmus
                elif event.key == pygame.K_RIGHT and x_way != -1:
                    lead_x_change = block
                    lead_y_change = 0
                    x_way = 1
                    y_way = 0
                elif event.key == pygame.K_UP and y_way != -1:
                    lead_y_change = -block
                    lead_x_change = 0
                    y_way = 1
                    x_way = 0
                elif event.key == pygame.K_DOWN and y_way != 1:
                    lead_y_change = block
                    lead_x_change = 0
                    y_way = -1
                    x_way = 0
                    """
            #Kui klahv tõstetakse ülesse
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = 0   
                if event.key == pygame.K_UP:
                    lead_y_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = 0
            """
        if lead_x > width or lead_x< 0 or lead_y > height or lead_y< 20:
            gameover = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        screen.fill(white)

        apple = 30
        pygame.draw.rect(screen, red,[randapplex,randappley,apple,apple])

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover = True
            
            
        snake(block, snakelist)
        
        pygame.display.update()
        #uuendab programmi, sulgudesse saab panna ka kindlaid asju mida uuendada
        #kui sulud on tühjad uuendab kõike

#        if lead_x == randapplex and lead_y == randappley:
 #           randapplex = round(random.randrange(0, width-block)/10.0)*10.0
  #          randappley = round(random.randrange(0, height-block)/10.0)*10.0
   #         snakelength += 1

        if lead_x > randapplex and lead_x < randapplex+ apple or lead_x + block > randapplex and lead_x + block < randapplex + apple:
            if lead_y >randappley and lead_y < randappley + apple or lead_y + block > randappley and lead_y + block < randappley + apple:
                randapplex = round(random.randrange(0, width-block)/10.0)*10.0
                randappley = round(random.randrange(0, height-block)/10.0)*10.0
                snakelength += 1
            

        clock.tick(FPS)

    pygame.quit()
    quit()

gameloop()
