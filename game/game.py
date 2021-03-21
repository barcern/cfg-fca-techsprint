# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:23:14 2021

@author: barbora
"""

import pygame
import sys
from pygame.locals import *
import random

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
collect_size = 30
collect_pos = [random.randint(0, size[0]-collect_size), 0]
collect_list = [collect_pos]
collect_speed = 7

def show_collect(collect_list):
    delay = random.random()
    if len(collect_list) < 10 and delay < 0.06:
        collect_list.append([random.randint(0, size[0]-collect_size), 0])

def display_collect(collect_list):
    for collect_pos in collect_list:
        screen.blit(collect_img, (collect_pos[0], collect_pos[1]))

def new_collect_pos(collect_list):
    for idx, collect_pos in enumerate(collect_list):
        if collect_pos[1]>=0 and collect_pos[1]<size[1]:
            collect_pos[1]+=collect_speed
        else:
            collect_list.pop(idx)
            #score+=1
    #return score

flag = True
score = 0
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
    show_collect(collect_list)
    new_collect_pos(collect_list)
    display_collect(collect_list)
    screen.blit(player_img,(player_pos[0],player_pos[1]))
    #pygame.display.flip()
    clock.tick(20)
    pygame.display.update()
            
pygame.quit()