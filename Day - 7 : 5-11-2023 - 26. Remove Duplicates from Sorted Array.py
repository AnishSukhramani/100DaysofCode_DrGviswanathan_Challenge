class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        
        # Clear the original 'nums' list and copy the unique elements from 'temp'
        nums.clear()
        nums.extend(temp)
        
        return len(nums)


# The Python code defines a class named `Solution` with a method called `removeDuplicates`. This method takes a list of integers, `nums`, as input and is supposed to remove any duplicate elements from the list, ensuring that the modified list only contains unique elements. The method returns the length of the modified list, which essentially represents the number of unique elements in the original list.

# Here's a breakdown of what the code does:
# 1. It initializes an empty list called `temp`. This list will be used to store the unique elements from the `nums` list.
# 2. It iterates through the elements in the `nums` list using a for loop.
# 3. For each element in `nums`, it checks if that element is already present in the `temp` list. If it's not in `temp`, the code appends it to `temp`. This check ensures that only unique elements are added to the `temp` list.
# 4. After processing all elements in the `nums` list, the code clears the original `nums` list using the `clear` method. This effectively empties the original list.
# 5. It then extends the `nums` list with the elements from the `temp` list. This populates the `nums` list with the unique elements found in `temp`.
# 6. Finally, the method returns the length of the modified `nums` list, which is now equal to the number of unique elements.

# In summary, this code takes an input list of integers, removes duplicates, and returns the number of unique elements in the original list. It uses a temporary list to store the unique elements during the process and then copies them back to the original list. This approach ensures that the original list is modified in place, and any duplicate elements are removed.
