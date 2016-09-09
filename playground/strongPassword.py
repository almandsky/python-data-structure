#! /usr/bin/env python3
# strongPassword.py - Make sure the password is strong enough

import re

while True:

    print('Please input a password to test, type \'exit\' to exit')
    
    pw = input()
    if pw == 'exit':
        break
    
    lengthCheckRegex = re.compile(r'(\d|\w|\s|\D|\W|\S){8,}')
    upperCaseCheck = re.compile(r'[A-Z]+')
    lowerCaseCheck = re.compile(r'[a-z]+')
    digitCheck = re.compile(r'\d+')
    
    isLengthEnough = lengthCheckRegex.search(pw)
    if isLengthEnough == None:
        print('Error! Please input at least 8 characters\n')
        continue
    
    containUpperCase = upperCaseCheck.search(pw)
    if containUpperCase == None:
        print('Error! Please input at least one upper case character\n')
        continue
    
    containLowerCase = lowerCaseCheck.search(pw)
    if containLowerCase == None:
        print('Error! Please input at least one lower case character\n')
        continue
    
    containDigit = digitCheck.search(pw)
    if containDigit == None:
        print('Error! Please input at least one digit number\n')
        continue
    
    print('Congratulations! This is a valid password!\n')

