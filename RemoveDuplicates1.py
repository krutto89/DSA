def removeDuplicate(nums):
    if not nums:
        return 0
    j =1
    

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j]= nums[i]

            j +=1

    return j

nums = [0,1,1,2,3,4,4,7,8]
k = removeDuplicate(nums)
print(k)
print(nums[:k])
