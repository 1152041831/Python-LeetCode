import itertools
import math

def groupAnagrams(strs):
    resutlt = []
    resutlt_step = []
    for e in strs:
        list_str = list(e)
        list_str.sort()
        if list_str not in resutlt_step:
            resutlt_step.append(list_str)
            resutlt.append([e])
        else:
            #print(resutlt_step.index(list_str))
            resutlt[resutlt_step.index(list_str)].append(e)
    print(resutlt)
    print(resutlt_step)
    return resutlt





if __name__ == '__main__':
    groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])