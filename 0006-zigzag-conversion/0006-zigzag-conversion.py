class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # If only one row, or rows >= length of string,
        # zigzag doesn't actually happen
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        curr_row = 0
        direction = 1  # 1 = moving down, -1 = moving up

        for ch in s:
            rows[curr_row] += ch

            # Change direction at the top or bottom
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)