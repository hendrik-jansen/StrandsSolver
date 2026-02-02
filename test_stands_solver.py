from utils import Trie, Path

def test_trie():
    """Test the Trie Data-Structure""" 
    word_list = ['hello', '', 'there']
    trie = Trie()
    trie.add_dict(word_list)
    assert trie.is_prefix('hel') is True
    assert trie.is_prefix('hi') is False
    assert trie.is_word('there') is True
    assert trie.is_word('ther') is False


def test_path():
    field = [
        ['h', 'o', 'l', 'l', 'o'],
        ['o', 'e', 'i', 'n', 'f'],
        ['f', 'h', 'i', 'h', 'u'],
        ['g', 'e', 'u', 'e', 's']
    ]
    dictionary = ['hello']
    trie = Trie()

    trie.add_dict(dictionary)
    path1 = Path([[0, 0]], field, trie)
    path2 = Path([[2, 1]], field, trie)
    assert(len(path1.next_paths()) == 1)
    assert(len(path2.next_paths()) == 2)
