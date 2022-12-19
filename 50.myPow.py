import itertools
import math

def myPow(x,n):
    if n >= 0:
        power_2 = 1
        r = 1
        p = x
        while power_2 <= n:
            if power_2 & n != 0:
                #r=r*p
                r *= p
            #x^2 x^4 x^8 x^16
            p = p * p
            print("前power",power_2)
            #power_2 = power_2*2 翻倍当前次数 ，相当于当前的p值平方之后的结果
            power_2 = power_2 * 2
            print("后power",power_2)
        print("结果：",r)
        return r
    else:
        n = -n
        x = 1/x
        power_2 = 1
        r = 1
        p = x
        while power_2 <= n:
            if power_2 & n != 0:
                r *= p
            p = p * p
            power_2 = power_2 * 2
            print(r)
        print(r)
        return r







if __name__ == '__main__':
    myPow(0.00001,2147483647)