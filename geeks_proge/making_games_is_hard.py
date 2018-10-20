__author__ = 'markus.tiigimäe'
import pygame, sys
from random import randint

HEIGHT = 600
WIDTH=800
x=400
y=randint(0,600)
x_speed=0
y_speed=0


pygame.init()
screen=pygame.display.set_mode([WIDTH,HEIGHT])
clock=pygame.time.Clock()
pygame.key.set_repeat(1,10)


class Ball():

    def __init__(self,x=0,y=0,r=10):
        self.x=x
        self.y=y
        self.r=10
        self.xspeed = randint(-3,3)
        self.yspeed = randint(-3,3)

    def step(self,player1,player2):
        self.x += self.xspeed
        if self.x < 0+self.r:
            self.x= 0+self.r
            self.xspeed *= -1
        elif self.x > WIDTH-self.r:
            self.x = WIDTH-self.r
            self.x = 400
        elif self.x == self.r:
            self.x=400
        self.y += self.yspeed
        if self.y < 0+self.r :
            self.y = 0+self.r
            self.yspeed *= -1
        elif self.y> HEIGHT-self.r :
            self.y=HEIGHT-self.r
            self.yspeed *=-1

    def draw(self,surface):
        pygame.draw.circle(surface,[255,255,255],[self.x,self.y],self.r,0)


class Player():
    def __init__(self,x,whichPlayer):

        self.y=HEIGHT//2
        self.whichPlayer=playerNumber
        self.x=x

    def draw(self,surface):
        pygame.draw.rect(screen,[255,255,255],[self.x-5,self.y-WIDTH//2],10,40,0)

    def setCoordinate(self,y):
        self.y =y




ball= Ball(400,randint(0,600),10)
#player1=Player(10,LEFTPLAYER)
#player2=Player(WIDTH-10,RIGHTPLAYER)


is_running = True # Muutuja "running" väärtustamine
while is_running :
    screen.fill([0,0,0])
"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            is_running = False
        if e.type == pygame.MOUSEMOTION:
            x,y=e.pos
            player1.setCoordinate(y)
        elif e.type == pygame.KEYDOWN():
            if e.key==pygame.K_DOWN:
                player2.setCoordinate(player2.y+10)
            if e.key==pygame.K_UP:
                player2.setCoordinate(player2.y-10)
"""
ball.step()
ball.draw(screen)
player1.draw(screen)
player2.draw(screen)
pygame.display.flip()
clock.tick(60)
pygame.quit()