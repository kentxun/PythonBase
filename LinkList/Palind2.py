class Palindrome:
    def isPalindrome(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return True
        stack = []
        fast = pHead
        slow = pHead
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next if fast.next else None
        # 奇数长度
        if fast:
            slow = slow.next
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True if len(stack) == 0 else False