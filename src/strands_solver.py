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
    ["u", "e", "t", "e", "r", "m"],
    ["c", "i", "m", "i", "n", "a"],
    ["r", "l", "g", "i", "y", "s"],
    ["u", "y", "c", "r", "d", "e"],
    ["c", "e", "r", "s", "i", "s"],
]
puzzle = Puzzle(field, DICT)

words = []
for i in range(len(field)):
    for j in range(len(field[i])):
        new_words = puzzle.find_words_from([i, j], min_len=4)
        print([str(word) for word in new_words])
        print(f"Found {len(new_words)} new words from position {i}, {j}")
        words += new_words

print(words)
print("searching word covers")
covers = []
covers = find_word_cover(words, 6, 8)
print("done!")
