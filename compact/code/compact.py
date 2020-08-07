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
    generator_object = del_adjacent_dups(sequence)
    result = [item for item in generator_object]
    print(result)
 
