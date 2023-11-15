class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1
        return result  
# This Python code defines a class `Solution` with a method `reverseBits`. The method takes an integer `n` as input and reverses its bits (binary digits) to obtain a new integer.
# Here's a brief explanation of the code:
# 1. `result` is initialized to 0, which will store the reversed bits of the input.
# 2. A loop runs 32 times since integers typically have 32 bits.
# 3. Inside the loop:
#    - `result` shifts its bits to the left by 1 position (`result << 1`), making space for the next bit.
#    - The least significant bit (the rightmost bit) of `n` is obtained by performing a bitwise AND operation with 1 (`n & 1`), and this bit is appended to `result` using a bitwise OR operation (`|`).
#    - `n` is shifted to the right by 1 position (`n = n >> 1`) to extract the next bit for processing.
# 4. After the loop, the reversed bit sequence stored in `result` is returned as an integer.
# In summary, this method reverses the bit sequence of the input integer `n` by iterating through its bits and constructing a new integer with the reversed bit order.
