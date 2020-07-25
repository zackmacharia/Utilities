"""
Pseudo Code
Task - Remove adjacent duplicate values e.g. [1, 1, 2, 3, 3, 4, 5, 2] -> [1, 2, 3, 4, 5, 2]
Set a placeholder variable to store the value to compare against. e.g. placeholder_val = None (to initialize)

placeholder_val = None  # initialize comparison variable to none since there is nothing to compare against
compact_list = [] # Initialize an empty list to hold the non-adjacent duplicate values
for item in item_list: # item list here is the input iterable provided
    if item != placeholder_val: # compare the current value to the placeholder value
        compact_list.append(item)
        placeholder_val = item # update the  placeholder variable to hold the current value of item
    else:
        continue

"""       

def del_adjacent_dups(sequence):
    placeholder_val = None
    compact_list = []
    for item in sequence:
        if item != placeholder_val:
            compact_list.append(item)
            placeholder_val = item
    return compact_list    


if __name__ == '__main__':
    sequence = [1, 1, 2, 2, 3, 2]
    # sequence = [n**2 for n in [1, 2, 2]]
    del_adjacent_dups(sequence)

