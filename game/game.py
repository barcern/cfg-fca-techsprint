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
player_img_sleep = pygame.image.load("dog_sleep.png")
player_img_wait = pygame.image.load("dog_wait.png")
player_size = 70
player_pos = [int(size[0]/2), size[1] - 300]

# Enemy
enemy_img = pygame.image.load("chocolate.png")
enemy_size = 30
enemy_pos = [random.randint(0, size[0]-enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 5

# Collect
#collect_img = pygame.image.load("chocolate.png")
collect_img = pygame.image.load("bone.png")
collect_size = 30
collect_pos = [random.randint(0, size[0]-collect_size), 0]
collect_list = [collect_pos]
collect_speed = 5

# Jewel
jewel_img = pygame.image.load("jewel.png")
jewel_size = 30
jewel_pos = [random.randint(0, size[0]-jewel_size), 0]
jewel_list = [jewel_pos]
jewel_speed = 15

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

# Jewel functions
def show_jewel(jewel_list):
    delay = random.random()
    if len(jewel_list) < 1 and delay < 0.001:
        jewel_list.append([random.randint(0, size[0]-jewel_size), 0])

def display_jewel(jewel_list):
    for jewel_pos in jewel_list:
        screen.blit(jewel_img, (jewel_pos[0], jewel_pos[1]))

def new_jewel_pos(jewel_list):
    for idx, jewel_pos in enumerate(jewel_list):
        if jewel_pos[1]>=0 and jewel_pos[1]<size[1]:
            jewel_pos[1]+=jewel_speed
        else:
            jewel_list.pop(idx)
            #score+=1
    #return score

def multi_collide_jewel(player_pos, jewel_list, jewels):
    for jewel_pos in jewel_list:
        old_jewels = jewels
        jewels = collide_jewel(player_pos, jewel_pos, jewels)
        if old_jewels != jewels:
            jewel_list.remove(jewel_pos)
    return jewels

def collide_jewel(player_pos, jewel_pos, jewels):
    p_x = player_pos[0]
    p_y = player_pos[1]
    j_x = jewel_pos[0]
    j_y = jewel_pos[1]
    if (j_x>=p_x and j_x<(p_x+player_size)) or (p_x>=j_x and p_x<(j_x+jewel_size)):
        if(j_y>=p_y and j_y<(p_y+player_size)) or (p_y>=j_y and p_y<(j_y+jewel_size)):
            jewels += 1
    return jewels

# Game over
def gameover(score):
    screen.blit(background,(0,0))
    text=" GAME OVER"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-120,int(size[1]/2)-200))
    text="Your Score: "+str(score)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-100)))
    text="Your Current Jewels: "+str(jewels)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-60)))
    text="Your Total Jewels: "+str(125)
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-150,int(size[1]/2-20)))
    text="Play Again"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-400,int(size[1]/2)+80))
    text="Buy Power Ups"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-120,int(size[1]/2)+80))
    text="Quit"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)+300,int(size[1]/2)+80))
    screen.blit(player_img_sleep, (int(size[0]/2)-120, int(size[1])-270))

# Start screen
myFont=pygame.font.SysFont("calibri",35, bold=True, italic=True)
end_it=False
while (end_it==False):
    screen.fill(white)
    screen.blit(background, (0,0))
    text = "Welcome to *insert name* game!"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-250,int(size[1]/2)-200))
    text = "Aims of the game:"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-200,int(size[1]/2)-50))
    text = "- eat as many bones as possible"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-200,int(size[1]/2)-0))
    text = "- collect as many jewels as possible"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-200,int(size[1]/2)+50))
    text = "- avoid the chocolate!"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-200,int(size[1]/2)+100))
    text = "Click anywhere to start"
    label=myFont.render(text, 1, (0, 0, 0))
    screen.blit(label,(int(size[0]/2)-200,int(size[1]/2)+250))
    screen.blit(player_img_wait, (50, int(size[1]/2)+0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            end_it=True
    pygame.display.flip()

# Running loop
flag = True
score = 0
jewels = 0
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
        # Initiate bones and chocolates and jewels
        show_collect(collect_list)
        show_enemy(enemy_list, enemy_count)
        show_jewel(jewel_list)
        new_collect_pos(collect_list)
        new_enemy_pos(enemy_list, enemy_speed)
        new_jewel_pos(jewel_list)
        # Update score and lives in case of collision
        score = multi_collide_collect(player_pos, collect_list, score)
        lives = multi_collide_enemy(player_pos, enemy_list, lives)
        jewels = multi_collide_jewel(player_pos, jewel_list, jewels)
        # Show score and lives and jewels
        text="Score: "+str(score)
        label=myFont.render(text, 1, (0, 0, 0))
        screen.blit(label,(int(size[0]-250),0))
        text="Lives: "+str(lives)
        label=myFont.render(text, 1, (0, 0, 0))
        screen.blit(label,(int(size[0]-250),40))
        text="Jewels: "+str(jewels)
        label=myFont.render(text, 1, (0, 0, 0))
        screen.blit(label,(int(size[0]-250),80))
        # Display updates
        display_collect(collect_list)
        display_enemy(enemy_list)
        display_jewel(jewel_list)
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