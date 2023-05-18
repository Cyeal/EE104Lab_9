# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:24:50 2023

@author: Franc
"""

#Importing necessary modules and functions
import pgzrun
from pgzero.builtins import Actor, clock
from random import randint
import music, time

#Setting up the game window dimensions
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

#Initializing variables
move_list = []          
display_list = []      

score1 = 0              
score2 = 0              
current_move = 0        
count = 4               #Countdown timer value
dance_length = 4        

say_dance = False       #Flag to display "Dance!" message
show_countdown = True   #Flag to display countdown
moves_complete = False  #Flag to indicate if all moves have been displayed
game_over = False       #Flag to indicate if the game is over

#Creating actor objects for the dancer and dance move arrows
dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40

up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    #Function to draw the game elements on the screen
    global game_over, score1, score2, say_dance, count, show_countdown
    if not game_over:
        #If the game is not over, draw the dancer, arrows, and scores
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Player 1 Score: " + str(score1), color="black", topleft=(10, 10))
        screen.draw.text("Player 2 Score: " + str(score2), color="black", topleft=(10, 30))
        if say_dance:
            screen.draw.text("Dance!", color="black", topleft=(CENTER_X - 65, 150), fontsize=60)
        if show_countdown:
            screen.draw.text(str(count), color="black", topleft=(CENTER_X - 8, 150), fontsize=60)
    else:
        #If the game is over, only draw the scores and "GAME OVER!" message
        screen.clear()
        screen.blit("stage", (0, 0))
        screen.draw.text("Player 1 Score: " + str(score1), color="black", topleft=(10, 10))
        screen.draw.text("Player 2 Score: " + str(score2), color="black", topleft=(10, 30))
        screen.draw.text("GAME OVER!", color="black", topleft=(CENTER_X - 130, 220), fontsize=60)

def reset_dancer():
    #Function to reset the dancer and arrow images
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"

def update_dancer(move):
    #Function to update the dancer and arrow images based on the given move
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)

def display_moves():
    #Function to display the dance moves on the screen
    global move_list, display_list, dance_length, say_dance, show_countdown, current_move
    if display_list:
        #If there are moves left to display, get the next move from the list
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
           
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
           
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        
        say_dance = True
        show_countdown = False

def generate_moves():
    #Function to generate random dance moves
    global move_list, dance_length, count, show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        #Generate a random move (0: up, 1: right, 2: down, 3: left) and add it to the move list
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
    show_countdown = True
    countdown()

def countdown():
    #Function to implement the countdown before displaying dance moves
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()

def next_move():
    #Function to move to the next dance move in the sequence
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True

def on_key_up(key):
    #Function to handle key release events
    global score1, score2, game_over, move_list, current_move, Player2
    if Player2 == 1:
        #If it's Player 1's turn, check the released key and update the dancer and scores accordingly
        if key == keys.UP:
            update_dancer(0)
            if move_list[current_move] == 0:
                score1 = score1 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.RIGHT:
            update_dancer(1)
            if move_list[current_move] == 1:
                score1 = score1 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.DOWN:
            update_dancer(2)
            if move_list[current_move] == 2:
                score1 = score1 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.LEFT:
            update_dancer(3)
            if move_list[current_move] == 3:
                score1 = score1 + 1
                next_move()
            else:
                game_over = True
    else:
        #If it's Player 2's turn, check the released key and update the dancer and scores accordingly
        if key == keys.W:
            update_dancer(0)
            if move_list[current_move] == 0:
                score2 = score2 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.D:
            update_dancer(1)
            if move_list[current_move] == 1:
                score2 = score2 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.S:
            update_dancer(2)
            if move_list[current_move] == 2:
                score2 = score2 + 1
                next_move()
            else:
                game_over = True
        elif key == keys.A:
            update_dancer(3)
            if move_list[current_move] == 3:
                score2 = score2 + 1
                next_move()
            else:
                game_over = True

def update():
    #Function to update the game state
    global game_over, current_move, moves_complete, Player2
    if not game_over:
        if moves_complete:
            #If all moves have been executed, generate a new sequence and switch players
            generate_moves()
            moves_complete = False
            current_move = 0
            Player2 = Player2 * -1

#Setting the initial player to 1 and generating the first dance moves
Player2 = 1
generate_moves()
music.play("song")
pgzrun.go()
update()


"""
from random import randint
# Import Libraries / Modules
import pgzrun
import pygame
import pgzero
import sys
import random
from pgzero.builtins import Actor

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

move_list = []
display_list = []

score = 0
current_move = 0
count = 4
dance_length = 4

say_dance = False
show_countdown = True
moves_complete = False
game_over = False

dancer = Actor("dancer-start")
dancer.pos = CENTER_X + 5, CENTER_Y - 40
up = Actor("up")
up.pos = CENTER_X, CENTER_Y + 110
right = Actor("right")
right.pos = CENTER_X + 60, CENTER_Y + 170
down = Actor("down")
down.pos = CENTER_X, CENTER_Y + 230
left = Actor("left")
left.pos = CENTER_X - 60, CENTER_Y + 170

def draw():
    global game_over, score, say_dance
    global count, show_countdown
    if not game_over:
        screen.clear()
        screen.blit("stage", (0, 0))
        dancer.draw()
        up.draw()
        down.draw()
        right.draw()
        left.draw()
        screen.draw.text("Score: " +
                         str(score), color="black",
                         topleft=(10, 10))
        if say_dance:
            screen.draw.text("Dance!", color="black",
                             topleft=(CENTER_X - 65, 150), fontsize=60)
        if show_countdown:
            screen.draw.text(str(count), color="black",
                             topleft=(CENTER_X - 8, 150), fontsize=60)
        else:
            screen.clear()
            screen.blit("stage", (0, 0))
            screen.draw.text("Score: " +
                             str(score), color="black",
                             topleft=(10, 10))
            screen.draw.text("GAME OVER!", color="black",
                             topleft=(CENTER_X - 130, 220), fontsize=60)
            return
        
def reset_dancer():
    global game_over
    if not game_over:
        dancer.image = "dancer-start"
        up.image = "up"
        right.image = "right"
        down.image = "down"
        left.image = "left"
    return

def update_dancer(move):
    global game_over
    if not game_over:
        if move == 0:
            up.image = "up-lit"
            dancer.image = "dancer-up"
            clock.schedule(reset_dancer, 0.5)
        elif move == 1:
            right.image = "right-lit"
            dancer.image = "dancer-right"
            clock.schedule(reset_dancer, 0.5)
        elif move == 2:
            down.image = "down-lit"
            dancer.image = "dancer-down"
            clock.schedule(reset_dancer, 0.5)
        else:
            left.image = "left-lit"
            dancer.image = "dancer-left"
            clock.schedule(reset_dancer, 0.5)
        return
    
def display_moves():
    global move_list, display_list, dance_length
    global say_dance, show_countdown, current_move
    if display_list:
        this_move = display_list[0]
        display_list = display_list[1:]
        if this_move == 0:
            update_dancer(0)
            clock.schedule(display_moves, 1)
        elif this_move == 1:
            update_dancer(1)
            clock.schedule(display_moves, 1)
        elif this_move == 2:
            update_dancer(2)
            clock.schedule(display_moves, 1)
        else:
            update_dancer(3)
            clock.schedule(display_moves, 1)
    else:
        say_dance = True
        show_countdown = False
    return

def countdown():
    global count, game_over, show_countdown
    if count > 1:
        count = count - 1
        clock.schedule(countdown, 1)
    else:
        show_countdown = False
        display_moves()
    return

def generate_moves():
    global move_list, dance_length, count
    global show_countdown, say_dance
    count = 4
    move_list = []
    say_dance = False
    for move in range(0, dance_length):
        rand_move = randint(0, 3)
        move_list.append(rand_move)
        display_list.append(rand_move)
        show_countdown = True
        countdown()
    return

def next_move():
    global dance_length, current_move, moves_complete
    if current_move < dance_length - 1:
        current_move = current_move + 1
    else:
        moves_complete = True
    return

def on_key_up(key):
    global score, game_over, move_list, current_move
    if key == keys.UP:
        update_dancer(0)
        if move_list[current_move] == 0:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.RIGHT:
        update_dancer(1)
        if move_list[current_move] == 1:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.DOWN:
        update_dancer(2)
        if move_list[current_move] == 2:
            score = score + 1
            next_move()
        else:
            game_over = True
    elif key == keys.LEFT:
        update_dancer(3)
        if move_list[current_move] == 3:
            score = score + 1
            next_move()
        else:
            game_over = True
    return

generate_moves()
music.play("vanishing-horizon")

def update():
    global game_over, current_move, moves_complete
    if not game_over:
        if moves_complete:
            generate_moves()
            moves_complete = False
            current_move = 0
        else:
            music.stop()
            """