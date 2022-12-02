import math
def intToRoman(num):
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    print("字符 数值")
    for i in dic:
        print(i," ",dic[i])

    count_1000 = int(num / 1000)
    count_100 = int((num - count_1000*1000 )/100)
    count_10 =  int((num - count_1000*1000 - count_100*100)/10)
    count_1 = int((num - count_1000*1000 - count_100*100 - count_10*10))

    print(f"千位数字为:{count_1000}")
    print(f"百位数字为:{count_100}")
    print(f"十位数字为:{count_10}")
    print(f"最后的个位数字为:{count_1}")
    re_str = ''
    #判断千位数字的罗马符号
    for i in range(count_1000):
        re_str = re_str + 'M'

    #判断百位数字的罗马符号
    if count_100 == 1:
        re_str = re_str + 'C'
    if count_100 == 2:
        re_str = re_str + 'CC'
    if count_100 == 3:
        re_str = re_str + 'CCC'
    if count_100 == 4:
        re_str = re_str + 'CD'
    if count_100 == 5:
        re_str = re_str + 'D'
    if count_100 == 6:
        re_str = re_str + 'DC'
    if count_100 == 7:
        re_str = re_str + 'DCC'
    if count_100 == 8:
        re_str = re_str + 'DCCC'
    if count_100 == 9:
        re_str = re_str + 'CM'


    #判断十位数字的罗马符号
    if count_10 == 1:
        re_str = re_str + 'X'
    if count_10 == 2:
        re_str = re_str + 'XX'
    if count_10 == 3:
        re_str = re_str + 'XXX'
    if count_10 == 4:
        re_str = re_str + 'XL'
    if count_10 == 5:
        re_str = re_str + 'L'
    if count_10 == 6:
        re_str = re_str + 'LX'
    if count_10 == 7:
        re_str = re_str + 'LXX'
    if count_10 == 8:
        re_str = re_str + 'LXXX'
    if count_10 == 9:
        re_str = re_str + 'XC'


    #判断个位数字的罗马符号
    if count_1 == 1:
        re_str = re_str + 'I'
    if count_1 == 2:
        re_str = re_str + 'II'
    if count_1 == 3:
        re_str = re_str + 'III'
    if count_1 == 4:
        re_str = re_str + 'IV'
    if count_1 == 5:
        re_str = re_str + 'V'
    if count_1 == 6:
        re_str = re_str + 'VI'
    if count_1 == 7:
        re_str = re_str + 'VII'
    if count_1 == 8:
        re_str = re_str + 'VIII'
    if count_1 == 9:
        re_str = re_str + 'IX'

    print(re_str)
    return re_str












#尾数有 4 ， 9的有例外
# 4 9 14 19 24 ...
if __name__ == '__main__':
    intToRoman(3999)