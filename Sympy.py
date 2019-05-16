#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:27:07 2019

@author: brett
"""



"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
comments: https://docs.sympy.org/latest/tutorial/matrices.html
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

"""
#Matrix
from sympy import *
init_printing(use_unicode=True)



# Matrix Creation
#    Creates a matrix of ones.
ones(5,2)

#   Creates matrix
m = Matrix([[1,8],[2,8]])
n = Matrix([3,3])

#Matrix Shape
m
n
#Matrix Multiplicatin
n * m

# Accessors
m.row(0)
m.col(0)

#Matrix Transpose

    #non mutating
m.T
m.transpose()

m
# Compute the determinant 
m.det()

# Put a matrix into reduced row echelon form
m.rref()
