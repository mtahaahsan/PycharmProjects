list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
myMatrix = [list1, list2, list3, list4]
myMatrix2 = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
myNotMatrix = [list1, list2, [1]]



# Takes in a matrix and checks if the length of any list in the matrix has the same size as the element in front, if the
# statement is true, then the loop continues to run, for any instance where the statement is false, the loop stops and
# returns false, if the entire loop has finished, the method returns true
def isMatrix(matrix):
    for i in range(len(matrix) - 1):
        if (len(matrix[i]) == len(matrix[i + 1])):
            continue
        else:
            return False
    return True


print(isMatrix(myMatrix))
print(isMatrix(myNotMatrix))


# Takes in a matrix and returns a tuple with the length of the first list in the matrix (rows), and then the length of
# the matrix (columns)
def shapeMatrix(matrix):
    return (len(matrix[1]), len(matrix))


print(shapeMatrix(myMatrix))


# Takes in two lists and returns the sum of two lists as a list
def addMatrixHelp(list1, list2):
    helpAddlist = []
    for i in range(len(list1)):
        helpAddlist.append(list1[i] + list2[i])
    return helpAddlist


# Takes in two matrices, uses a loop to take each list in the matrices, passes those list into addMatrixHelp, the return
# of that method is appended to finalMatrix, and finalMatrix is returned once the two matrices have been added
def addMatrix(matrix, matrix2):
    finalMatrix = []
    for i in range(len(matrix)):
        addlist1 = matrix[i]
        addlist2 = matrix2[i]
        finalMatrix.append(addMatrixHelp(addlist1, addlist2))
    return finalMatrix

print(addMatrix(myMatrix, myMatrix))


# Takes in two lists and returns the product of two lists as a list
def multMatrixHelp(multLis1, multList2):
    helpMultList = []
    for i in range(len(multLis1)):
        helpMultList.append(multLis1[i] * multList2[i])
    return sum(helpMultList)


# Takes in a matrix and transposes it by appending all of the same index of all the lists in the matrix to a new list
# and then appending those lists to another empty list to create a matrix
def transMatrix(matrix):
    newMatrix = []
    for index in range(len(matrix[1])):
        newList = []
        for x in matrix:
            newList.append(x[index])
        newMatrix.append(newList)
    return newMatrix


# Takes two matrices and takes the head of each matrix, and then takes the first element of each list, and multiplies
# them, and adds them to sum, once it's done iterating through the lists, it adds the sum to another list, and once
# that second matrix is done, the first matrix is iterated and everything repeated
def multMatrix(matrix1, matrix2):
    finalMatrix = []
    matrix2 = transMatrix(matrix2)
    print(matrix2)
    for x in range(len(matrix1)):
        multlist1 = matrix1[x]
        finalList = []
        for y in range(len(matrix2)):
            multlist2 = matrix2[y]
            sum = 0
            for z in range(len(multlist1)):
                sum = sum + (multlist1[z] * multlist2[z])
            finalList.append(sum)
        finalMatrix.append(finalList)
    return finalMatrix

print(multMatrix(myMatrix,myMatrix2))
