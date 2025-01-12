# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1080, 720])

# Pos variables
x = 250
y = 250

# Variables for text
font = pygame.font.SysFont("comicsansms", 35)
score = 0
lives = 3

player_img = pygame.image.load(r'ufo.png')
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image = player_img
        self.rect = self.image.get_rect()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:
    all_sprites.update()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()

    #Cicle move
    if key_pressed[pygame.K_d]:
        x += 1
    if key_pressed[pygame.K_a]:
        x -= 1
    if key_pressed[pygame.K_w]:
        y -= 1
    if key_pressed[pygame.K_s]:
        y += 1

    #Player move
    if key_pressed[pygame.K_d]:
        player.rect.x += 1
    if key_pressed[pygame.K_a]:
        player.rect.x -= 1
    if key_pressed[pygame.K_w]:
        player.rect.y -= 1
    if key_pressed[pygame.K_s]:
        player.rect.y += 1

    # Limits of move
    if player.rect.x > 720:
        player.rect.x = 720
    if player.rect.x < 20:
        player.rect.x = 20
    if player.rect.y > 780:
        player.rect.y = 780
    if player.rect.y < 20:
        player.rect.y = 20

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Add text to screen
    score_b = font.render("Score " + str(score), True, (0, 0, 255))
    screen.blit(score_b, [0, 0])
    live_b = font.render("Live " + str(lives), True, (255, 0, 0))
    screen.blit(live_b, [0, 40])


    # Draw the player on screen
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()