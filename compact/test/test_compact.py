from compact.code.compact import del_adjacent_dups

def test_del_adjacent_dups():

    test_list = [1, 1, 2, 2, 3, 2]
    c = del_adjacent_dups(test_list)
    assert iter(c) == c
