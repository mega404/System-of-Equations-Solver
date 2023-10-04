from math import*

class evaluation():

    def get_expression(expression, x):
        expression = expression.replace("^", '**') #get the correct sign for the exponential
        expression = expression.replace("=", '-') #change the = to - just like we add the number to the other side of the equation
        
        #rebalce any value in the keys in the string with its value 
        globals= { "square_root": sqrt,
                    'sqrt': sqrt,
                    'pi': pi, 
                    'exp': exp,
                    'e': exp, 
                    'tan':tan, 
                    'sin': sin,
                    'cos': cos,
                    'x' : x,
                    'z':x,
                    'y':x}
        
        return eval(expression, globals) #return the evaluation





