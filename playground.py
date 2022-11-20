import pygame_textinput
import pygame
pygame.init()

# # Create TextInput-object
# textinput = pygame_textinput.TextInputVisualizer()
#
# screen = pygame.display.set_mode((1000, 200))
# clock = pygame.time.Clock()
#
# while True:
#     screen.fill((225, 225, 225))
#
#     events = pygame.event.get()
#
#     # Feed it with events every frame
#     textinput.update(events)
#     # Blit its surface onto the screen
#     screen.blit(textinput.surface, (10, 10))
#
#     for event in events:
#         if event.type == pygame.QUIT:
#             exit()
#
#     pygame.display.update()
#     clock.tick(30)


import numpy as np
eingabe = '4,2,3,4,5,6,7,8'
inteingabe =list(map(int, eingabe.split(",")))
#print(inteingabe)
einstellig_1 = [4, 9, 1, 7, 2, 2, 6, 5, 8, 3]


import numpy as np

a = np.array(inteingabe)
lena = a.size

if lena < 10:
    rest = 10 - lena
    restVector = np.zeros(rest)
    a = np.append(inteingabe,restVector)

b = np.array(einstellig_1)
a = list(a==b)
count= a.count(True)
print(a==b)
