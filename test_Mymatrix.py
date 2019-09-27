from Mymatrix import MyMatrix

def test_repr():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.__repr__() == '\n1 2 3 \n4 5 6 ')
def test_size():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.size() == (2,3))
def test_get_data():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    assert(mat.get_data() == [[1,2,3],[4,5,6]])
def test_flip_up_down():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    fud = mat.flip_up_down()
    assert(fud.get_data() == [[4,5,6],[1,2,3]])
def test_flip_left_right():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    flr = mat.flip_left_right()
    assert(flr.get_data() == [[3,2,1],[6,5,4]])
def test_flipped_up_down():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    flud = mat.flipped_up_down()
    assert(flud.get_data() == [[4,5,6],[1,2,3]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test_flipped_left_right():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    fllr = mat.flipped_left_right()
    assert(fllr.get_data()== [[3,2,1],[6,5,4]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test_transpose():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    tra = mat.transpose()
    assert(tra.get_data()== [[1,4],[2,5],[3,6]])
def test_transposed():
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    tr = mat.transposed()  
    assert(tr.get_data()== [[1,4],[2,5],[3,6]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
def test__add__():
    s = [[1,2,3],[4,5,6]]
    other = [[1,1,2],[2,2,3]]
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    ads = mat + oth
    assert(ads.get_data()== [[2, 3, 5], [6, 7, 9]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
    assert(oth.get_data()== [[1,1,2],[2,2,3]])
def test__sub__():
    s = [[1,2,3],[4,5,6]]
    other = [[1,1,2],[2,2,3]]
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    subs = mat - oth
    assert(subs.get_data()== [[0,1,1],[2,3,3]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])
    assert(oth.get_data()== [[1,1,2],[2,2,3]])
def test_iadd():
    other = [[1,1,2],[2,2,3]]
    s = [[1,2,3],[4,5,6]]
    oth = MyMatrix(other)
    mat = MyMatrix(s)
    mat += oth
    assert(mat.get_data()== [[2, 3, 5],[6,7,9]])
def test_isub():
    other = [[1,1,2],[2,2,3]]
    s = [[1,2,3],[4,5,6]]
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    mat -= oth
    assert(mat.get_data()== [[0,1,1],[2,3,3]])
def test_empt():
    empt_m = MyMatrix([])
    assert(empt_m.size() == (0,0))
