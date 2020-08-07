from collections import deque


def tail(data, num):
    """This functions takes in data (sequence or iterable) and an integer.
    It then returns the last items specified by the input integer.
    Input: Sequence or Iterable and an Integer -> designated as (n)
    Output: Last n items of the sequence
    """

    if num < 1:
        return list()
    else:
        dequed_data = deque(data, num)
        dequed_data_list = list(dequed_data)  # return deque list only
        return dequed_data_list


if __name__ == '__main__':
    # seq = 'hello'
    seq = (n**2 for n in range(10))
    tail(seq, -3)
