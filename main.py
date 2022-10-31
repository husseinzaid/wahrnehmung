import time

import pygame
import pygame.freetype  # Import the freetype module.
from random import randrange

import pygame_textinput


def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Calibri", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    #print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y))

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

clock = pygame.time.Clock()

print(randrange(1000))

pygame.init()
screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.Font("KOMIKAX_.ttf", 24)
NUM_FONT = pygame.freetype.Font("KOMIKAX_.ttf", 100)
running =  True
j = 3
l = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("The numbers will apear..", (0, 0, 0))
    screen.blit(text_surface, (210, 100))
    # Generate the number


    pygame.display.flip()
    time.sleep(2)
    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (220, 100),"Try to memorize them", (0, 0, 0))
    pygame.display.flip()
    time.sleep(1)
    random = randrange(pow(10, j))
    numonscreen= str(random)
    for i in range(len(str(random))):
        numonscreen
        screen.fill((255,255,255))
        NUM_FONT.render_to(screen, (350, 200), numonscreen[i], (0, 0, 0))
        pygame.display.flip()
        time.sleep(2)
    j = j+1
    buttonunclicked = True
    l=l+1
    while buttonunclicked:
        screen.fill((225, 225, 225))
        b1 = button(screen, (300, 300), "Submit", 50, "red on gray")
        level = "level" + str(l)
        GAME_FONT.render_to(screen, (150, 10), level, (0, 0, 0))

        GAME_FONT.render_to(screen, (150, 100), "enter the numbers in reverse order", (0, 0, 0))
        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (250, 250))
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    if textinput.value == numonscreen[::-1]:
                        screen.fill((225, 225, 225))
                        GAME_FONT.render_to(screen, (220, 100), "CORRECT!", (0, 0, 0))

                        pygame.display.update()
                        time.sleep(2)
                        buttonunclicked = False
                        textinput.value = ''
                        break
                    else:
                        screen.fill((225, 225, 225))
                        GAME_FONT.render_to(screen, (220, 100), "You Lost!", (0, 0, 0))

                        pygame.display.update()
                        time.sleep(2)
                        exit()
                        break






        pygame.display.update()

        clock.tick(30)



pygame.quit()