#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:55:21 2021

@author: gad
"""
import numpy as np
from itertools import permutations

class iterative:
    
    #Constructor to instialize the object
    def __init__(self, numOfVar, coefMat, bMat ,precision,absolute_Error, iterations, initial):
        self.numOfVariables = numOfVar
        #will use [[0],[0],[0],...] as initial guess if an intial guess is not provided


        if (precision == "") :
            precision = 5
        if iterations == "" :
            iterations = 10000
        if initial == "" :
            initial = [[1.0]]
        if absolute_Error == "" :
            absolute_Error = 0.0001

        if(initial == [[1.0]]):
            self.answer  = np.array([[1.0]*self.numOfVariables]).T
             #np.array([[1.0,0.0,1.0]]).T
         
        else:
            self.answer  = np.array([[initial]*self.numOfVariables]).T
            ''' 
            !!!!!!!!! 
            '''

        self.prev_iteration = np.array([[0.0]*numOfVar]).T
        self.coeffMat = coefMat
        self.bMat = bMat
        self.Error = float(absolute_Error)
        self.iterations = int(iterations)
        self.precision = int(precision)
        self.all_permutations = []
        self.all_permutations_B = []
#        print(self.coeffMat)
#        print(self.bMat)
#        print(self.answer)
#        print(self.prev_iteration)
#        print(self.Es_conv)
#        print(self.iterations)
        
        
    def precision(self, num):
        ans = round(num, self.precision)
        return ans
        
    def check_convergence(self):
        conv = 0
        for i in range (0, self.numOfVariables):
            Ea = abs((float(self.answer[i][0] - self.prev_iteration[i][0])) / self.answer[i][0])*100
            if( Ea < self.Error):
                conv+=1
                
        if conv == self.numOfVariables:
            return True
        
        return False
    
    
    def Convert_diagonallyD(self):
        row_matrix = np.array(self.coeffMat).tolist()
        row_matrix_B = np.array(self.bMat).tolist()
        rows = list(range(len(row_matrix)))

        for perm in permutations(rows):
            shuffled_rows_matrix = []
            shuffled_rows_matrix_B = []
            for idx in perm:
                shuffled_rows_matrix.append(row_matrix[idx])
                shuffled_rows_matrix_B.append(row_matrix_B[idx])
            self.all_permutations.append( np.array(shuffled_rows_matrix).tolist() )
            self.all_permutations_B.append(np.array(shuffled_rows_matrix_B).tolist() )
            if self.diagonallyD( np.array(shuffled_rows_matrix)):
                return True
        return False
        


    def diagonallyD(self, array):
        sum_of_rows = np.sum(array, axis = 1)
        dominant = 0
        for i in range (0, self.numOfVariables):
            if abs(array[i][i]) >= abs(sum_of_rows[i]-array[i][i]):
                dominant+=1
            if abs(array[i][i]) > abs(sum_of_rows[i]-array[i][i]):
                dominant+=1
                
        # All must be >= and atleast one is > so dominant will be atleast numOfVariables + 1
        if dominant >= (self.numOfVariables + 1):
            return True
        
        return False
        
        
    def print_answer(self):
        print("The answer is: ")
        print(self.answer)
        
        
    def changeValues(self):
        self.bMat = self.all_permutations_B[len(self.all_permutations_B) - 1]
        self.coeffMat = self.all_permutations[len(self.all_permutations) - 1]
        #print(self.coeffMat)