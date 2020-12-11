'''
Danny Godwin
CS5001 Final Project
12/07/20
'''

import turtle
import time
import random
from PositionService import *

screen = turtle.Screen()
screen.bgpic("Screen Shot 2020-12-02 at 9.36.59 AM.gif")
screen.register_shape('card_back.gif')

status = turtle.Turtle()
status.ht()
status.penup()
status.setposition(-300, -317)
status.write('0 moves, 0 matches', font = ('Arial', 19))

match = turtle.Turtle()
match.ht()
match.penup()
match.setposition(-190, -317)

leaders = turtle.Turtle()
leaders.ht()
leaders.pencolor("blue")
leaders.penup()
leaders.setposition(175,270)
    
with open('Leaderboard.txt', mode ='r') as leaderboard:
    leaders.right(90)
    score = []
    for line in leaderboard:
        score.append(line.split())
    score.sort(key=lambda x: int(x[0]))
    score = score[:8]
  
    for x in score:
        x = ' '.join(x)
        leaders.write(x, font = ('Arial', 19))
        leaders.forward(30)
        
class Card:

    def __init__(self, image, x,y):

        screen.register_shape(image)
        self.x = x
        self.y = y
        self.image = image
        self.card_back = turtle.Turtle()
        self.card_front = turtle.Turtle()
        self.card_back.penup()
        self.card_front.penup()
        self.card_back.ht()
        self.card_front.ht()
        self.card_back.goto(x,y)
        self.card_front.goto(x,y)
        self.card_front.shape(image)
        self.card_back.shape('card_back.gif')
        self.card_back.st()
        self.card_front.ht()

    def x_axis(self):
        x = self.x
        return x

    def y_axis(self):
        y = self.y
        return y

    def flip(self):
        
        self.card_back.ht()
        self.card_front.st()

    def __eq__(self, other):
        if self.card_front == other.card_front:
            return True
        else:
            return False

    def same(self):
        
        return self.image

    def remove(self):

        self.card_back.ht()
        self.card_front.ht()
        self.card_back.clear()
        self.card_front.clear()

    def __str__(self):
        return self.image

    def win(self):
        if self.card_back.isvisible() == False and self.card_front.isvisible() == False:
            return False

    def is_visible(self):
        return self.card_back.isvisible()

    def reset(self):
    
        self.card_back.st()
        self.card_front.ht()

def get_click(x,y):

    set_position_x(x)
    set_position_y(y)
    x = get_position_x()
    y = get_position_y()


    if x > 175 and x < 240 and y > -330 and y < -290:
        Quit = turtle.Turtle()
        screen.register_shape('quitmsg.gif')
        Quit.shape('quitmsg.gif')
        time.sleep(1.5)
        turtle.Screen().bye()
        
    if is_visible() == False:
        for card in cards:
            a = card.x_axis()
            b = card.y_axis()
            if  x > a-60 and x < a+60 and y > b-80 and y < b+80 and card.is_visible() == True:
                card.flip()
                global picked_first
                picked_first = card
                set_visible(True)
                return
                                  
    if is_visible() == True:
        for card in cards:
            a = card.x_axis()
            b = card.y_axis()
            if  x > a-60 and x < a+60 and y > b-80 and y < b+80 and card.is_visible() == True:
                card.flip()
                picked_second = card
                time.sleep(1)
                global guesses
                global name
                if picked_first.same() == picked_second.same() and picked_first != picked_second:
                    picked_first.remove()
                    picked_second.remove()
                    global matches
                    matches = matches + 1
                    status.clear()
                    status.write('Guesses: {}'.format(guesses), font = ('Arial', 19))
                    match.clear()
                    match.write('Matches: {}'.format(matches), font = ('Arial', 19))
                    win = all(card.win() == False for card in cards)
                    if win == True:
                        won = turtle.Turtle()
                        screen.register_shape('winner.gif')
                        won.shape('winner.gif')
                        with open('Leaderboard.txt', mode ='a+') as leaderboard:

                            leaderboard.write(str(guesses)+' ')
                            leaderboard.write(name)
                            leaderboard.write('\n')

                        time.sleep(1)
                        turtle.Screen().bye()
                    else:
                        set_visible(False)
                        return   
                else:
                    picked_first.reset()
                    picked_second.reset()
                    
                    guesses = guesses + 1
                    status.clear()
                    status.write('Guesses: {}'.format(guesses), font = ('Arial', 19))
                    match.write('Matches: {}'.format(matches), font = ('Arial', 19))
                    
                set_visible(False)
                return

def card_distro(number):

    card_list = ['2_of_clubs.gif','2_of_clubs.gif','2_of_diamonds.gif',\
                 '2_of_diamonds.gif','3_of_hearts.gif','3_of_hearts.gif',\
                 'ace_of_diamonds.gif','ace_of_diamonds.gif','jack_of_spades.gif',\
                 'jack_of_spades.gif','king_of_diamonds.gif','king_of_diamonds.gif']
                
    global card_1, card_2, card_3, card_4, card_5, card_6,card_7,card_8,card_9,card_10,card_11,card_12

    global cards
    cards = []

    if number == 8:

        card_list = card_list[0:8]
        random.shuffle(card_list)

        card_1 = Card(card_list[0],-300,250)
        card_2 = Card(card_list[1],-180,250)
        card_3 = Card(card_list[2],-60,250)
        card_4 = Card(card_list[3],60,250)
        card_5 = Card(card_list[4],-300,80)
        card_6 = Card(card_list[5],-180,80)
        card_7 = Card(card_list[6],-60,80)
        card_8 = Card(card_list[7],60,80)

        cards = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8]

    if number == 10:

        card_list = card_list[0:10]
        random.shuffle(card_list)
    
        card_1 = Card(card_list[0],-300,250)
        card_2 = Card(card_list[1],-180,250)
        card_3 = Card(card_list[2],-60,250)
        card_4 = Card(card_list[3],60,250)
        card_5 = Card(card_list[4],-300,80)
        card_6 = Card(card_list[5],-180,80)
        card_7 = Card(card_list[6],-60,80)
        card_8 = Card(card_list[7],60,80)
        card_9 = Card(card_list[8],-300,-90)
        card_10 = Card(card_list[9],-180,-90)
    
        cards = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,\
             card_10]

    if number == 12:

        random.shuffle(card_list)

        card_1 = Card(card_list[0],-300,250)
        card_2 = Card(card_list[1],-180,250)
        card_3 = Card(card_list[2],-60,250)
        card_4 = Card(card_list[3],60,250)
        card_5 = Card(card_list[4],-300,80)
        card_6 = Card(card_list[5],-180,80)
        card_7 = Card(card_list[6],-60,80)
        card_8 = Card(card_list[7],60,80)
        card_9 = Card(card_list[8],-300,-90)
        card_10 = Card(card_list[9],-180,-90)
        card_11 = Card(card_list[10],-60,-90)
        card_12 = Card(card_list[11],60,-90)

        cards = [card_1,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,\
             card_10,card_11,card_12]

def main():

    global name
    name = screen.textinput("CS5001 Memory game","Your Name:")

    card_number = screen.textinput("Set Up","# of Cards to Play: (8, 10 or 12)")

    while card_number != '8' and card_number != '10' and card_number != '12' :
        card_number = screen.textinput("Set Up","Invalid Entry. # of Cards to Play: (8, 10 or 12)")

    card_number = int(card_number)
    card_distro(card_number) 
    set_visible(False)

    global guesses
    guesses = 0
    global matches
    matches = 0

    screen.onclick(get_click)

main()
        
        
    

        

        

        
