from Mymatrix import MyMatrix

def test_repr():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.__repr__() == '\n1 2 3 \n4 5 6 ')
def test_size():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.size() == '(2,3)')
def test_get_data():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.get_data() == [[1,2,3],[4,5,6]])
def test_flip_up_down():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.flip_up_down() == [[4,5,6],[1,2,3]])
def test_flip_left_right():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.flip_left_right() == [[3,2,1],[6,5,4]])
def test_flipped_up_down():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    flud = mat.flipped_up_down()
    assert(flud == [[4,5,6],[1,2,3]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test_flipped_left_right():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    fllr = mat.flipped_left_right()
    assert(fllr== [[3,2,1],[6,5,4]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test_transpose():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.transpose()== [[1,4],[2,5],[3,6]])
def test_transposed():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    tr = mat.transposed()
    assert(tr== [[1,4],[2,5],[3,6]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test__add__():
    other = [[3,5,6],[9,4,6]]
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.__add__(other)== [[4,7,9],[13,9,12]])
def test__sub__():
    other = [[1,1,2],[2,2,3]]
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.__sub__(other)== [[0,1,1],[2,3,3]])
def test_iadd():
    other = [[1,1,2],[2,2,3]]
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.iadd(other)== [[2, 3, 5],[6,7,9]])
def test_isub():
    other = [[1,1,2],[2,2,3]]
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.isub(other)== [[0,1,1],[2,3,3]])
