# Time Complexity: O(N)
# Space Complexity: O(1)

tempValue=nums[-1]
tempIndex=len(nums)-1
for i in range(len(nums)-1,-1,-1):
    if(nums[i]<tempValue):
        tempIndex=i
        break
    else:
        tempValue=nums[i]
nextNumber=nums[tempIndex]
if(len(nums)-1==tempIndex):
    nums[0:] = nums[::-1]
else:
    nextNumberIndex=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if(nextNumber<nums[i]):
            nums[tempIndex]=nums[i]
            nums[i]=nextNumber
            break
    nums[tempIndex+1:]=nums[tempIndex+1:][::-1]