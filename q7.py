#-------------------------------------------------------------------------------
# Name:        Question 7,Assignment 5, CS-510
# Purpose:      using Python 2.7 and NOT Python 3.
#               Method used is Dynamic Programming
#              
# Author:      Muzammil Abdul Rehman
#
# Created:     17/03/2014
# Copyright:   (c) Muzammil 2014
# Licence:     15100104
#-------------------------------------------------------------------------------
matLen=0
matMax=matLen-1

def createMatrix():
    global matLen,matMax
    matrix=[]
    matFile=open('matrix.txt','rU')
    for everyLine in matFile:
        curRow=everyLine.split('\n')
        curRow=curRow[0].split(',')
        curRow=map(int,curRow)
        matrix.append(curRow)
    matLen=len(matrix)
    matMax=matLen-1
    return matrix

def createPathMatrix(matrix):
    global matLen,matMax
    #create initial matrix O(n^2)
    pathMatrix=[]
    for i in range(matLen):
        pathMatRow=[float('inf') for j in range(matLen)]
        pathMatrix.append(pathMatRow)
    #populate it
    #the end column
    for i in range(matLen):
        pathMatrix[i][matMax]=matrix[i][matMax]
    #the second last column to the first one.
    colTraversalList=range(matMax)
    colTraversalList.reverse()
    for j in colTraversalList:
        #repeat n times since we have to minimize, ie go n times in worst case that the top is dependent on the bottom element in a column or vice versa.(You know like networks)
        for k in range(matLen):
            pathMatrix=computeColumnValues(pathMatrix,matrix,j)
    return pathMatrix

def computeColumnValues(pathMatrix,matrix,j):
    for i in range(matLen):#just like networks(IP layer).
        pathMatrix[i][j]=min(pathMatrix[i][j],computeCellValue(i,j,matrix,pathMatrix))
    return pathMatrix

def computeCellValue(i,j,matrix,pathMatrix):
    if i==0:
        return matrix[i][j]+min(pathMatrix[i+1][j],pathMatrix[i][j+1])
    if i==matMax:
        return matrix[i][j]+min(pathMatrix[i-1][j],pathMatrix[i][j+1])
    return matrix[i][j]+min(pathMatrix[i-1][j],pathMatrix[i+1][j],pathMatrix[i][j+1])


def main():
    global matLen,matMax
    matrix=createMatrix()
    minPathSum=0
    pathMatrix=createPathMatrix(matrix)
    minPathSum=min([pathMatrix[i][0] for i in range(matLen)])
    print "The Shortest Path Sum: ",minPathSum

if __name__ == '__main__':
    main()
