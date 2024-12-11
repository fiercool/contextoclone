import random


def randomWord():
    with open("wordlist/filtered_oxford_3000.txt", "r") as file:
        word_list = file.read().splitlines()
        a = random.choice(word_list)
        print ("the random word is " + a)
    return a