from nltk.corpus import words

class path():
    def __init__(self, coord_list):
        self.coord_list = coord_list

    def is_word():
        pass


class puzzle():
    def __init__(self, field):
        field = field

    def path_is_word(self, path):
        #TODO
        pass

    def path_is_prefix(self, path):
        #TODO
        pass

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



words = []

for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        print(puzzle[i][j])



