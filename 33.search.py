import itertools
import math
def search(nums,target):
    z = 0
    y = len(nums) - 1
    index = -1
    while z <= y:
        m = int((z + y) / 2)
        if target == nums[m]:
            print("m:",m)
            #如果此时的目标值等于当前的中间值，则找到
            return m
        #如果左边部分有序：
        if nums[0] <= nums[m]:
            #如果目标值在左边部分范围
            if nums[0] <= target < nums[m]:
                #缩小左边部分的右边界
                y = m - 1
            #如果目标值超出了左边部分范围
            else:
                #跳转至右边部分
                z = m + 1
        #如果右边部分有序（至少有一边是有序的）：
        else:
            #如果目标值在右边部分范围内
            if nums[m] < target <= nums[len(nums) - 1]:
                #缩小右边部分的左边界
                z = m + 1
            #如果目标值超出了右边部分范围
            else:
                #跳转至左边界
                y = m - 1
    print(-1)
    #如果最后仍然没有找到目标值，则返回-1
    return -1


if __name__ == '__main__':
    search([],0)