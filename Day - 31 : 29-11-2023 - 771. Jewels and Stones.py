class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c=0
        for j in range(len(stones)):
            if stones[j] in jewels:
                c+=1
        return c

# This Python code defines a class Solution that contains a method numJewelsInStones. The purpose of this method is to count the number of jewels present in a collection of stones.

# Let's break down the code:

# def numJewelsInStones(self, jewels, stones):: This method takes in two parameters, jewels and stones, representing strings. jewels contains different types of jewels (characters), and stones contains various stones (also characters).

# c = 0: Initializes a counter variable c to keep track of the number of jewels found in the stones.

# for j in range(len(stones)):: Iterates through each index of the stones string.

# if stones[j] in jewels:: Checks if the character at the current index in the stones string exists in the jewels string. If it does, it means that the stone is a jewel, so it increments the counter c by 1.

# Finally, return c at the end of the method returns the total count of jewels found in the stones.

# The logic used here is straightforward. For each stone in the stones collection, it checks if that particular stone exists in the jewels collection. If it does, it increments the counter c. After iterating through all the stones, it returns the total count of jewels found.
