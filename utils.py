class TrieNode():
    def __init__(self, children = None, end = False):
        self.children = children
        if self.children == None:
            self.children = {}
        self.end = end

class Trie():
    def __init__(self, root = None):
        self.root = root
        if self.root == None:
            self.root = TrieNode() 
    
    def add_word(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.end = True

    def add_dict(self, dictionary):
        for word in dictionary:
            self.add_word(word)

    def is_prefix(self, prefix):
        current_node = self.root
        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False
        return True
    
    def is_word(self, word):
        current_node = self.root
        for c in word:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return False
        return current_node.end == True

class Path():
    def __init__(self, coord_list, field, trie, current_node = None):
        self.coord_list = coord_list
        self.field = field
        self.trie = trie
        self.current_node = current_node
        if self.current_node == None:
            self.update_current_node()
        
    def update_current_node(self):
        prefix = str(self)
        current_node = self.trie.root
        for c in prefix:
            try:
                current_node = current_node.children[c]
            except:
                raise ValueError('Path is not a prefix in Trie')
        self.current_node = current_node

    def is_word(self):
        return self.current_node.end

    def next_paths(self):
        next_paths = []
        last_coord = self.coord_list[-1]
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                new_coord = [last_coord[0] + i, last_coord[1] + j]
                if (new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= len(self.field)
                    or new_coord[1] >= len(self.field[0]) or new_coord in self.coord_list):
                    continue
                new_char = self.field[new_coord[0]][new_coord[1]]
                if new_char not in self.current_node.children:
                    continue
                next_path = Path(self.coord_list + [new_coord], self.field, self.trie, self.current_node.children[new_char])
                next_paths.append(next_path)
        return next_paths

    def __str__(self) -> str:
        return ''.join([self.field[i][j] for i, j in self.coord_list])

class Puzzle():
    def __init__(self, field, dictionary):
        self.field = field
        self.dictionary = dictionary
        self.trie = Trie()
        self.trie.add_dict(dictionary)

    def find_words_from(self, coords, min_len = 4):
        words = []
        done = False
        paths = [Path([coords], self.field, self.trie)]
        while not done:
            next_paths = []
            for path in paths:
                if path.is_word() and len(path.coord_list) >= min_len:
                    words.append(path)
                next_paths += path.next_paths()
            paths = next_paths
            if len(paths) == 0:
                done = True
        return words
    


