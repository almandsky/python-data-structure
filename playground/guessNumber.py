#! /usr/bin/env python3
import random

print('Please input the max number to guess')
max_num = int(input())
min_num = 1

answer = random.randint(min_num, int(max_num))
retry_times = 0

while True:
    print('Please input your guess number between ' + str(min_num) + ' and ' + str(max_num) + ', input \'exit\' to exit.')
    guess = input()
    if guess == 'exit':
        print('Thanks for playing.  See you!')
        break
    retry_times += 1
    if int(guess) == answer:
        print('Congratulation! You guess the correct answer ' + str(answer) + ' with ' + str(retry_times) + ' guesses')
        break
    elif int(guess) < answer:
        print('Oops, your guess is too small. Please try again.')
        if int(guess) > min_num:
            min_num = int(guess)
    elif int(guess) > answer:
        print('Oops, your guess is too large. Please try again.')
        if int(guess) < max_num:
            max_num = int(guess)
    






