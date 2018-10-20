import sys, pygame

import random
import time

pygame.init()

font = pygame.font.SysFont(None, 25)

def message(msg,color):
    
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text,[width/2-100, height/2])


black = 0,0,0

white = 255,255,255

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ping pong")

ball = 10

clock = pygame.time.Clock()
FPS = 60


def gameloop():
    gameexit = False
    gameover = False

    rackety_1 = height/2
    rackety_2 = height/2
    
    racketx_1 = 0
    racketx_2 = width-ball

    x_ball = width/2
    y_ball = height/2

    ball_loc = [0, 0]
    r1_loc = [0, 0]
    r2_loc = [0, 0]
    
    y_change = 0
    y_change2 = 0
    
    r_movement = 10
    r_size = 100

    movement = [-5, 5, -3, 3]

    x = random.choice(movement)
    y = random.choice(movement)

    while not gameexit:

        while gameover:
            
            message("game over, press c to play again or q to quit", white)
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
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    y_change = r_movement
                if event.key == pygame.K_DOWN:
                    y_change2 = r_movement
                if event.key == pygame.K_w:
                    y_change = -r_movement
                if event.key == pygame.K_UP:
                    y_change2 = -r_movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    y_change2 = 0
                if event.key == pygame.K_w:
                    y_change = 0
                if event.key == pygame.K_UP:
                    y_change2 = 0
        #pall
        pygame.draw.rect(screen, white,[x_ball,y_ball,ball,ball])
        #L_racket
        pygame.draw.rect(screen, white,[racketx_1,rackety_1,ball,r_size])
        #R_racket
        pygame.draw.rect(screen, white,[racketx_2,rackety_2,ball,r_size])

        pygame.display.update()
        screen.fill(black)

        x_ball += x
        y_ball += y

        rackety_1 += y_change
        rackety_2 += y_change2
        if rackety_1 < 0 or rackety_1 > 500:
            y_change = 0
        if rackety_2 < 0 or rackety_2 > 500:
            y_change2 = 0
        ball_loc[:] = []
        
        ball_loc.insert(0, x_ball)
        ball_loc.insert(1, y_ball)

        r1_loc[:] = []

        r1_loc.insert(0, racketx_1)
        r1_loc.insert(1, rackety_1)

        r2_loc[:] = []
        
        r2_loc.insert(0, racketx_2)
        r2_loc.insert(1, rackety_2)

        if y_ball >= height-10 or y_ball <= 10:
            y = y*(-1)

        if r1_loc[0]-3 <= ball_loc[0] <= r1_loc[0]+3:
            if r1_loc[1] - r_size <= ball_loc[1] <= r1_loc[1] + r_size:
                x = x*-1
        if r2_loc[0]-3 <= ball_loc[0] <= r2_loc[0]+3:
            if r2_loc[1] - r_size <= ball_loc[1] <= r2_loc[1] + r_size:
                x = x*-1
        elif x_ball < 0 or x_ball>width:
            print(ball_loc," palli loc")
            print(r1_loc, "paddle 1 loc")
            print(r2_loc, "paddle 2 loc")
            gameover = True
            
        clock.tick(60)
            
    pygame.quit()
    quit()
    
gameloop()                    
