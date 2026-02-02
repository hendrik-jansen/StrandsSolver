from utils import *


DICT = []

with open('english3.txt', 'r') as file:
    for line in file:
        DICT.append(line[:-2].lower())

field = [
            ['t','s','a','h','a','s'],
            ['e','k','t','r','b','h'],
            ['r','s','i','a','g','t'],
            ['i','l','d','c','a','l'],
            ['s','e','t','k','o','r'],
            ['d','y','e','b','o','e'],
            ['n','e','m','c','e','a'],
            ['u','r','s','t','r','c']
         ]
puzzle = Puzzle(field, DICT)

words = []
for i in range(len(field)):
    for j in range(len(field[0])):
        new_words = puzzle.find_words_from([i, j])
        print([str(word) for word in new_words])
        print(f"Found {len(new_words)} new words from position {i}, {j}")
        words.append(new_words)
