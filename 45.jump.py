import itertools
import math


def jump(nums):
    count = [0]
    toJump(0,count,nums)
    if len(nums) == 1:
        print("count:",0)
        return 0
    else:
        print("count:",count[0])
        return count[0]

def toJump(start,count,a):
    if start+1+a[start] >= len(a):
        count[0] = count[0] + 1
    else:
        b = a[start + 1 : start+1+a[start]].copy()
        max_lengtg_index = 0
        for i in range(len(b)):
            if max_lengtg_index <= a[start + 1 + i] + start + 1 + i:
                max_lengtg_index = a[start + 1 + i] + start + 1 + i
                max_index = start + 1 + i
        count[0] = count[0] + 1
        start = max_index
        b.clear()
        toJump(start, count, a)
if __name__ == '__main__':
    jump([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])