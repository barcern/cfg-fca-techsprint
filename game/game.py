# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:23:14 2021

@author: barbora

Based on Space-Rocket repo
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
player_size = 70
player_pos = [int(size[0]/2), size[1] - 300]

# Enemy
enemy_img = pygame.image.load("chocolate.png")
enemy_size = 30
enemy_pos = [random.randint(0, size[0]-enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 10

# Collect
#collect_img = pygame.image.load("chocolate.png")
collect_img = pygame.image.load("bone.png")
collect_size = 30
collect_pos = [random.randint(0, size[0]-collect_size), 0]
collect_list = [collect_pos]
collect_speed = 5

# Enemy functions
def show_enemy(enemy_list, enemy_count):
    delay = random.random()
    if len(enemy_list) < enemy_count and delay < 0.05:
        enemy_list.append([random.randint(0, size[0]-collect_size), 0])

def display_enemy(enemy_list):
    for enemy_pos in enemy_list:
        screen.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))

def new_enemy_pos(enemy_list, enemy_speed):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < size[1]:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)

def multi_collide_enemy(player_pos, enemy_list, lives):
    for enemy_pos in enemy_list:
        old_lives = lives
        lives = collide_enemy(player_pos, enemy_pos, lives)
        if old_lives != lives:
            enemy_list.remove(enemy_pos)
    return lives

def collide_enemy(player_pos, enemy_pos, lives):
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x>=p_x and e_x<(p_x+player_size)) or (p_x>=e_x and p_x<(e_x+enemy_size)):
        if(e_y>=p_y and e_y<(p_y+player_size)) or (p_y>=e_y and p_y<(e_y+enemy_size)):
            lives -= 1     
    return lives

def difficulty(score):
    if score < 10:
        enemy_speed = 5
        enemy_count = 3
    elif score < 20:
        enemy_speed = 8
        enemy_count = 4
    elif score < 30:
        enemy_speed = 11
        enemy_count = 5
    elif score < 40:
        enemy_speed = 14
        enemy_count = 6
    elif score < 65:
        enemy_speed = 17
        enemy_count = 7
    else:
        enemy_speed = 20
        enemy_count = 8
    return enemy_speed, enemy_count

# Collect functions
def show_collect(collect_list):
    delay = random.random()
    if len(collect_list) < 7 and delay < 0.06:
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

def multi_collide_collect(player_pos, collect_list, score):
    for collect_pos in collect_list:
        old_score = score
        score = collide_collect(player_pos, collect_pos, score)
        if old_score != score:
            collect_list.remove(collect_pos)
    return score

def collide_collect(player_pos, collect_pos, score):
    p_x = player_pos[0]
    p_y = player_pos[1]
    c_x = collect_pos[0]
    c_y = collect_pos[1]
    if (c_x>=p_x and c_x<(p_x+player_size)) or (p_x>=c_x and p_x<(c_x+collect_size)):
        if(c_y>=p_y and c_y<(p_y+player_size)) or (p_y>=c_y and p_y<(c_y+collect_size)):
            score += 1
            
            return score
    return score

# Game over
def gameover(score):
    screen.blit(background,(0,0))
    text=" GAME OVER"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2)-200))
    text="Your Score: "+str(score)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-100)))
    text="Your Current Jewels: "+str(score)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-60)))
    text="Your Total Jewels: "+str(score)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-20)))
    text="Play Again"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-400,int(size[1]/2)+80))
    text="Buy Power Ups"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-100,int(size[1]/2)+80))
    text="Quit"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)+300,int(size[1]/2)+80))


myFont=pygame.font.SysFont("calibri",35, bold=True, italic=True)
flag = True
score = 0
lives = 3
clock = pygame.time.Clock()
while flag:
    if lives > 0:
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
        # Determine enemy characteristics
        enemy_values = difficulty(score)
        enemy_speed = enemy_values[0]
        enemy_count = enemy_values[1]
        # Initiate bones and chocolates
        show_collect(collect_list)
        show_enemy(enemy_list, enemy_count)
        new_collect_pos(collect_list)
        new_enemy_pos(enemy_list, enemy_speed)
        # Update score and lives in case of collision
        score = multi_collide_collect(player_pos, collect_list, score)
        lives = multi_collide_enemy(player_pos, enemy_list, lives)
        # Show score and lives
        text="Your Score: "+str(score)
        label=myFont.render(text, 1, (0, 0, 0))
        screen.blit(label,(int(size[0]-250),0))
        text="Your Lives: "+str(lives)
        label=myFont.render(text, 1, (0, 0, 0))
        screen.blit(label,(int(size[0]-250),40))
        # Display updates
        display_collect(collect_list)
        display_enemy(enemy_list)
        screen.blit(player_img,(player_pos[0],player_pos[1]))
        #pygame.display.flip()
        clock.tick(30)
        pygame.display.update()
    elif lives == 0:
        gameover(score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
    pygame.display.update()
            
pygame.quit()