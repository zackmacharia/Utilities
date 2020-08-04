def del_adjacent_dups(sequence):
    """This generator takes a sequence and removes adjacent duplicate values"""
    placeholder_val = None
    compact_list = []
    for item in sequence:
        if item != placeholder_val:
            compact_list.append(item)
            placeholder_val = item
    yield compact_list    


if __name__ == '__main__':
    sequence = [1, 1, 2, 2, 3, 2]
    del_adjacent_dups(sequence)
    # c = del_adjacent_dups(n**2 for n in [1, 2, 2])
    # print(iter(c) is c)
    # print(next(c))

