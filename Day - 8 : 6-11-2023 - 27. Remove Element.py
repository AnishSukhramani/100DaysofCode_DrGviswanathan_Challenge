class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
            else:
                i += 1

        return n

# This Python code defines a class `Solution` with a method `removeElement` that takes a list of integers `nums` and an integer `val`. The method removes all occurrences of the value `val` from the list `nums` and returns the new length of the modified list.
# It uses a while loop with an index `i` to iterate through the list. If the current element at index `i` is equal to the target value `val`, it removes that element from the list and decrements the length `n`. If the element is not equal to `val`, it increments `i`. The loop continues until all instances of `val` are removed, and the length of the modified list is returned.
