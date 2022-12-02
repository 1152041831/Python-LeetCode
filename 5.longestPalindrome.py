import operator


def longestPalindrome(s):
    List = []
    List1 = []
    P = []
    for i in s:
        List.append(i)

    if len(s) != 1 :
        while len(List) != 1:
            print(f"①当前的List1为：{List1}")
            for e in List:
                S = ""
                List1.append(e)
                print(f"当前判断的串为：{List1}")
                List_re = list(reversed(List1))
                print(f"当前反转后的串为：{List_re}")
                reversed(List1)
                print(f"这个串是否构成回文：{operator.eq(List1, List_re)}")
                if operator.eq(List1, List_re):
                    for i in range(len(List1)):
                        S = str(List[i]) + S
                    P.append(S)
            print(f"②当前的List1为：{List1}")
            List1.clear()
            print(f"③当前的List1为：{List1}")
            print(f"反转前的list为：{List}")
            List = list(reversed(List))
            print(f"反转后的list为：{List}")
            List.pop()
            print(f"删除反转后list的末尾元素后：{List}")
            List = list(reversed(List))
            print(f"下一次的list为：{List}")
        print(f"所有回文子串：{P}")
        print(f"最长的回文子串：{max(P, key=len)}")
        return max(P, key=len)
    else:
        print(f"最长的回文子串：{s}")
        return s








if __name__ == '__main__':
    longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")