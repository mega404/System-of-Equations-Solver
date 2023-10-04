import numpy as np
#GaussElimination method
class GaussElimination:
    def __init__(self, x, y, precision): 
        #Ax=b equation
        if (precision == '') :
            precision = 5
        self.inputMatrix = np.array(x, dtype= float) #A matrix
        self.y = np.array(y, dtype= float) #b matrix
        self.output = np.zeros(self.y.shape)
        self.precision = int(precision)
        self.no_error = True
        self.partialPivoting() #Apply partial pivoting on matrix
        self.forwardElimination()
        self.backSubstitution()
        print("GaussElimination Algorithm:")
        print(self.output) #print result

    #forward elimination method
    def forwardElimination(self):
            for i in range(self.inputMatrix.shape[1]):
                self.partialPivoting()
                for j in range(i+1, self.inputMatrix.shape[0]):
                    #get multiplier
                    if self.inputMatrix[i][i] != 0:
                        multiplier = round(float(self.inputMatrix[j][i])/float(self.inputMatrix[i][i]),
                                           ndigits=self.precision)
                    else :
                        self.no_error = False
                        return self.no_error
                    
                    self.y[j] = round(self.y[j] - multiplier*self.y[i], self.precision)
                    for k in range(self.inputMatrix.shape[1]):
                        #Chang values of A matrix using multiplier 
                        self.inputMatrix[j][k] = round(self.inputMatrix[j][k] - multiplier*self.inputMatrix[i][k],
                                                       self.precision)
    #partial pivoting algorithm
    def partialPivoting(self):        
        for i in range(self.inputMatrix.shape[1]):
                #get index of maximum element in the spicified column   
                index = np.argmax(abs(self.inputMatrix[i:,i]))
                for j in range(self.inputMatrix.shape[1]):
                    #Swap elemnts for all row
                    temp = self.inputMatrix[i][j]
                    self.inputMatrix[i][j] = self.inputMatrix[index+i][j]
                    self.inputMatrix[index+i][j] = temp
                temp = self.y[i]
                self.y[i] = self.y[index+i]
                self.y[index+i] = temp
                
    #backSubstitution method
    def backSubstitution(self):
        if self.no_error == True :
            if self.inputMatrix[self.output.shape[0]-1][self.output.shape[0]-1] !=0: 
                self.output[self.output.shape[0]-1] = round(self.y[self.output.shape[0]-1]/self.inputMatrix[self.output.shape[0]-1][self.output.shape[0]-1],
                                                            self.precision
                                                        )
            else:
                self.no_error = False
                return "error"
            for i in range(self.inputMatrix.shape[0]-2, -1, -1):
                sum = 0
                for j in range(i+1, self.inputMatrix.shape[0]):
                    sum += round(self.inputMatrix[i][j] * self.output[j], self.precision)    
                if self.inputMatrix[i][i] != 0:
                    self.output[i] = round((self.y[i] - sum)/self.inputMatrix[i][i], 
                                        self.precision
                                        )
                else:
                    return "error"
            return self.output
        else :
            return "error"
                
#GauessJordan algorithm       
#the class inherit gauess elemination class for forwardElimination & Partial pivoting    
class GauessJordan(GaussElimination):
    def __init__(self, x, y, precision): 
        if (precision == '') :
            precision = 5
        self.inputMatrix = np.array(x, dtype= float)
        self.y = np.array(y, dtype= float)
        self.output = np.zeros(self.y.shape)
        self.precision = int(precision)
        self.no_error = True
        self.partialPivoting() 
        self.forwardElimination()
        if self.no_error == True :
            self.backElimation()
        self.getOutput() 
        print("GauessJordan Algorithm:")
        print(self.output)
       
         
    def backElimation(self):
        for i in range(self.inputMatrix.shape[1]-1, -1, -1):
            self.partialPivoting()
            for j in range(i):         
                if self.inputMatrix[i][i] != 0:
                    multiplier = round(self.inputMatrix[j][i]/self.inputMatrix[i][i], self.precision)
                else:
                    self.no_error = False
                    return self.no_error
                self.inputMatrix[j][i] = round(self.inputMatrix[j][i]- multiplier*self.inputMatrix[i][i], self.precision)
                self.y[j] = round(self.y[j] - multiplier*self.y[i], self.precision)
                 
    def getOutput(self): 
        if self.no_error == True :
            for i in range(self.output.shape[0]):
                self.output[i] = round(self.y[i]/self.inputMatrix[i][i], self.precision)  
            return self.output      
        else :
            return "error"    

class LUDolittle((GaussElimination)):
    def __init__(self, x, y, precision):
        if (precision == '') :
            precision = 5
        self.inputMatrix = np.array(x, dtype= float)
        
        self.lowerMatrix = np.zeros(x.shape)
        self.y = np.array(y, dtype= float)
        self.output1 = np.zeros(self.y.shape)
        self.output2 = np.zeros(self.y.shape)
        self.precision = int(precision)
        self.no_error = True
        self.partialPivoting()
        self.forwardElimination()
        if self.no_error == True :
            self.forwardSubstituaion()
        self.backSubstitution()
        print("LUDolittle Algorithm")
        print(self.output2) 

    def forwardElimination(self):
        for i in range(self.inputMatrix.shape[1]):
            self.lowerMatrix[i][i] = 1
            for j in range(i+1, self.inputMatrix.shape[0]):
                if self.inputMatrix[i][i] != 0:
                    multiplier = self.inputMatrix[j][i]/self.inputMatrix[i][i]
                else:
                    self.no_error = False
                    return self.no_error
                #set elements of lower matrix
                self.lowerMatrix[j][i] = round(multiplier, self.precision)
                for k in range(self.inputMatrix.shape[1]):
                    self.inputMatrix[j][k] = round(self.inputMatrix[j][k] - multiplier*self.inputMatrix[i][k], self.precision)
    def forwardSubstituaion(self):
        self.output1[0] = round(self.y[0], self.precision)
        for i in range(1, self.inputMatrix.shape[0]):
            sum = 0
            for j in range(0, i):
                sum += self.lowerMatrix[i][j] * self.output1[j]
            self.output1[i] = round(self.y[i] - sum, self.precision)
             
    def backSubstitution(self):
        if self.no_error == True :
            self.output2[self.output2.shape[0]-1] = round(self.output1[self.output2.shape[0]-1]/self.inputMatrix[self.output2.shape[0]-1][self.output2.shape[0]-1] , self.precision)
            for i in range(self.inputMatrix.shape[0]-2, -1, -1):
                sum = 0
                for j in range(i+1, self.inputMatrix.shape[0]):
                    sum += self.inputMatrix[i][j] * self.output2[j]
                self.output2[i] = round((self.output1[i] - sum)/self.inputMatrix[i][i], self.precision)

            return self.output2
        else :
            return "error"
                
#Sample test    
# x = np.array([[0.0 for i in range(4)] for j in range(4)])
# x[0][0] = 25
# x[0][1] = 5
# x[0][2] = 1
# x[0][3] = 2


# x[1][0] = 64
# x[1][1] = 8
# x[1][2] = 1
# x[1][3] = 5

# x[2][0] = 144
# x[2][1] = 12
# x[2][2] = 1
# x[2][3] = 6

# x[3][0] = 144
# x[3][1] = 12
# x[3][2] = 1
# x[3][3] = 6


# y = np.array([8, 1, 10, 11])

# print("Equation Form : Ax=b\nA:", x, "\nb:\n", y)
# gauess = GaussElimination(x, y, 4)
# gauess = GauessJordan(x, y, 4)
# gauess = LUDolittle(x, y, 4)


