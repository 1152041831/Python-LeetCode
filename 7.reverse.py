import math
def reverse(x):
    if x == 0 or x < -math.pow(2,31) or x >(math.pow(2,31)-1) :
        print("x =",0)
        return 0
    else:
        print(x)
        list = []
        fuhao = ''
        for e in str(x):
            list.append(e)
        if list[0] == '-':
            fuhao = list.pop(0)
        print(list)
        x_re = ''
        list.reverse()
        print(list)
        while list[0] == '0':
            list.pop(0)
        for i in range(len(list)):
            x_re = x_re + list[i]
        x_re = fuhao + x_re
        if int(x_re) < (-math.pow(2,31)) or int(x_re) >(math.pow(2,31)-1):
            print("x = ",0)
            return 0
        else:
            print("x = ",x_re)
            return int(x_re)



if __name__ == '__main__':
    reverse(-123)