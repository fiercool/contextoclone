from score import scorer
from randomWord import randomWord

with open("wordlist/filtered_oxford_3000.txt", "r") as file:
    word_list = file.read().splitlines()

targetWord = randomWord()

while True:
    guess = input("Enter your word: ").strip().lower()
    result = scorer(guess, targetWord, word_list)  
    
    if result:
        print(f"yes the correct word was '{targetWord}'.")
        break
