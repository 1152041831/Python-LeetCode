import itertools
import math
def generateParenthesis(n):
    list_1 = [' ','(',' ',')',' ']
    list_2 = [[' ','(',' ',')',' ','(',' ',')',' '],[' ','(',' ','(',' ',')',' ',')',' ']]
    str1 = ["()"]
    str2 = ["()()","(())"]
    if n == 1:
        return str1
    if n == 2:
        return str2
    else:
        str = ""
        result = ["()()","(())"]
        print("n:",n)
        for count in range(n-2):
            str2 = result.copy()
            print("str2:",str2)
            for n in range(len(str2)):
                for i in range(len(str2[n])):
                    if str2[n][0:i]+ "()" + str2[n][i:len(str2[n])] not in result:
                        result.append(str2[n][0:i] + "()" + str2[n][i:len(str2[n])])

            print("1",result)
            for j in range(len(str2)):
                result.pop(0)
            print("2",result)


        print(result)
        return result

if __name__ == '__main__':
    generateParenthesis(8)