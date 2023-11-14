class Solution(object):
    def singleNumber(self, nums):
        t1 = []
        for i in range(len(nums)):
            if nums[i] not in t1:
                t1.append(nums[i])
            else:
                t1.remove(nums[i])
        return t1[0]
      
# This Python class contains a method called `singleNumber` that takes in a list of numbers called `nums`. It aims to find the single number that appears only once in the list, while all other numbers appear twice.
# It uses a list `t1` to keep track of numbers encountered in the input list. It iterates through each number in the input list. If the number is not already in `t1`, it adds it. If the number is already in `t1`, it removes it. 
# Finally, the method returns the first (and only) element in `t1`, which is the number that appears only once in the input list.
