import itertools
import math
def threeSum(nums):
    listS = []
    nums.sort()
    result = []
    # 全组合函数combinations()
    listS = itertools.combinations(nums, 3)
    listS = list(listS)
    print(listS)
    for i in range(len(listS)):
        if listS[i][0] + listS[i][1] + listS[i][2] == 0:
            list_temp = [listS[i][0] , listS[i][1] , listS[i][2]]
            list_temp.sort()
            if list_temp not in result:
                result.append(list_temp)

    print(result)

    return result



if __name__ == '__main__':
    threeSum([0,0,0])