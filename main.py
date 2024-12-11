from score import scorer
from randomWord import randomWord

while True:
    word1 = input("enter your word: ").strip().lower()
    word2 = randomWord()
    print(word2)
    scorer(word1, word2)