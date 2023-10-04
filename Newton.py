import math
import numpy as np
from sympy import *
import random
import matplotlib.pyplot as plt
from sympy.plotting import plot as symplot
from sympy import plot

class Newton:
    def __init__(self, equation, intitialGuess='a', precision=10000.5, iterations=100, AbsoluteRelativeError=0.00001):
        
        if (precision == "") :
            precision = 10000.5
        if iterations == "" :
            iterations = 10000
        if intitialGuess == "" :
            intitialGuess = 'a'
        else :
            intitialGuess = float(intitialGuess)
            
        if AbsoluteRelativeError == "" :
            AbsoluteRelativeError = 0.00001
        
        precision = int(precision)
        iterations = int(iterations)
        AbsoluteRelativeError = float(AbsoluteRelativeError)
        
        
        equation = self.modify(equation)
        print(equation)
        self.xSymbol = Symbol('x')
        
        self.equation = sympify(equation)  # parse_expr(equation)

        print("equation ", equation)
        self.derivative = self.getDerivative()

        print("derivative ", self.derivative)
        self.precision = precision
        self.iterations = iterations
        self.AbsoluteRelativeError = AbsoluteRelativeError
        self.xiPlus1 = 2.3
        self.xi = intitialGuess

    def modify(self, equation):
        equation = equation.replace("^","**")
        
        tempList = equation.split('=')
        mod = tempList[1]
        if mod[0]!='-':
            mod = '+'+mod
        
        print(mod)
        new = list(mod)
        for i in range (0, len(mod)):
            
            if new[i] =='+' or new[i] == '-' :
                if new[i] == '+':
                    new[i] = '-'
                else:
                    new[i] = '+'
                    
        mod = ''.join(new)
            
        print(mod)        
        tempList[1] = ''.join(mod)
        equation    = ''.join(tempList)   
        print(equation)      
        for i in range (0, len(equation)):
            if equation[i] == 'x' and i!=0 and equation[i-1].isdigit():
                temp = list(equation)
                temp.insert(i, '*')
                equation = ''.join(temp)
                
        
        
        print(equation)        
        return equation
        
        
        
    def getDerivative(self):
        # print(type(equation))s
        #equ = parse_expr(equation)
        der = self.equation.diff(self.xSymbol)
        # print(type(der))
        return der

    def getInitialGuess(self):
        while(True):
            initial = random.uniform(0, 100)
            # print(initial)
            y = self.evaluate(self.derivative, initial)
            if(y != 0):
                print("initial guess ", initial)
                self.xi = initial
                break

    def algorithm(self):
        if self.xi == 'a':
            self.getInitialGuess()

        x = self.iterations
        #self.xi = 0.05
        #x = 3
        for i in range(0, x):

            if x != 0 and self.getAbsoluteRelativeError() and (self.evaluate(self.equation, self.xiPlus1) <= 10**-10):
                break

            temp = self.evaluate(self.equation, self.xi) / \
                self.evaluate(self.derivative, self.xi)
            if self.precision != 10000.5:
                temp = self.getPrecision(temp)

            self.xiPlus1 = self.xi - temp
            if self.precision != 10000.5:
                self.xiPlus1 = self.getPrecision(self.xiPlus1)

            self.xi = self.xiPlus1
            
            

        evalOfAns = self.evaluate(self.equation, self.xiPlus1)
        # print(sys.float_info.epsilon)
        ans = self.equation.subs(self.xSymbol, self.xiPlus1)

        print(evalOfAns < 10**-6)
        if evalOfAns < 10**-6:
            print(self.xiPlus1)
        else:
            print(
                "Solution wasn't found! may be the initail guess or the function itself")
            print(self.xiPlus1)

        self.plot()
        print("in algorithm")
        return self.xiPlus1

      

    def plot(self):
        e = symbols('e')
        x = symbols('x')
        self.derivative = self.derivative.subs(e, exp(1))
        plot(self.derivative,(x, -50, 50), show = false).save('/home/gad/Desktop/newton_raphason.png')
        
            #                                        'C:/Users/es-abdoahmed022/numerical_project/static/confusion_matrix.png')
        #symplot(self.derivative, show = false)

    def getPrecision(self, val):
        val = round(val, self.precision)
        return val

    def getAbsoluteRelativeError(self):
        # print(self.xiPlus1)
        # print("################################")
        # print(self.xi)
        Abserror = (self.xiPlus1 - self.xi) / self.xiPlus1
        Abserror *= 100
        #print("Absolute error ", Abserror)
        if(Abserror < self.AbsoluteRelativeError):
            return true
        return false

    def evaluate(self, equation, value):
        #print(self.derivative,"  ",value)
        ans = equation.subs(self.xSymbol, value)
        # print(ans)

        e = symbols('e')
        ans = ans.subs(e, exp(1))
        ans = ans.evalf()
        # sprint(ans)
        return ans



# while(true):
#     equ = input("Enter The equation ")

#     n = Newton(equ)
#     n.algorithm()





    #eq = sympify('e**x')
    # print(eq)
    # print(n.evaluate(sin(x),math.pi/6))
