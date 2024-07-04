import pygame
import sys
import random
import asyncio

pygame.init()
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

class Banana:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed 

    def move(self):
        self.rect.y += self.speed


# variables
speed = 3
score = 0
seconds = score//60

# constants
TILESIZE = 32
# floor
floor_image = pygame.image.load('DropDash-main/assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE*15, TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))

# player
player_image = pygame.image.load('DropDash-main/assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE*3, TILESIZE*3))
player_rect = player_image.get_rect(center = (screen.get_width()/2, 
                                              screen.get_height()-floor_image.get_height()-(player_image.get_height()/2)) )

# banana
banana_image = pygame.image.load('DropDash-main/assets/banana.png').convert_alpha()
banana_image = pygame.transform.scale(banana_image, (TILESIZE, TILESIZE))

bananas = [
    Banana(banana_image, (100, 0), 3),
    Banana(banana_image, (300, 0), 3),
]
# fonts
font = pygame.font.Font('DropDash-main/assets/PixeloidMono.ttf', TILESIZE//2)

# sound effects
pickup =pygame.mixer.Sound('DropDash-main/assets/powerup.mp3')
pickup.set_volume(0.1)


running = True

def gameover():
    text = font.render('Game Over', True,(0, 0, 0))
    # survive_text = font.render("Survived For {seconds} SECONDS")
    # banana_count = font.render("Banana count: {banana_count}")

    # screen.fill(0, 0, 0)
    # screen.blit(text, (TILESIZE/2 - (text.get_width()/2), TILESIZE/2 - (text.get_height()/2))) 
    # screen.blit(survive_text, (TILESIZE/2 - (survive_text.get_width()/2), TILESIZE/2 + (survive_text.get_height()*1.5))) 
    # screen.blit(banana_count (TILESIZE/2 - (banana_count.get_width()/2), TILESIZE/2 + (banana_count.get_height()*2.5))) 

 
    
def update():
    global speed 
    global score

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 7
    if keys[pygame.K_RIGHT]:
        player_rect.x += 7

    #    banana movement
    for banana in bananas:
     banana.move()
     if banana.rect.colliderect(floor_rect):
         bananas.remove(banana)
         bananas.append(Banana(banana_image, (random.randint(50,300), -50), speed))
     elif banana.rect.colliderect(player_rect):
         bananas.remove(banana)
         bananas.append(Banana(banana_image, (random.randint(50,300), -50), speed))

        #  increment speed of bananas when colliding with player
         speed += 0.1
         score += 1
         pickup.play()

def draw():
    screen.fill('lightblue')
    screen.blit(player_image, player_rect)
    screen.blit(floor_image, floor_rect)

    for banana in bananas:
        screen.blit(banana.image, banana.rect)

    # score board
    score_text = font.render(f'Score:{score}', True, "white")
    screen.blit(score_text, (5,5))

async def main():
    global screen
    global clock
    global speed
    global score
    global seconds
    global floor_image
    global floor_rect
    global player_rect
    
# game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update()
        draw()
        # gameover()

        clock.tick(60)
        pygame.display.update()
        asyncio.run(draw())
        await asyncio.sleep(0)

asyncio.run(main())
   



    