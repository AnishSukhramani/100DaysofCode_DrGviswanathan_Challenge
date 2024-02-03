class Solution:
    def sortSentence(self, s: str) -> str:
        list_of_words = s.split()

        for index in range(len(list_of_words)):
            order_char = list_of_words[index][-1]
            in_process_str = order_char + list_of_words[index]
            in_process_str = in_process_str[:-1]
            list_of_words[index] = in_process_str 

        list_of_words.sort()
        without_nums = [sub[1:] for sub in list_of_words]
        return " ".join(without_nums)
        
