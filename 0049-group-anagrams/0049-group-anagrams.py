class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            
            # Count frequency of each character
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            # Lists cannot be dictionary keys,
            # so convert it into a tuple
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())