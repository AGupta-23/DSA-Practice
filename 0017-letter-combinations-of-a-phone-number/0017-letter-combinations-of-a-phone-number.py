class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):

            # Base case:
            # If we processed all digits,
            # store the current combination.
            if index == len(digits):
                result.append("".join(current))
                return

            # Get letters for the current digit
            letters = phone[digits[index]]

            # Try every letter
            for letter in letters:

                # Choose
                current.append(letter)

                # Explore next digit
                backtrack(index + 1, current)

                # Undo choice (Backtrack)
                current.pop()

        backtrack(0, [])

        return result