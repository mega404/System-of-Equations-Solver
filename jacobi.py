import numpy as np
from copy import copy
import iterativeMethods as it

class jac (it.iterative):

    #Constructor to instialize the object
    def __init__(self, numOfVar, coefMat, bMat ,precision,  absolute_Error, iterations, initial):
        super(self.__class__, self).__init__(numOfVar, coefMat, bMat , precision, absolute_Error, iterations, initial)
    
    
    def Eval (self):
        if not super().diagonallyD(self.coeffMat):
            print("It will not converge\
                  will try to interchange rows to become diagonally Dominant!")
            canD = super().Convert_diagonallyD()
            if canD:
                super().changeValues()
                
             
        iterations = self.iterations
        
        while(True):
            
            if iterations == 0:
                break
            
            if (iterations!=self.iterations) and (super().check_convergence()):
                break
            
            a = []
            #iteration (O(n^2)) for each
            for i in range (0, self.numOfVariables):
                it = self.bMat[i]
                for j in range (0, self.numOfVariables):
                    if j != i :
                        term = self.coeffMat[i][j] * self.answer[j][0]
                        term = super().precision(term)
                        it -= term
                        it = super().precision(it)
                        
                                
                it /= self.coeffMat[i][i]
                it = super().precision(it)
                a.append(it)

            self.prev_iteration  = copy(self.answer)
            a = np.array(a).T
            a = a.reshape((-1, 1))
            self.answer = copy(a)
            iterations-=1
            
        super().print_answer()
        return self.answer.flatten().tolist()