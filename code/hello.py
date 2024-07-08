#!/usr/bin/env python3.10
import random

noun = input("noun:")
verb = input("verb:")

sentence = f"i love to see {noun} fly high .I love you so much my kid.you are \ my everything , i know you love to {verb}.Keep flying my sunshine."
print(sentence)

######Guess the number#########

def guess(a, b):
    random_num = random.randint(a, b)
    gues = 0
    while gues != random_num:
        gues = int(input(f'Guess your random number between {a} and {b} : '))
        if gues < random_num:
            print(f"Sorry ! Guess agin , too low")
        elif gues > random_num:
            print(f"sorry! Guess again , too high !")
    print(f"yahhh! you guessed it correctly , your gueesed number is {random_num}")

guess(1,10)