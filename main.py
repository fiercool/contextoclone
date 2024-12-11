from score import scorer
from randomWord import randomWord

targetWord = randomWord()

while True:
    guess = input("enter your word: ").strip().lower()
    result = scorer(guess, targetWord)  
    
    if result: 
        break