import itertools
import math





def multi(x, y):
    # 判断一下x的长度
    len_x = getNumLen(x)
    # 判断一下y的长度
    len_y = getNumLen(y)

    # 如果他们之间有一个小于1的话那就直接返回这两个数据的乘法即可
    if len_x <= 1 or len_y <= 1:
        return x * y

    # 获取x的第一部分的长度
    branch_x1 = int(len_x / 2)
    # 获取x的第二部分的长度
    branch_x2 = len_x - branch_x1

    # 获取y的第一部分的长度
    branch_y1 = int(len_y / 2)
    # 获取y的第二部分的长度
    branch_y2 = len_y - branch_y1

    # 获取x第一部分的数据
    x1 = int(x / pow(10, branch_x2))
    # 获取x第二部分的数据
    x2 = x % pow(10, branch_x2)

    # 获取y第一部分的数据
    y1 = int(y / pow(10, branch_y2))
    # 获取y第二部分的数据
    y2 = y % pow(10, branch_y2)

    # 获取第一部分的乘法的结果
    temp_x1_y1 = multi(x1, y1)
    x1_y1 = temp_x1_y1 * math.pow(10, branch_x2 + branch_y2)
    # 获取第二部分乘法的结果
    x2_y2 = multi(x2, y2)

    # 下面就是对两个乘法化为一个乘法的过程
    # 先判断一下0.5n 是否大于0.5m
    # 如果大于的话
    if branch_x2 > branch_y2:
        # 获取两者之差
        pow_num = branch_x2 - branch_y2
        # 依次获取公式中第 1 2 3 4部分
        A = x1 * math.pow(10, pow_num) - x2
        B = y2 - y1
        C = temp_x1_y1 * math.pow(10, pow_num)
        D = x2_y2

        # 排除乘法中的负数，如果有负数的话，在上面计算的时候会麻烦很多
        if A >= 0 and B >= 0:
            mid = (multi(A, B) + C + D) * math.pow(10, branch_y2)
        elif A >= 0 and B < 0:
            B = -B
            mid = (-multi(A, B) + C + D) * math.pow(10, branch_y2)
        elif A < 0 and B >= 0:
            A = -A
            mid = (-multi(A, B) + C + D) * math.pow(10, branch_y2)
        else:
            A = -A
            B = -B
            mid = (multi(A, B) + C + D) * math.pow(10, branch_y2)
    else:
        pow_num = branch_y2 - branch_x2
        A = x1 - x2
        B = y2 - y1 * math.pow(10, pow_num)
        C = temp_x1_y1 * math.pow(10, pow_num)
        D = x2_y2
        if A >= 0 and B >= 0:
            mid = (multi(A, B) + C + D) * math.pow(10, branch_x2)
        elif A >= 0 and B < 0:
            B = -B
            mid = (-multi(A, B) + C + D) * math.pow(10, branch_x2)
        elif A < 0 and B >= 0:
            A = -A
            mid = (-multi(A, B) + C + D) * math.pow(10, branch_x2)
        else:
            A = -A
            B = -B
            mid = (multi(A, B) + C + D) * math.pow(10, branch_x2)

    return x1_y1 + mid + x2_y2


def getNumLen(num):
    x = 0
    while (num / 10 != 0):
        x += 1
        num = int(num / 10)
    return x


def multiply(num1,num2):
    Number_s = ['0','1','2','3','4','5','6','7','8','9']
    Number_int = [0,1,2,3,4,5,6,7,8,9]
    num1_list = list(num1)
    num2_list = list(num2)
    for i in range(len(num1_list)):
        for j in range(len(Number_s)):
            if num1_list[i] == Number_s[j]:
                num1_list[i] = Number_int[j]
    for i in range(len(num2_list)):
        for j in range(len(Number_s)):
            if num2_list[i] == Number_s[j]:
                num2_list[i] = Number_int[j]
    print(num1_list)
    print(num2_list)
    num1_int = 0
    num2_int = 0
    for i in range(len(num1_list)):
        num1_int = math.pow(10,(len(num1_list)-i-1))*num1_list[i] + num1_int
    for i in range(len(num2_list)):
        num2_int = math.pow(10,(len(num2_list)-i-1))*num2_list[i] + num2_int
    print(num1_int)
    print(num2_int)
    n = str(multi(int(num1_int),int(num2_int)))
    print(n)
    return n


if __name__ == '__main__':
    multiply("123456789","987654321")