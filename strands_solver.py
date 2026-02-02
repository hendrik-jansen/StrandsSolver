from utils import *


class puzzle():
    def __init__(self, field, dictionary):
        self.field = field
        self.dictionary = dictionary

    def find_words_from(self, coords):
        words = []
        done = False
        next_paths = [Path([coords], self.field, self.dictionary)]
        while not done:
            for path in next_paths:
                if path.is_word():
                    words.append(path)
                next_paths += path.next_paths()
            if len(next_paths) == 0:
                done = True

DICT = []

with open('words.txt', 'r') as file:
    for line in file:
        DICT.append(line[:-2].lower())

# print(DICT)

WordTrie = Trie()

WordTrie.add_dict(DICT)

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(puzzle[i][j])