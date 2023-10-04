import numpy as np
from numpy.core.numeric import zeros_like

class Court_decompostion:
    #initializaiton function
    def __init__(self, coefficient, answer, percision):
        if percision == "" :
            percision = 5
        self.co_array = coefficient #matrix of cooefficient 
        self.ans = answer #matrix of equations' answers
        self.perc = int(percision) #the percision the user needed
        
    #function to turn co-efficient to LU decompostion
    def turn_to_LU(self):
        arr = self.co_array #copy of the co-efficient matrix
        r = self.co_array.shape[0] #number of rows of the matrix
        c = self.co_array.shape[1] #number of columns of the matrix
        L = np.zeros([r, c]) #L matrix
        U = np.zeros([r, c]) #U matrix

        for i in range(r):
            L[i, 0] = arr[i, 0] #first column in L matrix

        for i in range(r):
            for j in range(c):
                if i == j:
                    U[i, j] = 1 #diagonal in U matrix is 1s
                elif i == 0:
                    U[i, j] = round(float(arr[i, j]) / float(L[0,0]), self.perc) #first row in U matrix

        #from the second row to the end
        for i in range(1, r):
            for j in range(i+1): #elemetns under the diagonal 
                sum = 0
                for k in range(j):
                    sum += L[i, k] * U[k, j] #sum of the elements befor the one we want to get
                L[i, j] = round(float(arr[i, j]) - float(sum), self.perc) #get elements under the diagonal
            
            for j in range(i+1, r):
                sum = 0
                for k in range(i):
                    sum += L[i, k] * U[k, j]
                U[i, j] = round((float(arr[i, j]) - sum)/float(L[i, i]), self.perc)

        return L, U #return 2 matrices which are  the L, and U matrices

    #LUx = b --> Ly = b
    #fucntion to get y
    def find_y(self, L):
        b = self.ans #copy of answer matrix
        r = b.shape[0] #number of rows
        y = [0 for i in range(r)]
        try:
            y[0] = round(float(b[0]) / float(L[0, 0]), self.perc) #get first value in y matrix
            #go through the rest of L matrix to get the rest of y matrix
            for i in range(1, r):
                for j in range(i):
                    b[i] = float(b[i]) - float(L[i, j]) * float(y[j]) #subract the coefficent in its variable value until we reach the unkonw variable
                y[i] = round(float(b[i]) / float(L[i, i]), self.perc) #get the unkonw variable be divide the subraction by coefficient of the unkown
        except ZeroDivisionError: #in case of division by 0 return error
            return 'error'
        print("y equals : -", y)
        return y
    

    
    #LUx = b --> Ly = b --> y = Ux
    #function to get x
    def find_x(self, U, y):
        if (y != "error") :
            r = U.shape[0]
            x = [0 for i in range(r)]
            try:
                x[r-1] = round(float(y[r-1])/ float(U[r-1, r-1]), self.perc)
    
                for i in range(1, r):
                    index = r - i - 1
                    for j in range(r):
                        if j != index:
                            y[index] -= (U[index, j] * x[j])
                    x[index] = round(float(y[index]) / float(U[index, index]), self.perc)
            except ZeroDivisionError:
                return 'error'
            return x
        else :
            return "error"

        



       
    

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# answers = [1,2,3]
# array =  np.array(values, float).reshape(3, 3)
# ans = np.array(answers, float).reshape(3, 1)
# court = Court_decompostion(array, ans, 5)
# L, U = court.turn_to_LU()
# print(L)
# print(U)
# y = court.find_y(L)
# print(y)
# if(y == 'error'):
#     print("this equations can't be solved")
# else:
#     X = court.find_x(U, y)
#     if(X != 'error'):
#         print("crout")
#         print(X)
#     else:
#         print("this equations can't be solved")


