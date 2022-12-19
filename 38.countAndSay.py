import itertools
import math

def countAndSay(n):
    #除了n=1时，其他值输出值都为偶数个数
    str1 = "1"
    if n == 1:
        return str1
    else:
        for i in range(n-1):
            str1 = findStr(str1)
        return str1

def findStr(str1):
    #str1 = "3322251"
    first_s = []
    str_result = ""
    list_s = list(str1)
    first_s.append(list_s.pop(0))
    count_s = [1]
    print(list_s)
    print(first_s)
    while len(list_s) > 0:
        if list_s[0] == first_s[len(first_s) - 1]:
            count_s[len(first_s) - 1] = count_s[len(first_s) - 1] + 1
            list_s.pop(0)
        else:
            first_s.append(list_s.pop(0))
            count_s.append(1)
    print("list_s:", list_s)
    print("first_s:", first_s)
    print("count_s:", count_s)
    # 拼接字符串
    while len(first_s) > 0:
        str_result = str_result + f"{count_s.pop(0)}"
        str_result = str_result + first_s.pop(0)
    print("str_result:", str_result)
    return str_result
















if __name__ == '__main__':
    countAndSay(10)