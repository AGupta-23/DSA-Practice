class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        #this will contain sorted form of anagrams as keys and actual words as values

        for word in strs:
            
            count = [0] * 26 #created a count list with at most 26 numbers

            for char in word:
                index = ord(char) - ord('a')
                count[index] +=1

            key = tuple(count)

            if key not in dict:
                dict[key]=[]

            dict[key].append(word)

        groups = list(dict.values())
        return groups