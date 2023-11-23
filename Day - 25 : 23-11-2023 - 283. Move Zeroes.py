class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)

# This Python class Solution contains a method moveZeroes that takes in a list of integers nums as input and aims to move all the zeroes in the list to the end while maintaining the order of the non-zero elements.

# Here's a breakdown of what the method does:

# It iterates through the nums list using a for loop that goes through the indices from 0 to len(nums) - 1.
# For each index i, it checks if the element at that index is equal to 0 (if nums[i]==0).
# If the element at index i is zero, it removes that element from the list using nums.remove(nums[i]). This operation alters the list by removing the first occurrence of the zero in the list.
# After removing the zero, it appends a new zero (nums.append(0)) to the end of the list.
