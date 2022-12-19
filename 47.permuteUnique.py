import itertools
import math


def permuteUnique(nums):
    result = []

    #回溯法，每次找一个未被添加进入tmp中的元素添加进入tmp，
    #然后在数组中排除（没有删掉）已添加的元素，并将其作为递归方法中的新参数
    #知道nums数组所有元素被选中，即nums为空时，记录当前的tmp数组，即为一种排列
    def backtrack(nums, tmp):
        #如果当前队列nums为空，则表明遍历到最底层元素，则将存储当前排列的tmp存入result，并返回上一层
        if not nums:
            if tmp not in result:
                result.append(tmp)
            return
        #遍历当前nums
        for i in range(len(nums)):
            #nums[:i] + nums[i + 1:]表示排除了当前 nums[i]后剩下的数组
            #tmp + [nums[i]] 表示当前的已被选中的 nums数组
            backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

    backtrack(nums, [])

    print(result)
    return result



if __name__ == '__main__':
    permuteUnique([1,1,2])