import pygame
from pygame.constants import*
pygame.init()
W,H=(1000,700)
h=500
win=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()
img=pygame.image.load("main.jpeg")
edited_img=pygame.image.load("edited.jpeg")
r_h=img.get_height()
if r_h>h:
    r_w=h*(img.get_width())//r_h
    r_h=h
img=pygame.transform.scale(img,(r_w,r_h))
edited_img=pygame.transform.scale(edited_img,(r_w,r_h))

class Slider:
    def __init__(self,x,height,speed,m_x):
        self.x=x
        self.height=height
        self.speed=speed
        self.m_x=m_x
    
    def draw(self,win,color):
        pygame.draw.line(win,color,(self.x,350-self.height//2),(self.x,350+self.height//2),4)

    def move(self):
        if self.x<self.m_x:
            self.x+=self.speed
    
    def blit_images(self,o_x):
        cropped_region = (0, 0, self.x-o_x, r_h)
        win.blit(edited_img, (500-r_w//2,350-r_h//2), cropped_region)


def redrawwin():
    win.fill((255,255,255))
    pygame.draw.rect(win,(255,0,0),(500-r_w//2,350-r_h//2,r_w+10,510),)
    pygame.draw.rect(win,(0,0,255),(490-r_w//2,340-r_h//2,r_w+10,510),)
    win.blit(img,(500-r_w//2,350-r_h//2))
    slider.blit_images(500-r_w//2)
    # win.blit(img,(500-r_w//2,350-r_h//2))
    slider.draw(win,(0,0,0))
    slider.move()
    pygame.display.flip()

slider=Slider(500-r_w//2,h+50,2,500+r_w//2)
while 1:
    clock.tick(40)
    redrawwin()
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()