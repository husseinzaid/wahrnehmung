import time

import pygame
import pygame.freetype  # Import the freetype module.
from random import randrange
from pygame import mixer
import csv

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


pygame.init()
screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.Font("KOMIKAX_.ttf", 24)
NUM_FONT = pygame.freetype.Font("KOMIKAX_.ttf", 100)
running =  True
j = 3
l = 0
einstellig_1 = [4, 9, 1, 7, 2, 2, 6, 5, 8, 3]
einstellig_2 = [5, 0, 2, 8, 8, 3, 7, 6, 9, 4]
zweistellig_1 = [49,17,22,65,83]
zweistellig_2 = [50,28,83,76,94]



header = ['SpielerName', '1te Sequenz 4-9-1-7-2-2-6-5-8-3', '2te Sequenz 5-0-2-8-8-3-7-6-9-4', '3te Sequenz 49-17-22-65-83' , '4te Sequenz 50-28-83-76-94']
spielerName= "Hönemann"
dateiName = spielerName + ".csv"


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Die erste Sequenz kommt gleich..", (0, 0, 0))
    screen.blit(text_surface, (210, 100))
    # Generate the number

    pygame.display.flip()
    time.sleep(2)
    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (220, 100), "Versuche sie auswendig zu lernen", (0, 0, 0))
    pygame.display.flip()
    time.sleep(2)

    for i in einstellig_1:
        screen.fill((255, 255, 255))
        NUM_FONT.render_to(screen, (350, 200), str(i), (0, 0, 0))
        pygame.display.flip()
        audiofile_path= "zahlen/mp3/" + str(i) + ".mp3"
        mixer.music.load(audiofile_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (100, 200), "Die Eingabe Fenster erscheint nach 1 Minute", (0, 0, 0))
    pygame.display.flip()
    time.sleep(7)
    screen.fill((255, 255, 255))


    buttonunclicked = True
    while buttonunclicked:
        screen.fill((225, 225, 225))
        b1 = button(screen, (300, 300), "Submit", 50, "red on gray")

        GAME_FONT.render_to(screen, (150, 100), "Geben Sie die Zahlen komma getrennt ein", (0, 0, 0))
        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (250, 250))
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ersteEingabe = textinput.value
                print(ersteEingabe)
                buttonunclicked = False
                textinput.value = ''
                break

        pygame.display.update()
        clock.tick(30)

    #----------------------------------------------------------------------------------------------#

    screen.fill((255, 255, 255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Die zweite Sequenz kommt gleich..", (0, 0, 0))
    screen.blit(text_surface, (210, 100))
    # Generate the number

    pygame.display.flip()
    time.sleep(2)
    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (220, 100), "Versuche sie auswendig zu lernen", (0, 0, 0))
    pygame.display.flip()
    time.sleep(2)

    for i in einstellig_2:
        screen.fill((255, 255, 255))
        NUM_FONT.render_to(screen, (350, 200), str(i), (0, 0, 0))
        pygame.display.flip()
        audiofile_path = "zahlen/mp3/" + str(i) + ".mp3"
        mixer.music.load(audiofile_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (150, 200), "Die Eingabe Fenster erscheint nach 2 Minuten", (0, 0, 0))
    pygame.display.flip()
    time.sleep(15)
    screen.fill((255, 255, 255))

    buttonunclicked = True
    while buttonunclicked:
        screen.fill((225, 225, 225))
        b1 = button(screen, (300, 300), "Submit", 50, "red on gray")


        GAME_FONT.render_to(screen, (150, 100), "Geben Sie die Zahlen komma getrennt ein", (0, 0, 0))
        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (250, 250))
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                zweiteEingabe = textinput.value
                buttonunclicked = False
                textinput.value = ''
                break

        pygame.display.update()

        clock.tick(30)


    #----------------------------------------------------------------------------------------------#

    screen.fill((255, 255, 255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Die dritte Sequenz kommt gleich..", (0, 0, 0))
    screen.blit(text_surface, (210, 100))
    # Generate the number

    pygame.display.flip()
    time.sleep(2)
    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (220, 100), "Versuche sie auswendig zu lernen", (0, 0, 0))
    pygame.display.flip()
    time.sleep(2)

    for i in zweistellig_1:
        screen.fill((255, 255, 255))
        NUM_FONT.render_to(screen, (350, 200), str(i), (0, 0, 0))
        pygame.display.flip()
        audiofile_path = "zahlen/mp3/" + str(i) + ".mp3"
        mixer.music.load(audiofile_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (150, 200), "Die Eingabe Fenster erscheint nach 1 Minute", (0, 0, 0))
    pygame.display.flip()
    time.sleep(7)
    screen.fill((255, 255, 255))

    buttonunclicked = True
    while buttonunclicked:
        screen.fill((225, 225, 225))
        b1 = button(screen, (300, 300), "Submit", 50, "red on gray")


        GAME_FONT.render_to(screen, (150, 100), "Geben Sie die Zahlen komma getrennt ein", (0, 0, 0))
        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (250, 250))
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                dritteEingabe = textinput.value
                buttonunclicked = False
                textinput.value = ''
                break

        pygame.display.update()

        clock.tick(30)



    #----------------------------------------------------------------------------------------------#

    screen.fill((255, 255, 255))
    # You can use `render` and then blit the text surface ...
    text_surface, rect = GAME_FONT.render("Die vierte Sequenz kommt gleich..", (0, 0, 0))
    screen.blit(text_surface, (210, 100))
    # Generate the number

    pygame.display.flip()
    time.sleep(2)
    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (220, 100), "Versuche sie auswendig zu lernen", (0, 0, 0))
    pygame.display.flip()
    time.sleep(2)

    for i in zweistellig_2:
        screen.fill((255, 255, 255))
        NUM_FONT.render_to(screen, (350, 200), str(i), (0, 0, 0))
        pygame.display.flip()
        audiofile_path = "zahlen/mp3/" + str(i) + ".mp3"
        mixer.music.load(audiofile_path)
        mixer.music.set_volume(1)
        mixer.music.play()
        time.sleep(2)

    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (150, 200), "Die Eingabe Fenster erscheint nach 2 Minuten", (0, 0, 0))
    pygame.display.flip()
    time.sleep(15)
    screen.fill((255, 255, 255))

    buttonunclicked = True
    while buttonunclicked:
        screen.fill((225, 225, 225))
        b1 = button(screen, (300, 300), "Submit", 50, "red on gray")


        GAME_FONT.render_to(screen, (150, 100), "Geben Sie die Zahlen komma getrennt ein", (0, 0, 0))
        events = pygame.event.get()

        textinput.update(events)
        screen.blit(textinput.surface, (250, 250))
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vierteEingabe = textinput.value
                buttonunclicked = False
                textinput.value = ''
                break

        pygame.display.update()

        clock.tick(30)



    screen.fill((255, 255, 255))
    GAME_FONT.render_to(screen, (150, 200), "Aufwiedersehen", (0, 0, 0))
    pygame.display.flip()
    break


pygame.quit()


secondRow= [spielerName , ersteEingabe , zweiteEingabe , dritteEingabe , vierteEingabe]

# Ergebnisse Berechnen
import numpy as np

ersteEingabe =list(map(int, ersteEingabe.split(",")))
a = np.array(ersteEingabe)
b = np.array(einstellig_1)
a = list(a==b)
erste_Resultat= a.count(True)

zweiteEingabe =list(map(int, zweiteEingabe.split(",")))
a = np.array(zweiteEingabe)
b = np.array(einstellig_2)
a = list(a==b)
zweite_Resultat= a.count(True)

dritteEingabe =list(map(int, dritteEingabe.split(",")))
a = np.array(dritteEingabe)
b = np.array(zweistellig_1)
a = list(a==b)
dritte_Resultat= a.count(True)

vierteEingabe =list(map(int, vierteEingabe.split(",")))
a = np.array(vierteEingabe)
b = np.array(zweistellig_2)
a = list(a==b)
vierte_Resultat= a.count(True)

thirdRow = ["Anzahl richtige Antworten" , str(erste_Resultat), str(zweite_Resultat) , str(dritte_Resultat), str(vierte_Resultat)]
with open(dateiName, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(secondRow)
    writer.writerow(thirdRow)
