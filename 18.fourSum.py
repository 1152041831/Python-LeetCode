import itertools
import math
def fourSum(nums,target):
    nums.sort()
    print(nums)
    listA = []
    result = []
    #全组合函数combinations()
    listA = itertools.combinations(nums,4)
    listA = list(listA)
    for i in range(len(listA)):
        if listA[i][0]+listA[i][1]+listA[i][2]+listA[i][3] - target == 0:
            list_temp = [listA[i][0],listA[i][1],listA[i][2],listA[i][3]]
            list_temp.sort()
            if list_temp not in result:
                result.append(list_temp)
    print(result)

    return result












if __name__ == '__main__':
    fourSum([1,0,-1,0,-2,2],0)