from evaluate import evaluation
from plot import plot
from math import *
import sys
#%%

class Bracketing():
    
    XR = []
    XU = []
    XL = [] 
    def __init__(self, exp, algorithm, L, U, percision = 5, min_error = 0.00001):

        if (percision == "") :
            percision = 5
        if min_error == "" :
            min_error = 0.00001

        percision = int(percision)
        L = float(L)
        U = float(U)
        min_error = float(min_error)

        self.exp = exp # the expression
        self.algorithm = algorithm #tyep of used algorithm(bisection, regula-falsi)
        self.Xl = L #the minimum value
        self.Xu = U #maximum value
        self.percision = percision #percision the user chose
        self.min_error = min_error #the erorr the user wants

        self.number_of_iteration = 0 #count number of iteration
        self.calc_error = 0  #flag to start count the error
        self.error = 1  #the erorr at each state
        self.temp = 0 #temp variable to hold the old value of x to calc the error
        

    def expression(self, x):
        try:
                return evaluation.get_expression(self.exp, x) #get the evaluation of the expression
        except:
                return 'sorry there is error in the evaluation'

    #check that f(Xl) * f(Xu) is negative:
    # take param Xu, Xl which is the values to check, and fun which is the function of the question
    def brackets_cond(self, Xu, Xl, fun):
            return self.expression(Xl) * self.expression(Xu) < 0

    
    
    #tack old value of Xr and new value to check the error 
    def calculate_error(self, Xr_new, Xr_old):
            if Xr_new != 0:
                return round(abs((Xr_new-Xr_old)/ Xr_new), self.percision)

    def find_root(self):

        #check that there is available bracketing
        if not(self.brackets_cond(self.Xu, self.Xl, self.expression)):
                return "there is no bracketing in this section"

        #get Xr with bisection method (the mean of xu, xl)
        if self.algorithm == 'bisection':
                try:
                        Xr = round((self.Xl + self.Xu) / 2, self.percision) #calculate Xr in the beginning iteration
                except:
                        print('there is error...division by zero the input is not suitable')
                        sys.exit()


        #get Xr using Regula-Falsi 
        elif self.algorithm == 'Regula-Falsi':
                try:
                        fl = self.expression(self.Xl)
                        fu = self.expression(self.Xu)
                        Xr = round(((self.Xl*fu) - (self.Xu*fl)) / (fu - fl), self.percision)
                except:
                        print('there is error...division by zero the input is not suitable')
                        sys.exit()

        
        print('Xr is: {}'.format(Xr)) #print Xr
        self.XR.append(Xr) #save values of Xr
        self.XU.append(self.Xu) #save values of Xu
        self.XL.append(self.Xl) #save values of Xl

        
        if self.calc_error == 1: #if it's not the first iteration calculate the error
                self.error = self.calculate_error(Xr, self.temp) #calculate error between old Xr and the new one
                print("error is: {}".format(self.error)) #print the error
        
        self.calc_error = 1 #turn to 1 after first iteration so we can calculate the error after that
        self.number_of_iteration += 1
        
        if self.expression(Xr) == 0 or self.error <= self.min_error: #stop if we find tha exact answer or if we reach the allowed error
                plot(self.algorithm, self.exp).plot(self.XR, self.XU, self.XL)
                return Xr

        elif self.brackets_cond(self.Xl, Xr, self.expression): #if the root in the lower area
                self.temp = Xr
                self.Xu = Xr
                return self.find_root()

        else: #if the root in the upper area
                self.temp = Xr
                self.Xl = Xr
                return self.find_root() 
        
       
                

        


# exp = 'x^3'
# xu = -2
# xl = 3

# root = Bracketing(exp, 'bisection', xl, xu,5, 0.001)
# cond = root.find_root()
# print(cond)



# %%
