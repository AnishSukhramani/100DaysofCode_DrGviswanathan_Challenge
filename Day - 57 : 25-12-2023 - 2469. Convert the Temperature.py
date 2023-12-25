class Solution(object):
    def convertTemperature(self, celsius):
        # a=celsius + 273.15
        # b=celsius * 1.80 + 32.00
        # answer=[a,b]
        # return answer
        return [celsius + 273.15, celsius * 1.80 + 32.00]
