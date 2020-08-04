from tail.code.tail import tail


def test_tail():

    data = [12, 45, 6, 7, 88, 4, 'boy', 'girl']
    exptected_output = [4, 'boy', 'girl']
    assert tail(data, 3) == exptected_output