# 链表节点
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def removeNthFromEnd(head: ListNode, n: int) :
        tail=head
        list=[]

        while(tail):
            list.append(tail.val)
            tail=tail.next
        list.pop(len(list)-n)
        lenth=len(list)
        if lenth==0:
            return None
        head=ListNode(list[0],None)
        tail=head
        for i in range(lenth-1):
            node=ListNode(list[i+1],None)
            tail.next=node
            tail=node
        return head

    if __name__ == '__main__':
        removeNthFromEnd([1, 2, 3, 4, 5], 2)



