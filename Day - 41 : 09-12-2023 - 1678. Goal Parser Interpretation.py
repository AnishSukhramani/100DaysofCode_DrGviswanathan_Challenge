class Solution(object):
    def interpret(self, command):
        # str1=command.replace("()", "o")
        # str2=str1.replace("(al)","al")
        # return str2
        return (command.replace("()", "o")).replace("(al)","al")
