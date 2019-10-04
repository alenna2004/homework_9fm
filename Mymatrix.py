sl =[[1,2,3,4],[4,8,19,1],[3,4,6,7], [8,9,0,4], [3,5,11,8]]
import copy
class MyMatrix:
    def __init__(self, data: list):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        self.__data = copy.deepcopy(data)
        

    def __repr__(self) -> str:

        e = []
        for i in self.__data:
            for j in i:
                e.append(j)
       
        mx = len(str(max(e)))
        a= ""
        for i in self.__data:
            a = a + "\n"
            for j in i:
                a = a + str(j) + " " *mx
        return a


    def size(self) -> tuple:
        try:
            return len(self.__data),len(self.__data[0])
        except:
            return 0,0 

    def flip_up_down(self):

        for i in range(len(self.__data)//2):
            
            self.__data[i],self.__data[-i-1] = self.__data[-i-1],self.__data[i]
        return self
    
    
    def flip_left_right(self):

        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])//2):
                self.__data[i][j],self.__data[i][-j-1] = self.__data[i][-j-1],self.__data[i][j]
        return self

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):
        sdd = copy.deepcopy(self.__data)
        sdd = MyMatrix(sdd).flip_up_down()
        return sdd
    
    def flipped_left_right(self):
        ss = copy.deepcopy(self.__data)
        ss = MyMatrix(ss).flip_left_right()
        return ss

    def transposed(self):
        sdata = copy.deepcopy(self.__data)
        transmat = MyMatrix(sdata).transpose()
        return transmat
    
    def transpose(self):
        #self.__data = MyMatrix(self.__data).transposed()
        transmat = []
        c = 0
        for j in range(len(self.__data)):
            while c < len(self.__data[j]):
                st = []
                for i in range(len(self.__data)):
                    st.append(self.__data[i][c])
                transmat.append(st)
                c +=1
        #trans = copy.deepcopy(transmat)
        #return MyMatrix(transmat)
        self = MyMatrix(transmat)
        return self
    
    def get_data(self) -> list:
        copd = copy.deepcopy(self.__data)
        return copd
    
    def __add__(self, other):      
        newdate = [[0]*len(self.__data[0])]*len(self.__data)
        for i in range(len(self.__data)):
            newdate[i] = copy.deepcopy(self.__data[i])
            for j in range(len(self.__data[i])):
                newdate[i][j] = self.__data[i][j] + other.__data[i][j]

        return MyMatrix(newdate)
    def __sub__(self, other):
        newdate = [[0]*len(self.__data[0])]*len(self.__data)
        for i in range(len(self.__data)):
            newdate[i] = copy.deepcopy(self.__data[i])
            for j in range(len(self.__data[i])):
                newdate[i][j] = self.__data[i][j] - other.__data[i][j]
        return MyMatrix(newdate)
    def __iadd__(self, other):  # change the name!
        """self += other."""
        self = MyMatrix(self.__data).__add__(other)
        return self
        
        
    def __isub__(self, other):  # change the name!
        """self -= other."""
        self = MyMatrix(self.__data).__sub__(other)
        return self
    def rotate_clockwise_90(self):
        self= MyMatrix(self.__data).transpose()
        self = self.flip_left_right()
        return self

    def rotate_counterclockwise_90(self):
        self = MyMatrix(self.__data).transpose()
        self = self.flip_up_down()
        return self

    def rotate_180(self):
        self = MyMatrix(self.__data).flip_left_right()
        self = self.flip_up_down()
        return self 
    
    def rotated_clockwise_90(self):
        seld = copy.deepcopy(self.__data)
        return MyMatrix(seld).rotate_clockwise_90()

    def rotated_counterclockwise_90(self):
        sel = copy.deepcopy(self.__data)
        return MyMatrix(sel).rotate_counterclockwise_90()

    def rotated_180(self):
        se = copy.deepcopy(self.__data)
        return MyMatrix(se).rotate_180()
    
    def __getitem__(self,ind):
        return self.__data[ind[0]][ind[1]]
    
    def __setitem__(self,ind,val):  
        self.__data[ind[0]][ind[1]]= val
