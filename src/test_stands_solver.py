from utils import Trie, Path, Puzzle, Element, Column, construct_matrix


def test_trie():
    """Test the Trie Data-Structure"""
    word_list = ["hello", "", "there"]
    trie = Trie()
    trie.add_dict(word_list)
    assert trie.is_prefix("hel") is True
    assert trie.is_prefix("hi") is False
    assert trie.is_word("there") is True
    assert trie.is_word("ther") is False


def test_path():
    field = [
        ["h", "o", "l", "l", "o"],
        ["o", "e", "i", "n", "f"],
        ["f", "h", "i", "h", "u"],
        ["g", "e", "u", "e", "s"],
    ]
    dictionary = ["hello"]
    trie = Trie()

    trie.add_dict(dictionary)
    path1 = Path([[0, 0]], field, trie)
    path2 = Path([[2, 1]], field, trie)
    assert len(path1.next_paths()) == 1
    assert len(path2.next_paths()) == 2


def test_puzzle():
    field = [
        ["h", "o", "l", "l", "o"],
        ["o", "e", "i", "n", "f"],
        ["f", "i", "i", "h", "u"],
        ["g", "l", "o", "e", "s"],
    ]
    dictionary = ["hello"]
    puzzle = Puzzle(field, dictionary)
    words = puzzle.find_words_from([0, 0])
    assert [str(word) for word in words] == ["hello"]


def test_construct_matrix():
    field = [
        ["i", "n"],
        ["n", "i"],
    ]
    dictionary = ["in"]
    puzzle = Puzzle(field, dictionary)
    words = []
    for i in range(2):
        for j in range(2):
            words += puzzle.find_words_from([i, j])
    assert len(words) == 4
    h = construct_matrix(words, 2, 2)
    for i in range(4):
        h = h.right
        assert h.size == 2
