# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail1 = l1
        tail2 = l2
        list1 = []
        list2 = []
        sumlist = []
        # 将链表保存至list中
        while (tail1):
            list1.append(tail1.val)
            tail1 = tail1.next

        while (tail2):
            list2.append(tail2.val)
            tail2 = tail2.next

        length = min(len(list1), len(list2))

        jia = 0

        while list1 and list2:
            sumlist.append(list1.pop(0) + list2.pop(0) + jia)
            if sumlist[len(sumlist) - 1] >= 10:
                sumlist[len(sumlist) - 1] = sumlist[len(sumlist) - 1] - 10
                jia = 1
            else:
                jia = 0

        if len(list1) != 0:
            while list1:
                sumlist.append(list1.pop(0) + jia)
                if sumlist[len(sumlist) - 1] >= 10:
                    sumlist[len(sumlist) - 1] = sumlist[len(sumlist) - 1] - 10
                    jia = 1
                else:
                    jia = 0
        if len(list2) != 0:
            while list2:
                sumlist.append(list2.pop(0) + jia)
                if sumlist[len(sumlist) - 1] >= 10:
                    sumlist[len(sumlist) - 1] = sumlist[len(sumlist) - 1] - 10
                    jia = 1
                else:
                    jia = 0
        if jia == 1:
            sumlist.append(1)

        # sumlist为空时
        lenth = len(sumlist)
        if lenth == 0:
            return None
        # sumlist不为空时，将list列表转换为单链表
        head = ListNode(sumlist[0], None)
        tail = head
        for i in range(lenth - 1):
            node = ListNode(sumlist[i + 1], None)
            tail.next = node
            tail = node
        return head

