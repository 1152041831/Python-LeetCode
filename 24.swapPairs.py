import itertools
import math

from ListNode import ListNode


def swapPairs(head):
    tail = head
    list = []
    # 将链表保存至list中
    while (tail):
        list.append(tail.val)
        tail = tail.next

    print(list)


if __name__ == '__main__':
    swapPairs([1,2,3,4])