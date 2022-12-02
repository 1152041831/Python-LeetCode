import math
def myAtoi(x):
        print(x)
        list1 = []
        num = ['0','1','2','3','4','5','6','7','8','9']
        for e in x:
            list1.append(e)
        for i in range(len(list1)):
            if list1[0] == ' ':
                list1.pop(0)
            else:
                break

        print("list1:",list1)

        if  len(list1) == 0:
            print("1.判断后的结果为：0")
            return 0
        else:
            if list1[0] not in num and list1[0] != '+' and list1[0] != '-':
                print("2.判断后的结果为：0")
                return 0
            else:
                fuhao = ''
                flag = 0
                if list1[0] == '-' or list1[0] == '+':
                    fuhao = list1.pop(0)
                    if len(list1) == 0:
                        print("3.判断后的结果为：0")
                        return 0
                if list1[0] == '-' or list1[0] == '+' or list1[0] not in num:
                    print("4.判断后的结果为：0")
                    return 0
                else:
                    result = ''
                    for e in list1:
                        if e in num:
                            result = result + e
                        else:
                            break
                    result = fuhao + result
                    print("最后数字长度为:", len(result))
                    print("最后数字为:", int(result))
                    result = int(result)
                    if result < -math.pow(2, 31):
                        result = -math.pow(2, 31)
                    if result > (math.pow(2, 31) - 1):
                        result = math.pow(2, 31) - 1
                    print("5.判断后的结果为：", int(result))
                    return int(result)





if __name__ == '__main__':
    myAtoi("   +0 123")