class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:

            # Get current digits, or 0 if list is exhausted
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Add digits + previous carry
            total = x + y + carry

            # Current digit
            digit = total % 10

            # Carry for next position
            carry = total // 10

            # Create node for current digit
            curr.next = ListNode(digit)
            curr = curr.next

            # Move lists forward
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next