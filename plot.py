#%%
from evaluate import evaluation
import numpy as np
import matplotlib.pyplot as plt


class plot():
    def __init__(self, algorithm, exp):
        self.algorithm = algorithm #take the algorithm to determint type of the plot
        self.expression = exp #take the expression to use it in plotting
        
    
   #function to evaluate values to plot it    
    def get_y(x, exp):
        y = [] #list to hold the values of y axis to plot
        for i in x:
            y.append(evaluation.get_expression(exp, i)) #get the values and add them to the list
        return y
           
    #function to plot the values
    def plot(self, xr, xl, xu):      
        fig = plt.figure(figsize=(40, 90)) #the big figure to hold all the plots
        for i in range(len(xr)):
            x_values = np.linspace(xl[i], xu[i], 5) #make 5 values between xl, and xu
            y_values = plot.get_y(x_values, self.expression) #get the evaluation of the x values 
            fig.add_subplot(9,5, i+1) #start to plot 
            plt.plot(x_values, y_values) 
            plt.plot([xr[i]] * len(y_values), y_values) #vertical line at Xr
            plt.plot([xu[i]] * len(y_values), y_values ) #vertical line at Xu
            plt.plot([xl[i]] * len(y_values), y_values ) #vertical line at Xl 
            if self.algorithm == 'Regula-Falsi':
                x_slope = [x_values[0], x_values[9]] #in case False-Position we plot a line between Xu and Xl to get Xr
                y_slope = [y_values[0], y_values[9]] #these two lines represtns the co-ordinaiton of 2 points of the line bewteen Xr and Xl
                plt.plot(x_slope, y_slope) 
            
        
        plt.savefig('/home/gad/Desktop/allSteps.png', bbox_inches='tight') #save the image so we can use it
        
            
# %%
