#!/usr/bin/env python33
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:02:42 2021

#This application has the user guess a number between 1 to 1000 and counts the amount of guesses of the user.
It will tell the user if the value guessed is too low or too high and ask to try again. If the user guesses the number
correct, it will ask the user if they want to play again.

@author: terrydennison
"""
import random
again = str
def guesser():
    number = random.randrange(1,1001)
    counter = 0
    guess = int
    
    while guess != number:
                    guess = int(input('Guess a number between 1 to 1000 with the fewest guesses: '))
                    counter+=1
                                 
                    if guess < number:
                        print('Too low. try again')
                    elif guess > number:
                      print('Too high. try again')

                    elif guess == number:
                        print('\nCongratulations. You guessed the number!')
                        print('You guessed ' + str(counter) + " times")
                        again = str(input('Do you want to play again? (y / n) '))
                        if again == 'y':
                                guesser()
                        elif again =='n':
                             print('Bye!')
guesser()