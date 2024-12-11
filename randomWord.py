import random
def randomWord():

    with open("wordlist\oxford_3000_edited.txt", "r") as file:
        word_list = file.read().splitlines()
    return random.choice(word_list)

