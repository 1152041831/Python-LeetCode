import itertools
import math

def searchRange(nums,target):
    z = 0
    y = len(nums) - 1
    index1 = diedai(nums, z, y, target)
    if len(index1) != 0:
        index1.sort()
        print("indexi:",index1)
        print("result:",[index1[0],index1[len(index1)-1]])
        return [index1[0],index1[len(index1)-1]]
    else:
        print([-1,-1])
        return [-1,-1]

def diedai(nums,z,y,target):
    index1 = []
    while z <= y:
        m = int((z + y) / 2)
        if target == nums[m]:
            index1.append(m)
            print("index1:",index1)
            print("nums[0:m]:",nums[0:m])
            print("nums[m+1:len(nums)]:",nums[m+1:len(nums)])

            for i in range(len(nums[0:m])):
                if nums[m-i-1] == target:
                    index1.append(m-i-1)
                else:
                    nums[0:m].reverse()
                    break
            for i in range(len(nums[m+1:len(nums)])):
                if nums[i+m+1] == target:
                    index1.append(i+m+1)
                else:
                    break
            break
        if target < nums[m]:
            y = m - 1
        if target > nums[m]:
            z = m + 1
    return index1


if __name__ == '__main__':
    searchRange([5,7,7,8,8,10],8)