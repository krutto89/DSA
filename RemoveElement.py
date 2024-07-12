def removeElement(nums, val):
    j =0 
    # traverse all the elements of the nums array
    for i in range(len(nums)):
        if nums[i] != val :
            nums[j] =nums[i]
            j +=1
    return j

nums = [1,2,3,4,5,4,7,4,9]
val = 4
k = removeElement(nums,val)
print(k)
print(nums[:k])
