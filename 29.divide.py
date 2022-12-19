import itertools
import math
def divide(dividend, divisor):
    result = divisor
    if dividend>0 and divisor>0 and divisor > dividend :
        return 0
    if divisor == 1:
        if math.pow(-2, 31) > dividend or dividend > math.pow(2, 31) - 1:
            return math.pow(-2, 31)
        return dividend
    if divisor == -1:
        return -dividend
    if dividend > 0 and divisor > 0:
        count = 0
        while 0 <= dividend - result:
            result = result + divisor
            count = count + 1
            if math.pow(-2,31) > count or count > math.pow(2,31)-1:
                return math.pow(-2, 31)
            print("result:",result)
            print("count:",count)

    if math.pow(-2,31) <= count <= math.pow(2,31)-1:
        print(count)
        return count




if __name__ == '__main__':
    divide(1000000+00,3)