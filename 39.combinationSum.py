import itertools
import math


def combinationSum(candidates,target):
    #result是存储最后结果的二维数组
    result = []
    #path记录的是可能添加进入result的一维数组
    path = []

    def backtrack(candidates, target, sum, startIndex):
        #如果 sum > target 则结束当前回溯
        if sum > target:
            return
        #如果 sum == target 则记录下当前的path数组信息，然后结束当前回溯
        if sum == target:
            #path[:]表示重新给予一个新内存空间，后面用到path的地方不会被影响
            return result.append(path[:])
        #从startIndex开始遍历candidates数组
        for i in range(startIndex, len(candidates)):
            # 如果 sum + candidates[i] > target 就终止遍历
            if sum + candidates[i] > target:
                return
            #否则就sum = sum + candidates
            sum += candidates[i]
            #在path一维数组中添加入当前值
            path.append(candidates[i])
            # startIndex = i:表示可以重复读取当前的数
            backtrack(candidates, target, sum, i)
            # 回溯 删除sum添加进入的值
            sum -= candidates[i]
            # 回溯 删除path刚刚添加进入的值（末尾的值）
            path.pop()

    candidates.sort()
    backtrack(candidates, target, 0, 0)
    print(result)
    return result

if __name__ == '__main__':
    combinationSum([1],1)