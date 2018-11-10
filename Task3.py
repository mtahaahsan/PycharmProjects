list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
myList = []
finalMatrix = []

myMatrix = [list1, list2, list3, list4]
myMatrix2 = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
myNotMatrix = [list1, list2, [1]]

def isMatrix(matrix):
    for i in range(len(matrix)-1):
        if(len(matrix[i]) == len(matrix[i+1])):
            continue
        else:
            return False
    return True

def shapeMatrix(matrix):
    return (len(matrix[1]), len(matrix))

def addMatrixHelp(list1, list2):
    helpAddlist = []
    for i in range(len(list1)):
        helpAddlist.append(list1[i] + list2[i])
    return helpAddlist

def addMatrix(matrix, matrix2):
    for i in range(len(matrix)):
        addlist1 = matrix[i]
        addlist2 = matrix2[i]
        finalMatrix.append(addMatrixHelp(addlist1,addlist2))
    print(finalMatrix)

def multMatrixHelp(multLis1, multList2):
    helpMultList = []
    for i in range(len(multLis1)):
        helpMultList.append(multLis1[i] * multList2[i])
    return sum(helpMultList)

def transMatrix(matrix):
    newMatrix = []
    for index in range(len(matrix[1])):
        newList=  []
        for x in matrix:
            newList.append(x[index])
        newMatrix.append(newList)
    return newMatrix

def multMatrix(matrix1, matrix2):
    multMatrix = []
    newList = []
    sumList = []
    matrix2 = transMatrix(matrix2)
    for i in range(len(matrix1)):
        multList1 = matrix1[i]
        print(multList1)
        for z in range(len(matrix1)-1):
            multList2 = matrix2[z]
            sumList.append(multList1[z] * multList2[z])
            newList.append(sum(sumList))

        multMatrix.append(multMatrixHelp(multList1, multList2))
    print(multMatrix)





print(shapeMatrix(myMatrix))
print(isMatrix(myMatrix))
# transMatrix(myMatrix2)
# addMatrix(myMatrix, myMatrix)
multMatrix(myMatrix, myMatrix2)