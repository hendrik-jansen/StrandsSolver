from utils import *
import nltk

nltk.download("words")
from nltk.corpus import words

DICT = words.words()

# with open('english3.txt', 'r') as file:
#     for line in file:
#         DICT.append(line[:-2].lower())

field = [
    ["d", "c", "a", "f", "l", "a"],
    ["a", "e", "m", "u", "e", "g"],
    ["g", "i", "f", "o", "r", "o"],
    ["l", "i", "t", "e", "r", "m"],
    ["o", "y", "m", "i", "n", "a"],
    ["i", "n", "m", "i", "y", "s"],
    ["t", "a", "c", "r", "d", "e"],
    ["c", "r", "t", "s", "i", "s"],
]
puzzle = Puzzle(field, DICT)

words = []
for i in range(len(field)):
    for j in range(len(field[i])):
        new_words = puzzle.find_words_from([i, j], min_len=0)
        print([str(word) for word in new_words])
        print(f"Found {len(new_words)} new words from position {i}, {j}")
        words += new_words

print(words)
