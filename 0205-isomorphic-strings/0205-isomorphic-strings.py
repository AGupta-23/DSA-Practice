class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Maps characters from s -> t
        map_s = {}

        # Maps characters from t -> s
        map_t = {}

        for i in range(len(s)):

            # Current characters
            a = s[i]
            b = t[i]

            # Check s -> t mapping
            if a in map_s and map_s[a] != b:
                return False

            # Check t -> s mapping
            if b in map_t and map_t[b] != a:
                return False

            # Create the mappings
            map_s[a] = b
            map_t[b] = a

        return True