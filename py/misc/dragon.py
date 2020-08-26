import random, time

def intro():
    print('a')

def choose():
    choice = ''
    while choice != '1' and choice != '2':
        print('choice? (1 or 2)')
        choice = input()

    return choice

def checkChoice(choice)
