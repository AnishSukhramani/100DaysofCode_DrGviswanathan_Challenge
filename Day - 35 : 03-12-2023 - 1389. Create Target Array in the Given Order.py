class Solution(object):
    def createTargetArray(self, nums, index):
        # target=[]
        # for i in range(len(index)):
        #     target.insert(index[i], nums[i])
        # return target
        target = []
        for num, idx in zip(nums, index):
            target.insert(idx, num)
        return target
# This Python class named `Solution` contains a method called `createTargetArray` that takes in two lists as parameters: `nums` and `index`. The objective of this method is to create a target array based on the elements in the `nums` list and their corresponding insertion indices provided in the `index` list.

# The commented-out code at the beginning of the method indicates an alternative approach to achieving the same goal using a `for` loop to iterate through the `index` list. For each index value, it inserts the corresponding element from the `nums` list into the `target` array at that specific index.

# However, the active part of the method uses a more concise method by employing `zip`. `zip` combines elements from both `nums` and `index` lists iteratively, allowing simultaneous traversal. For each pair of elements (num, idx) obtained from `zip(nums, index)`, it performs an insertion of the `num` element into the `target` list at the specified `idx` position using the `insert` method.

# Finally, the method returns the `target` array, which now contains elements from the `nums` list inserted at positions specified by the `index` list.
