import itertools
import math
import operator


def nextPermutation(nums):
    listA = []
    result = []
    list1 = []
    list2 = []
    for e in nums:
        listA.append(e)
    listA.sort()
    print("listA:",listA)
    print("nums:",nums)
    listA.reverse()
    print(operator.eq(nums,listA))
    if operator.eq(nums,listA) == True:
        nums.reverse()
        print("re:",nums)
        return nums
    i = 0
    len_index = len(nums) - 1
    ex_index = 0
    re_index = 0
    length = len(nums)
    #将nums倒序
    nums.reverse()
    print(nums)
    N = nums.copy()
    print("N:",N)
    for i in range(length-1):
        for j in range(length-i-1):
            if N[i] > N[i+1+j]:
                temp = N[i]
                N[i] = N[i+1+j]
                N[i+1+j] = temp
                ex_index = i+1+j
                re_index = length - ex_index - 1
                N.reverse()

                list1 = N[0:re_index+1].copy()
                list2 = N[re_index+1:length].copy()
                list2.sort()
                print("list1:",list1)
                print("list2:", list2)
                N.clear()
                N.extend(list1)
                N.extend(list2)
                print("result-N:", N)
                result.append(N.copy())
                N.clear()
                N = nums.copy()




    result.sort()
    nums.clear()
    for e in result[0]:
        nums.append(e)

    print("result-nums:", nums)





if __name__ == '__main__':
    nextPermutation([4,2,0,2,3,2,0])