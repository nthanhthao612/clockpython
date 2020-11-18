import pygame
from pygame.constants import QUIT
#khai báo biến màn hình pygame.display.set_mode((chiều rồng, chiều dài))
screen = pygame.display.set_mode((500,600))
STATUS = True
RED = (255,0,0)
WHITE = (255,255,255)
while STATUS == True:
    screen.fill(RED)
    #vẽ hình chữ nhật với cấu trúc
    #pygame.draw.rect(biến màn hình,Màu sắc,(vị trí,vị trí,chiều rộng,chiều dài))
    pygame.draw.rect(screen,WHITE,(50,50,50,50))
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            STATUS = False
    pygame.display.flip()
pygame.quit()