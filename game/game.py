# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:23:14 2021

@author: barbora
"""

import pygame
import sys
from pygame.locals import *

pygame.init()

# Define colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Open a new window
size = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TO BE NAMED")
background = pygame.image.load("background.jpg")

# Player
player_img = pygame.image.load("dog_walk.png")
player_size = 30
player_pos = [int(size[0]/2), size[1] - 300]

# Enemy
# enemy_img = pygame.image.load("")

# Collect
collect_img = pygame.image.load("bone.png")


flag = True
clock = pygame.time.Clock()
while flag:
    screen.fill(white)
    screen.blit(background, (0,0))
    screen.blit(player_img, player_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_pos[0] > 10:
                player_pos[0] -= player_size + 10
            elif event.key == pygame.K_RIGHT and player_pos[0] < size[0] - 180:
                player_pos[0] += player_size + 10
            player_pos = player_pos
    #screen.fill(white)
    #pygame.draw.rect(screen, red, [55, 200, 100, 70],0)
    pygame.display.flip()
    clock.tick(60)
            
pygame.quit()