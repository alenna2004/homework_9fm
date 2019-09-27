from Mymatrix import MyMatrix

def test_repr():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.__repr__() == '1 2 3\n 4 5 6')
def test_size():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.size() == (2, 3))
def test_get_data():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.get_data() == [[1,2,3],[4,5,6]])
def test_flip_up_down():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.flip_up_down() == [[4,5,6],[1,2,3]])
def test_flip_left_right():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.flip_left_right() == [[3,2,1],[4,5,6]])
def test_flipped_up_down():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    flud = m.flipped_up_down()
    assert(flud == [[4,5,6],[1,2,3]])
    assert(m.get_data()== [[1,2,3],[4,5,6]])
def test_flipped_left_right():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    fllr = m.flipped_left_right()
    assert(fllr== [[3,2,1],[4,5,6]])
    assert(m.get_data()== [[1,2,3],[4,5,6]])
def test_transpose():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.transpose()== [[1,4],[2,5],[3,6]])
def test_transposed():
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    tr = m.transpose()
    assert(tr== [[1,4],[2,5],[3,6]])
    assert(m.get_data()== [[1,2,3],[4,5,6]])
def test__add__():
    other = [[3,5,6],[9,4,6]]
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.__add__(other)== [[4,7,9],[13,9,12]])
def test__sub__():
    other = [[1,1,2],[2,2,3]]
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.__sub__(other)== [[0,1,1],[2,3,3]])
def test_iadd():
    other = [[1,1,2],[2,2,3]]
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.iadd(other)== [[4,7,9],[13,9,12]])
def test_isub():
    other = [[1,1,2],[2,2,3]]
    sl = [[1,2,3],[4,5,6]]
    m = MyMatrix(sl)
    assert(m.isub(other)== [[0,1,1],[2,3,3]])
