import numpy as np
import iterativeMethods as it

class Seidel(it.iterative):
    
    def __init__(self, numOfVar, coefMat, bMat , precision= 5, absolute_Error= 5.5, iterations=10000, initial=[[1]]):
         super(self.__class__, self).__init__(numOfVar, coefMat, bMat ,precision,  absolute_Error, iterations, initial)
        
        
        
    def Eval (self):
        if not super().diagonallyD(self.coeffMat):
            print("It will not converge\n\t will try to interchange rows to become diagonally Dominant!")
            canD = super().Convert_diagonallyD()
            if canD:
                super().changeValues()
                
            
        iterations = self.iterations
        
        while(True):
            
            if iterations == 0:
                break
            if (iterations!= self.iterations) and (super().check_convergence()):
                break
            #iteration (O(n^2)) for each
            for i in range (0, self.numOfVariables):
                it = self.bMat[i]
                #print(it)
                for j in range (0, self.numOfVariables):
                    if j != i :
                        term = (self.coeffMat[i][j] * self.answer[j][0])
                        term = super().precision(term)
                        it -= term
                        it = super().precision(it)
                        
                        
                        

      
                it /= self.coeffMat[i][i]
                it = super().precision(it)
                self.prev_iteration[i][0] = self.answer[i][0]
                self.answer[i][0] = it       
            
            iterations-=1
            
        super().print_answer()
        return self.answer.flatten().tolist()
  
    
    
   
        
        
        
        
    
        


    