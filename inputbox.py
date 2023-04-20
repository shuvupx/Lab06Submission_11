import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
class InputBox:
    def __init__(self, x, y, w, h, text='', f=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.f = f
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.f = self.text
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def pick(self):
        return self.f
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

font = pg.font.Font('freesansbold.ttf', 26)
text7 = font.render('Please enter number', True, (255,0,0))
class InputBox3:
    def __init__(self, x, y, w, h, text='', f='',error = ''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.f = f
        self.txt_surface = FONT.render(text, True, self.color)
        self.error = 0
        self.active = False
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.f = self.text
                    self.text = ''
                    if not self.f.isnumeric():
                        print('Not number')
                        self.error = 1
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
    def pick(self):
        if not self.f.isnumeric():
            self.f = '-'
        return self.f
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)
        if self.error == 1:
            screen.blit(text7, (300,300))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox3(100, 300, 140, 32) # สร้าง InputBox3
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True
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
    def __init__(self, x=0, y=0, w=0, h=0, r=0, g=0, b=0):
        Rectangle.__init__(self, x, y, w, h, r ,g ,b)
    
    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else:
            return False
        pass
btn1 = Button(540,340,170,120,255,0,0)
btn = Button(550,350,150,100,255,255,255)
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('Firstname', True, (0,0,153), (255,255,255)) # (text,is smooth?,letter color,background color)
text2 = font.render('Lastname', True, (0,0,153), (255,255,255))
text3 = font.render('Age', True, (0,0,153), (255,255,255))
text4 = font.render('Submit', True, (0,0,0))
mouse = ''
while run:
    screen.fill((255, 255, 255))
    text5 = font.render('Hello '+input_box1.pick() + ' ' +input_box2.pick() + '!', True, (0,0,0))
    text6 = font.render('You are '+input_box3.pick() + ' years old.', True, (0,0,0))
    if btn.isMouseOn() and pg.mouse.get_pressed()[0] == 1:
        btn.r = 255
        btn.g = 0
        btn.b = 0
        mouse = True
    else:
        btn.r = 255
        btn.g = 255
        btn.b = 255
    if mouse == True:
        screen.blit(text5, (400,100))
        screen.blit(text6, (400,150))
    btn1.draw(screen)
    btn.draw(screen)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    
    screen.blit(text, (100,68))
    screen.blit(text2, (100,168))
    screen.blit(text3, (100,265))
    screen.blit(text4, (568,385))
    pg.time.delay(1)
    pg.display.update()