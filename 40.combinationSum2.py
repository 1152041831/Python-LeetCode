import itertools
import math


def combinationSum2(candidates,target):
    candidates.sort()
    for i in range(len(candidates)):
        if candidates[i] > target:
            candidates = candidates[0:i].copy()
            break



    # result是存储最后结果的二维数组
    result = []
    # path记录的是可能添加进入result的一维数组
    path = []

    def backtrack(candidates, target, sum, startIndex):
        # 如果 sum > target 则结束当前回溯
        if sum > target:
            return
        # 如果 sum == target 则记录下当前的path数组信息，然后结束当前回溯
        if sum == target:
            # path[:]表示重新给予一个新内存空间，后面用到path的地方不会被影响
            if  path not in result:
                return result.append(path[:])
            else:
                return
        # 从startIndex开始遍历candidates数组
        for i in range(startIndex, len(candidates)):
            # 如果 sum + candidates[i] > target 就终止遍历
            if sum + candidates[i] > target:
                return
            # 否则就sum = sum + candidates
            sum += candidates[i]
            # 在path一维数组中添加入当前值
            path.append(candidates[i])
            # startIndex = i:表示可以重复读取当前的数
            backtrack(candidates, target, sum, i)
            # 回溯 删除sum添加进入的值
            sum -= candidates[i]
            # 回溯 删除path刚刚添加进入的值（末尾的值）
            path.pop()


    backtrack(candidates, target, 0, 0)
    count_candidates = dict()
    count_result = dict()
    result_list = []

    for i in candidates:
        if i in count_candidates:
            count_candidates[i] += 1
        else:
            count_candidates[i] = 1

    for j in range(len(result)):
        for i in result[j]:
            if i in count_result:
                count_result[i] += 1
            else:
                count_result[i] = 1
        #print(f"第{j+1}个元素:",f"{count_result}")
        result_list.append(count_result.copy())
        count_result.clear()

    new_result = []
    for i in range(len(result_list)):
        flag = 0
        for key in result_list[i].keys():
            if result_list[i][key] > count_candidates[key]:
                flag = 1
                break
        if flag == 0:
            new_result.append(result[i])

    if len(set(candidates)) == 1 and candidates[0] == target:
        print(f"{[[target]]}")
        return [[target]]

    print("result:",result)
    print("new_result:",new_result)
    return new_result


if __name__ == '__main__':
    combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27)