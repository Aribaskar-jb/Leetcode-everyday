# Time Complexity: O(2*(N*M))
# Space Complexity: O(N) + O(M)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rowMap=set()
colMap=set()
for rowIndex in range(len(matrix)):
    for numberIndex in range(len(matrix[rowIndex])):
        if(matrix[rowIndex][numberIndex]==0):
            if(rowIndex not in rowMap):
                rowMap.add(rowIndex)
            if(numberIndex not in colMap):
                colMap.add(numberIndex)
for rowIndex in range(len(matrix)):
    if(rowIndex in rowMap):
        matrix[rowIndex]=[0]*(len(matrix[rowIndex]))
        rowMap.remove(rowIndex)
    else:
        for numberIndex in range(len(matrix[rowIndex])):
            if(numberIndex in colMap):
                matrix[rowIndex][numberIndex]=0