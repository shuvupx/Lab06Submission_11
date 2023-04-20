class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.r = r
        self.g = g
        self.b = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else:
            return False
        pass
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn():
        btn.r = 128
        btn.g = 128
        btn.b = 128
    else:
        btn.r = 255
        btn.g = 0
        btn.b = 0
    if btn.isMouseOn() and pg.mouse.get_pressed()[0] == 1:
        btn.r = 205
        btn.g = 0
        btn.b = 255
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.KEYDOWN and event.key == pg.K_w: 
            btn.y -= 10
        elif event.type == pg.KEYDOWN and event.key == pg.K_s: 
            btn.y += 10
        elif event.type == pg.KEYDOWN and event.key == pg.K_a: 
            btn.x -= 10
        elif event.type == pg.KEYDOWN and event.key == pg.K_d: 
            btn.x += 10     