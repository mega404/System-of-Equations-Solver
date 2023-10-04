import math
from sympy import symbols
from sympy import plot 
class ModifyEquation:
    def __init__(self, equation):
        self.equation = equation
    def modify(self):
        self.equation = self.equation.replace("^", "**")
        self.equation = self.equation.replace("sin", "math.sin")
        self.equation = self.equation.replace("cos", "math.cos")
        self.equation = self.equation.replace("exp", "math.eXp")
        temp = self.equation.split("=")
        self.equation = temp[0] 
        if (len(temp) == 2):
            self.equation += '-'+temp[1]
        for i in range(1, len(self.equation)):
            if (self.equation[i] == 'x' and self.equation[i-1].isdigit()):
                temp = list(self.equation)
                temp.insert(i, "*")
                self.equation = ''.join(temp) 
        return self.equation

class SecantMethod(ModifyEquation):
    def __init__(self, equation, xi_1, xi, es=0.00001, precision=5):
        print("Secant method constructor!")

        if (es == "") :
            es = 0.00001
        if (precision == "") :
            precision = 5

        precision = int(precision)
        es = float(es)
 
        self.es = es
        self.xi = xi
        self.xi_1 = xi_1 
        self.precision = precision
        self.equation = ModifyEquation(equation).modify()
        #self.secant()
    def secant(self):
        ea = 10e5
        i = 1
        while(ea > self.es):
            i +=1
            self.fxi = self.computEquation("self.xi")
            self.fxi_1 = self.computEquation("self.xi_1")
            self.xi2 = round(self.xi-self.fxi * (self.xi-self.xi_1)/(self.fxi-self.fxi_1), self.precision)
            ea = self.computEa(self.xi2, self.xi)
            self.xi_1 = self.xi
            self.xi = self.xi2 
        print(self.xi2, "   number of iterations = ",i)
        self.plot()
        return self.xi2

    def computEa(self, current, previuos):
        return abs(((current-previuos)/current)*100)
    
    def computEquation(self, x):
        eqn = self.equation.replace('x', x)
        eqn = eqn.replace('X', 'x')
        
        result = (eval(eqn))
        return result
    def plot(self):
        x = symbols("x")
        eqn = self.equation.replace('X', 'x')
        eqn = eqn.replace("math.", "")
        plot(eqn, (x, -10, 10)).save('/home/gad/Desktop/secant.png')
             
       
class fixed_point(ModifyEquation):
    def __init__(self, equation, xi, es= 0.00001,precision= 5):

        if (es == "") :
            es = 0.00001
        if (precision == "") :
            precision = 5

        precision = int(precision)
        es = float(es)

        self.equation = ModifyEquation(equation).modify()
        self.precision = precision
        self.es = es
        self.xi = xi
        #self.getGX()
        #self.computeFixedPoint()
    def getGX(self):
        self.equation = self.equation +"+x"
    def computeFixedPoint(self):
        ea = 10e10
        iterations = 0
        xi2 = 0
        while(ea > self.es):
            xi2 = self.evaluateEquation("self.xi")
            ea = abs((((xi2-self.xi)/xi2)*100))
            self.xi = xi2
            iterations += 1
            if(iterations > 1000):
                print("Equation diverge")
                break 
        print(self.xi, "     number of iterations = ", iterations)
        self.plot()
        return self.xi

    def evaluateEquation(self, x):
       x = self.xi 
       eqn = self.equation.replace('X', 'x')
       result = round(eval(eqn), self.precision)
       return result
    def plot(self):
         x = symbols("x")
         eqn = self.equation.replace('X', 'x')
         eqn = eqn.replace("math.", "")
         plot(eqn, (x, -10, 10)).save('/home/gad/Desktop/fixed.png')
  




        
      
        
        
        
        
        
        
        
        
        
        
        