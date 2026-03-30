from __future__ import annotations
from typing import Optional, Union, List
from dataclasses import dataclass


class TrieNode:
    def __init__(self, children=None, end=False):
        self.children = children
        if self.children == None:
            self.children = {}
        self.end = end


class Trie:
    def __init__(self, root: Optional[TrieNode] = None):
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


class Path:
    def __init__(
        self, coord_list, field, trie, current_node: Optional[TrieNode] = None
    ):
        self.coord_list = coord_list
        self.field = field
        self.trie = trie
        self.current_node = current_node
        if self.current_node == None:
            self.update_current_node()

    @property
    def length(self):
        return len(self.coord_list)

    def update_current_node(self):
        prefix = str(self)
        current_node = self.trie.root
        for c in prefix:
            try:
                current_node = current_node.children[c]
            except:
                raise ValueError("Path is not a prefix in Trie")
        self.current_node = current_node

    def is_prefix(self):
        return self.trie.is_prefix(str(self))

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
                if (
                    new_coord[0] < 0
                    or new_coord[1] < 0
                    or new_coord[0] >= len(self.field)
                    or new_coord[1] >= len(self.field[0])
                    or new_coord in self.coord_list
                ):
                    continue
                new_char = self.field[new_coord[0]][new_coord[1]]
                if new_char not in self.current_node.children:
                    continue
                next_path = Path(
                    self.coord_list + [new_coord],
                    self.field,
                    self.trie,
                    self.current_node.children[new_char],
                )
                next_paths.append(next_path)
        return next_paths

    def __str__(self) -> str:
        return "".join([self.field[i][j] for i, j in self.coord_list])


class Puzzle:
    def __init__(self, field, dictionary):
        self.field = field
        self.dictionary = dictionary
        self.trie = Trie()
        self.trie.add_dict(dictionary)

    def find_words_from(self, coords, min_len=0):
        if not self.trie.is_prefix(self.field[coords[0]][coords[1]]):
            return []
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


@dataclass
class Element:
    left: Optional[Element] = None
    right: Optional[Element] = None
    up: Optional[Element] = None
    down: Optional[Element] = None
    header: Optional[Column] = None


@dataclass
class Column(Element):
    size: Optional[int] = None
    index: Optional[int] = None


def insert_left(e1: Element, e2: Element):
    e2.left = e1.left
    e2.right = e1
    e1.left.right = e2
    e1.left = e2


def insert_right(e1: Element, e2: Element):
    e2.right = e1.right
    e2.left = e1
    e1.right.left = e2
    e1.right = e2


def insert_up(e1: Element, e2: Element):
    e2.up = e1.up
    e2.down = e1
    e1.up.down = e2
    e1.up = e2


# def insert_word(header: Column, word: Path):
#     new_column = Column(size=word.lenght, word=word)


def construct_matrix(word_list: List[Path], width, height):
    h = Column()
    h.left = h
    h.right = h
    columns = []
    for i in range(width * height):
        c = Column(size=0, index=i)
        c.header = c
        c.up = c
        c.down = c
        columns.append(c)
        insert_left(h, c)
    for word in word_list:
        indices = sorted([coord[0] * width + coord[1] for coord in word.coord_list])
        first_e = None
        for i in indices:
            e = Element(header=columns[i])
            columns[i].size += 1
            if first_e == None:
                e.right = e
                e.left = e
                first_e = e
            insert_up(columns[i], e)
            insert_left(first_e, e)
    return h


# def construct_matrix(word_list: List[Path], width, height):
#     first_row_element = [None] * (width * height)
#     root = Column()
#     root.left = root
#     root.right = root
#     for word in word_list:
#         new_column = Column(size=word.length, word=word)
#         new_column.right = root
#         new_column.left = root.left
#         root.left.right = new_column
#         root.left = new_column
#         new_column.down = new_column
#         new_column.up = new_column
#         element_rows = sorted([coord[0] * coord[1] for coord in word.coord_list])
#         for row in element_rows:
#             new_element = Element(header=new_column)
#             new_element.down = new_column
#             new_element.up = new_column.up
#             new_column.up.down = new_element
#             new_column.up = new_element
#             if first_row_element[row] == None:
#                 first_row_element[row] = new_element
#                 first_row_element[row].right = first_row_element[row]
#                 first_row_element[row].left = first_row_element[row]
#             new_element.right = first_row_element[row]
#             new_element.left = first_row_element[row].left
#             first_row_element[row].left.right = new_element
#             first_row_element[row].left = new_element
#     return root


def find_word_cover(word_list, width, height):
    matrix = construct_matrix(word_list, width, height)
