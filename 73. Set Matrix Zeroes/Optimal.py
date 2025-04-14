# Time Complexity: O(2*(N*M))
# Space Complexity: O(1)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# ref: https://youtu.be/N0MgLvceX7M?t=855&feature=shared
colIndex0=1
lenOfRow=len(matrix[0])
for rowIndex in range(len(matrix)):
    for numIndex in range(len(matrix[rowIndex])):
        if(matrix[rowIndex][numIndex]==0):
            matrix[rowIndex][0]=0
            if(numIndex==0):
                colIndex0=0
            else:
                matrix[0][numIndex]=0
# We shode no loop the index 0 because we are using it to store the information of the first row and first column
for rowIndex in range(1,len(matrix)):
    tempIsRowZero=matrix[rowIndex][0]==0
    for numIndex in range(1,len(matrix[rowIndex])):
        if(matrix[rowIndex][numIndex]!=0 and (tempIsRowZero or matrix[0][numIndex]==0)):
            matrix[rowIndex][numIndex]=0
if(matrix[0][0]==0):
    matrix[0]=[0]*lenOfRow
if(colIndex0==0):
    for rowIndex in range(len(matrix)):
        if(matrix[rowIndex][0]!=0):
            matrix[rowIndex][0]=0

