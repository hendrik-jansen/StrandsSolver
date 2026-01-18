from nltk.corpus import words

DICT = []

with open('words.txt', 'r') as file:
    for line in file:
        DICT.append(line[:-2].lower())

print(DICT)

class path():
    def __init__(self, coord_list, field):
        self.coord_list = coord_list
        self.field = field
        word_pointer_start = None
        word_pointer_end = None      

    def is_word(self):
        pass

    def is_prefix(self):
        pass

    def __repr__(self):
        ''.join([self.field[i][j] for i, j in self.coord_list])



class puzzle():
    def __init__(self, field):
        field = field

    def find_words_from(self, coords):
        words = []
        depth = 0
        done = False
        while not done:
            paths = [[coords]]
            for path in paths:
                if path.is_word():
                    words.append(path.string())
                if not path.is_prefix():
                    pass


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(puzzle[i][j])



