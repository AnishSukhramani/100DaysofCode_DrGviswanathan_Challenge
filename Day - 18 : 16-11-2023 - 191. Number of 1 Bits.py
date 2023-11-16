class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary_string=bin(n)
        return bin(n).count("1")

# Certainly! The given Python code defines a class `Solution` with a method `hammingWeight`. This method calculates the number of '1' bits in the binary representation of an input integer `n` using Python's `bin` function to convert `n` to binary and then counting the occurrences of '1's in that binary representation using `count("1")`. The method returns this count, giving the Hamming weight of the input integer `n`.
