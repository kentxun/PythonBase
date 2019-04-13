
class ChkLoop:
    def chkLoop(self, head, adjust):
        # write code here
        if head is  None or head.next is  None:
            return False
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            # 第一次判定是 确定有环
            if fast == slow:
                return  True
        return False

if __name__ == '__main__':
    # 根据题意输入，依次输入每个链表节点，无需使用链表确认方法
    # 直接对链表节点进行检测
    import  sys
    link = sys.stdin.readline().strip().split(',')
    if len(link)-len(set(link)):
        print(False)
    else:
        print(True)