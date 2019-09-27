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

        l = []
        for i in self.__data:
            for j in i:
                l.append(j)
       
        mx = len(str(max(l)))
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
        return MyMatrix(self.__data)
    
    
    def flip_left_right(self):

        for i in range(len(self.__data)):
            for j in range(len(self.__data[i])//2):
                self.__data[i][j],self.__data[i][-j-1] = self.__data[i][-j-1],self.__data[i][j]
        return MyMatrix(self.__data)

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):

        sdd = copy.deepcopy(self.__data)
        sdd = MyMatrix(sdd)
        s = sdd.flip_up_down()
        return s
    def flipped_left_right(self):
        ss = copy.deepcopy(self.__data)
        ss = MyMatrix(ss)
        s1 = ss.flip_left_right()
        return s1

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
        self.__data = transmat
        return MyMatrix(self.__data)
    
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
        self.__data = MyMatrix(self.__data).__add__(other)
        return MyMatrix(self.__data)
        
        
    def __isub__(self, other):  # change the name!
        """self -= other."""
        self.__data = MyMatrix(self.__data).__sub__(other)
        return MyMatrix(self.__data)
