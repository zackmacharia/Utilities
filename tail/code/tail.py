def tail(seq, num):
    """This functions takes a sequence and an integer and returns the last items specified by the input integer.
    Input: Sequence and Integer (n)
    Output: Last n itemes of the sequence 
    """
    seq_size = len(seq)
    start_index = seq_size - num

    new_seq = [item for item in seq[start_index:]]
    return new_seq


if __name__ == '__main__':
    seq = 'hello'
    tail(seq, 3)
