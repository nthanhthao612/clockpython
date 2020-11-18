import pygame

screen = pygame.display.set_mode((500,600))

STATUS = True
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREY = (150,0,0)
font = pygame.font.SysFont('Control Panel\All Control Panel Items\Fonts\Arial',50)
text_1 = font.render('+',True,BLACK)

while STATUS: 
    screen.fill(RED)
    #hàng 1
    pygame.draw.rect(screen,WHITE,(50,50,50,50))
    screen.blit(text_1,(50,50))
    pygame.draw.rect(screen,WHITE,(150,50,50,50))
    pygame.draw.rect(screen,WHITE,(250,50,100,50))
    #hàng 2
    pygame.draw.rect(screen,WHITE,(50,150,50,50))
    pygame.draw.rect(screen,WHITE,(150,150,50,50))
    pygame.draw.rect(screen,WHITE,(250,150,100,50))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STATUS = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('XXX')
    pygame.display.flip()
pygame.quit()