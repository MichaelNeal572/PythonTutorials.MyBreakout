# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:58:22 2018

@author: Michael
"""

from tkinter import *
import table, ball, bat, random

##Methods  
def setup_game():
    global first_serve
    first_serve = True
    my_ball.stop_ball()
    my_ball.start_position()
    bat_B.start_position()
    
def draw_scoreboard(condition):
    setup_game()
    if(condition=="win"):
        my_table.draw_score(""," YOU WIN!")
    if(condition=="lose"):
        while (len(bricks)!=0):
            my_table.remove_item(bricks[0].rectangle)
            bricks.remove(bricks[0])
        my_table.draw_score(""," YOU DIED")
    if(condition=="new game"):
        my_table.draw_score("","")
        
def stack_bricks():
    global bricks
    ##2 straight lines
    b=1
    while b<7:
        i=80
        bricks.append(bat.Bat(table=my_table, width=50, height=20, x_posn=(b*i), y_posn=75, colour="green"))
        b=b+1
    b=1
    while b<7:
        i=80
        bricks.append(bat.Bat(table=my_table, width=50, height=20, x_posn=(b*i), y_posn=150, colour="orange"))
        b=b+1
    ##
    #stack_bricks() can be extended with conditional statments to allow different level configurations to be selected 
    #at random or by level selection
def check_brick_collisions():
    global bricks
    for b in bricks:
        if (b.detect_collision(my_ball, sides_sweet_spot=False)[0]!=False):
            print(bool(random.getrandbits(1)))
            if(bool(random.getrandbits(1))==True):
                spawn_powerup()
            my_table.remove_item(b.rectangle)
            bricks.remove(b)
        if(len(bricks) == 0):
            draw_scoreboard("win")

def ball_movements():
    my_ball.move_next()
    window.after(50, game_flow)
    

def spawn_powerup():
    print ("spawn")
def spawn_bat():
    print("spawn")
def spawn_ball():
    print("spawn")

def restart_game(master):
    draw_scoreboard("new game")
    stack_bricks()
    my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
##

##global objects
x_velocity = 4
y_velocity = 10
first_serve = True
bricks=[]
bats = []
balls = []
power_ups = []

#window
window=Tk()
window.title("MyBreakout")
#table
my_table = table.Table(window)
#ball
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity, width=24, height=24, colour="red", x_start=288, y_start=250)
#bats
bat_B = bat.Bat(table=my_table, width=100, height=10, x_posn=250,y_posn=370, colour="blue")
#bricks
stack_bricks()
##
    
##keybindings
window.bind("<Left>", bat_B.move_left)
window.bind("<Right>" ,bat_B.move_right)
window.bind("<space>", restart_game)
##

##animation loops
def game_flow():
    global first_serve
    if(first_serve ==True):
        my_ball.stop_ball()
        first_serve=False
    #bat collisions
    bat_B.detect_collision(my_ball,sides_sweet_spot=False, topnbottom_sweet_spot=True)
    check_brick_collisions()
    #ball movement
    ball_movements()
    my_ball.move_next()
    window.after(50, game_flow)
    #wall collisions
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        draw_scoreboard("lose")
    #first serve
game_flow()

window.mainloop()
##
