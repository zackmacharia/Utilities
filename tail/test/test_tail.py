from tail.code.tail import tail


def test_tail_seq():
    """Tests a sequence and positive number as input"""

    data_seq = [12, 45, 6, 7, 88, 4, 'boy', 'girl']
    exptected_output = [4, 'boy', 'girl']
    assert tail(data_seq, 3) == exptected_output


def test_tail_seq_zero():
    """"Tests a sequence and negative number as input"""

    data = [12, 45, 6, 7, 88, 4, 'boy', 'girl']
    exptected_output = []
    assert tail(data, -3) == exptected_output


def test_tail_iter():
    """Tests an iterator and positive number as input"""

    data_iter = (n**2 for n in range(10))
    exptected_output = [49, 64, 81]
    assert tail(data_iter, 3) == exptected_output


def test_tail_iter_zero():
    """Tests an iterator and negative number as input"""

    data_iter = (n**2 for n in range(10))
    exptected_output = []
    assert tail(data_iter, -3) == exptected_output







