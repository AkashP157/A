import pygame
import time
import random

pygame.init()

display_width = 500
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

shipwidth = 73
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Shoot Them')
clock = pygame.time.Clock()
i = 0
ship_img = pygame.image.load('3.png')

def blocks(blockx,blocky,blockw,blockh,color):
    pygame.draw.rect(gameDisplay,color , [blockx,blocky,blockw,blockh])

def ship(x,y):
    gameDisplay.blit(ship_img,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
  
def crash():
    message_display('you crashed')
    

def game_loop():
    
    x = (display_width * 0.45)
    y = (display_height*0.8)
    x_change = 0
    block_startx = random.randrange(0,display_width)
    block_starty = -600
    block_speed = 7
    block_width = 100
    block_height = 100

    gameExit = False
    timing = 0


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x+=x_change
        gameDisplay.fill(white)
        blocks(block_startx,block_starty,block_width,block_height,black)
        
        block_starty += block_speed
        ship(x,y)

        if x > display_width - shipwidth or x < 0:
            crash()
        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0,display_width)
        if y < block_starty + block_height:
            
            if x > block_startx and x < block_startx + block_width or x+shipwidth > block_startx and x + shipwidth < block_startx+block_width:
                
                crash()
                
                
                           
        timing = timing + 1
        
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
                
        
                
                    
    
