from Mymatrix import MyMatrix
s = [[1,2,3],[4,5,6]]
other = [[1,1,2],[2,2,3]]
def test_repr():
    mat = MyMatrix(s)
    assert(mat.__repr__() == '\n1 2 3 \n4 5 6 ')


def test_size():
    mat = MyMatrix(s)
    assert(mat.size() == (2,3))
    empt_m = MyMatrix([])
    assert(empt_m.size() == (0,0))


def test_get_data():
    mat = MyMatrix(s)
    assert(mat.get_data() == s)


def test_flip_up_down():
    mat = MyMatrix(s)
    fud = mat.flip_up_down()
    assert(fud.get_data() == [[4,5,6],[1,2,3]])


def test_flip_left_right():
    mat = MyMatrix(s)
    flr = mat.flip_left_right()
    assert(flr.get_data() == [[3,2,1],[6,5,4]])


def test_flipped_up_down():
    mat = MyMatrix(s)
    flud = mat.flipped_up_down()
    assert(flud.get_data() == [[4,5,6],[1,2,3]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])


def test_flipped_left_right():
    mat = MyMatrix(s)
    fllr = mat.flipped_left_right()
    assert(fllr.get_data()== [[3,2,1],[6,5,4]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])


def test_transpose():
    mat = MyMatrix(s)
    tran = mat.transpose()
    assert(tran.size() == (3,2))
    assert(tran.get_data()== [[1,4],[2,5],[3,6]])


def test_transposed():
    mat = MyMatrix(s)
    tr = mat.transposed()  
    assert(tr.get_data()== [[1,4],[2,5],[3,6]])
    assert(mat.get_data()== [[1,2,3],[4,5,6]])


def test__add__():
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    ads = mat + oth
    assert(ads.get_data()== [[2, 3, 5], [6, 7, 9]])
    assert(mat.get_data()== s)
    assert(oth.get_data()== other)


def test__sub__():
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    subs = mat - oth
    assert(subs.get_data()== [[0,1,1],[2,3,3]])
    assert(mat.get_data()== s)
    assert(oth.get_data()== other)


def test_iadd():
    oth = MyMatrix(other)
    mat = MyMatrix(s)
    mat += oth
    assert(mat.get_data()== [[2, 3, 5],[6,7,9]])


def test_isub():
    mat = MyMatrix(s)
    oth = MyMatrix(other)
    mat -= oth
    assert(mat.get_data()== [[0,1,1],[2,3,3]])
    
    
def test_rotate_clockwise_90():
    mat = MyMatrix(s)
    rotm = mat.rotate_clockwise_90()
    assert(rotm.get_data() == [[4,1],[5,2],[6,3]])

           
def test_rotated_clockwise_90():
    mat = MyMatrix(s)
    rotm = mat.rotated_clockwise_90()
    assert(rotm.get_data() == [[4,1],[5,2],[6,3]])
    assert(mat.get_data()== s)

    
def test_rotate_counterclockwise_90():
    mat = MyMatrix(s)
    rotmcw = mat.rotate_counterclockwise_90()
    assert(rotmcw.get_data() == [[3,6],[2,5],[1,4]])
    
    
def test_rotated_counterclockwise_90():
    mat = MyMatrix(s)
    rotmcw = mat.rotated_counterclockwise_90()
    assert(rotmcw.get_data() == [[3,6],[2,5],[1,4]])
    assert(mat.get_data()== s)
    
def test_rotate_180():
    mat = MyMatrix(s)
    rt = mat.rotate_180()
    assert(rt.get_data() == [[6,5,4],[3,2,1]])
    
    
def test_rotated_180():
    mat = MyMatrix(s)
    rt = mat.rotated_180()
    assert(rt.get_data() == [[6,5,4],[3,2,1]])
    assert(mat.get_data()== s)
