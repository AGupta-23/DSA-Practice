class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        #this will contain sorted form of anagrams as keys and actual words as values

        for word in strs:
            sorted_word = sorted(word)  #formed as list
            key = "".join(sorted_word)  #now joined as string form

            if key not in dict:
                dict[key]=[]

            dict[key].append(word)

        groups = list(dict.values())
        return groups