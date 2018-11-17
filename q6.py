#-------------------------------------------------------------------------------
# Name:        Question 6,Assignment 5, CS-510
# Purpose:      using Python 2.7 and NOT Python 3.
#               Method used is Recursion+Memoization
#
# Author:      Muzammil Abdul Rehman
#
# Created:     17/03/2014
# Copyright:   (c) Muzammil 2014
# Licence:     15100104
#-------------------------------------------------------------------------------
matrix=[]
matMax=0
matrixDict={}

def createMatrix():
    global matrix;global matMax
    matFile=open('matrix.txt','rU')
    for everyLine in matFile:
        curRow=everyLine.split('\n')
        curRow=curRow[0].split(',')
        curRow=map(int,curRow)
        matrix.append(curRow)
    matMax=len(matrix)-1

def getMatrixMinSum(i,j):
    global matrixDict
    global matrix
    if(i==matMax and j==matMax):
        return matrix[i][j]
    if(i==matMax):
        if (i,j+1) not in matrixDict.keys():
            matrixDict[(i,j+1)]=getMatrixMinSum(i,j+1)
        return matrix[i][j]+matrixDict[(i,j+1)]
    if(j==matMax):
        if (i+1,j) not in matrixDict.keys():
            matrixDict[(i+1,j)]=getMatrixMinSum(i+1,j)
        return matrix[i][j]+matrixDict[(i+1,j)]
    if (i,j+1) not in matrixDict.keys():
        matrixDict[(i,j+1)]=getMatrixMinSum(i,j+1)
    if (i+1,j) not in matrixDict.keys():
        matrixDict[(i+1,j)]=getMatrixMinSum(i+1,j)
    return matrix[i][j]+min(matrixDict[(i+1,j)],matrixDict[(i,j+1)])

def main():
    global matrix
    global matrixDict
    createMatrix()
    minPathSum=0;i=0;j=0
    minPathSum=getMatrixMinSum(i,j)
    print "The Shortest Path Sum: ",minPathSum

if __name__ == '__main__':
    main()
