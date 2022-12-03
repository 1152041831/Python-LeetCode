import itertools
import math
def strStr(haystack,needle):
    length = len(needle)
    length1 = len(haystack)
    if needle not in haystack:
        print("N")
        return -1
    else:
        if length == length1:
            print(0)
            return 0
        else:

            for i in range(length1):
                L = i + length
                if L > length1:
                    L = length1
                if haystack[i:L] == needle:
                    print(i)
                    return i


if __name__ == '__main__':
    strStr("acb","b")