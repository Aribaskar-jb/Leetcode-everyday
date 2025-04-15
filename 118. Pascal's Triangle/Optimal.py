# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

if(numRows==1):
    return [[1]]
elif(numRows==2):
    return [[1],[1,1]]
elif(numRows>2):
    ans=[[1],[1,1]]
    for index in range(3,numRows+1):
        tempArray=[1]
        leftPointer=0
        leftPointerTow=1
        lastValue=ans[-1]
        for preValue in range(index-2):
            tempArray.append(lastValue[leftPointer]+lastValue[leftPointerTow])
            leftPointer=leftPointerTow
            leftPointerTow+=1
        tempArray.append(1)
        ans.append(tempArray)
return ans