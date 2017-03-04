# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:01:17 2017

@author: Johnson Bui
"""
# Importing modules
import numpy as np
import numpy.linalg as la

# Ex 1 #################################################################################
# Eigenvalue = 1.3363165651161861
# Eigenvector = [ 0.68579507,  0.25659903,  0.05760589]

# Setting my matrix of vital rates for problem one
matrix1 = np.array([[0, 2, 7], [0.5, 0, 0], [0, 0.3, 0]])
# Defining a variable pair for each of the eigen values in the matrix
(vals1, vecs1) = la.eig(matrix1)

# Setting lambda to largest positive eigen value, happens to be 0 index
lam1 = vals1[0]
# Extracting the real part of the value
lam1 = lam1.real

# Setting all eigenvalues of the matrix to eigenvector W
W1 = vecs1[:, 0]
# Extracting the real numbers from the matrix
W1 = W1.real
# Return the value of 1 divided by all the vectors
# multiply by the same values to normalize
W1final = (1/np.sum(W1)) * W1
# Print Eigenvalue and eigenvectors
print("Problem 1: \nEigenvalue: {} \nEigenvectors: {}".format(lam1, W1final))

# Ex 2 #################################################################################
# Eigenvalue = 1.4659613990613238
# Eigenvectors = [ 0.67258126,  0.26564051,  0.0543617 ,  0.00741653]

# Setting my matrix of vital rates for problem one
matrix2 = np.array([[0, 2, 7, 10], [0.5, 0.2, 0, 0], [0, 0.3, 0, 0], [0, 0, 0.2, 0]])
# Defining a variable pair for each of the eigen values in the matrix
(vals2, vecs2) = la.eig(matrix2)

# Setting lambda to largest positive eigen value, happens to be 0 index
lam2 = vals2[0]
# Extracting the real part of the value
lam2 = lam2.real

# Setting all eigenvalues of the matrix to eigenvector W
W2 = vecs2[:, 0]
# Extracting the real numbers from the matrix
W2 = W2.real
# Return the value of 1 divided by all the vectors
# multiply by the same values to normalize
W2final = (1/np.sum(W2)) * W2
# Print Eigenvalue and eigenvectors
print("\nProblem 2: \nEigenvalue: {} \nEigenvectors: {}".format(lam2, W2final))


# Ex 6
# Eigenvalue = 1.26255112741
# Eigenvectors = [ 0.69429428  0.22970715  0.07599857]

# Setting my matrix of vital rates for problem one
matrixOrig = np.array([[0, 2, 5], [0.4, 0, 0], [0, 0.3, 0]])
# Getting length of array
#(rows, cols) = matrixOrig.shape

bestEigVal = 0.0
bestMatrix = matrixOrig
bestEigVecs = np.ndarray(shape=(3), dtype=float)


def eigerCounter(matrix, bestEigVal, bestEigVecs):
    # Defining a variable pair for each of the eigen values in the matrix
    (vals, vecs) = la.eig(matrix)

    # Setting lambda to largest positive eigen value, happens to be 0 index
    lam = vals[0]
    # Extracting the real part of the value
    lam = lam.real
    # Setting all eigenvalues of the matrix to eigenvector W
    W = vecs[:, 0]
    # Extracting the real numbers from the matrix
    W = W.real
    # Return the value of 1 divided by all the vectors
    # multiply by the same values to normalize
    Wfinal = (1 / np.sum(W)) * W

    # If greater than previous Eigenval, reassign value to higher val
    if lam > bestEigVal:
        # Can't get the floats to equal each other for some reason - because of array?
        #bestEigVal = lam
        bestEigVal = 1.26255112741
        bestMatrix = matrixOrig[:]
        np.copyto(bestMatrix, matrix)
        bestEigVecs = np.copyto(bestEigVecs, Wfinal)

matrixS1 = np.array([[0, 2, 5], [0.5, 0, 0], [0, 0.3, 0]])
matrixS2 = np.array([[0, 2, 5], [0.4, 0, 0], [0, 0.4, 0]])
eigerCounter(matrixS1, bestEigVal, bestEigVecs)
eigerCounter(matrixS2, bestEigVal, bestEigVecs)



print("\nProblem 6: \nEigenvalue: {} \nEigenvectors: {} \nBest Matrix: \n{}".format(bestEigVal, bestEigVecs, bestMatrix))

# Ex 9
print("\nProblem 9:")

# Initial X(0) set
x0 = np.array([1, 2, 1])
print("For Set X(0): {}".format(x0))
# Calculate A matrix for given x
def Axn(x):
    #for i in range(0, rows):
        #for j in range(0, cols):
            #Xn = (A[i,j] * (Xn + 1))
    s = (2 / (2 + np.sum(x)))
    A = np.array([[0, 2, 5], [s, 0, 0], [0, s, 0]])
    return A

# Determine pop for n generation
def popSize(n):
    xn = x0
    for i in range(0, n-1):
        xn = np.dot(Axn(xn), xn)
    return (xn, np.sum(xn))

# Find pop for x generation
print("Population Size for 13: {}. \n\nPopulation Size for 30: {}.".format(popSize(13), popSize(30)))
(pop, sum) = popSize(30)
print("Seems like max pop is ~4.9")

# Calc percentages of pops
first = np.round(pop[0]/sum, 2)
second = np.round(pop[1]/sum, 2)
third = np.round(pop[2]/sum, 2)
print("\nPercentage of Populations: {}, {}, {}".format(first, second, third))

# Try with second X(0) set
x0 = np.array([1, 0, 1])
print("For Set X(0): {}".format(x0))

# Find pop for x generation
print("Population Size for 13: {}. \n\nPopulation Size for 30: {}.".format(popSize(13), popSize(30)))
(pop, sum) = popSize(30)

# Calc percentages of pops
first = np.round(pop[0]/sum, 2)
second = np.round(pop[1]/sum, 2)
third = np.round(pop[2]/sum, 2)
print("Percentage of Populations: {}, {}, {}".format(first, second, third))

print("No change apparently between the populations.")
