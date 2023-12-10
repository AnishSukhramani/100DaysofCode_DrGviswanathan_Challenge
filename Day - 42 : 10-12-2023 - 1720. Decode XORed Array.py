class Solution(object):
    def decode(self, encoded, first):
        arr=[first]
        for i in range(len(encoded)):
            arr.append(encoded[i]^arr[i])
        return arr
