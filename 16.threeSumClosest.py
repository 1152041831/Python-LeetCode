import itertools
import math
def threeSumClosest(nums,target):
    nums.sort()
    print(nums)
    listA = []
    #全组合函数combinations()
    listA = itertools.combinations(nums,3)
    listA = list(listA)
    closest = listA[0][0] + listA[0][1] + listA[0][2]
    for i in range(len(listA)):
        if abs(listA[i][0]+listA[i][1]+listA[i][2] - target) < abs(closest - target) :
            closest = listA[i][0]+listA[i][1]+listA[i][2]
    print(listA)
    print(closest)
    return closest












if __name__ == '__main__':
    threeSumClosest([-1,2,1,-4],1)