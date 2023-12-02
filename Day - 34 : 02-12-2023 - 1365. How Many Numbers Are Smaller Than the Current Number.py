class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        arr=[]
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j] < nums[i]:
                    count+=1
            arr.append(count)
        return arr

# This Python class contains a method called `smallerNumbersThanCurrent` which takes a list of numbers called `nums` as input. 

# Inside the method:
# - It first finds the length of the input list.
# - It initializes an empty list called `arr`.
# - It iterates through each element in the `nums` list using a nested loop to compare each element with the others.
# - For each element, it counts how many numbers in the list are smaller than the current element by comparing it to every other number in the list.
# - It appends the count of smaller numbers for each element to the `arr` list.
# - Finally, it returns the `arr` list containing the count of smaller numbers for each element in the input list. 

# This function essentially computes, for each element in the input list, how many numbers in the list are smaller than that particular element and returns a new list containing these counts.
