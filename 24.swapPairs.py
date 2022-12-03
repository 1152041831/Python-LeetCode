# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        list = []
        list1 = []
        list2 = []
        result = []
        # 将链表保存至list中
        while (tail):
            list.append(tail.val)
            tail = tail.next
        for i in range(len(list)):
            if i % 2 == 0:
                list1.append(list[i])
            else:
                list2.append(list[i])
        for i in range(max(len(list1), len(list2))):
            if len(list2) != 0:
                result.append(list2.pop(0))
            if len(list1) != 0:
                result.append(list1.pop(0))
        # list为空时
        lenth = len(result)
        if lenth == 0:
            return None
        # list不为空时，将list列表转换为单链表
        head = ListNode(result[0], None)
        tail = head
        for i in range(lenth - 1):
            node = ListNode(result[i + 1], None)
            tail.next = node
            tail = node
        return head


