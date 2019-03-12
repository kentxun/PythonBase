# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Remove:
    def removeNode(self, pNode):
        # write code here
        self.pNode = pNode
        if self.pNode.next == None:
            return False
        else:
            self.pNode.val = self.pNode.next.val
            self.pNode.next = self.pNode
            self.pNode = self.pNode.next
            return True

'''
class Remove {
public:
    ListNode* removeNode(ListNode* pHead, int delVal) {
        // 第一种情况：删除的节点是头节点
        if (pHead->val == delVal) {
            ListNode *node = pHead->next;
            pHead->next = NULL;
            return node;
        }
 
        ListNode *previous = pHead;
        ListNode *current = pHead->next;
        while (current != NULL) {
            if (current->val == delVal) {
                previous->next = current->next;
                current->next = NULL;
            }
            previous = previous->next;
            current = current->next;
        }
        return pHead;
    }
};

'''