DICT = []

with open('words.txt', 'r') as file:
    for line in file:
        DICT.append(line[:-2].lower())

print(DICT)

class path():
    def __init__(self, coord_list, field):
        self.coord_list = coord_list
        self.field = field
        if len(coord_list) == 1:
            self.word_pointer_start = None
            self.word_pointer_end = None

    def is_word(self):
        return str(self) == DICT[self.word_pointer_start]

    def is_prefix(self):
        pass

    def next(self):
        next_paths = []
        last_coord = self.coord_list[-1]
        for i, j in zip([-1,1]):
            # TODO
            pass

    def __str__(self):
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
            next_paths = []
            for path in paths:
                if path.is_word():
                    words.append(path)

                if path.is_prefix():
                    next_paths += path.next()


for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(puzzle[i][j])



