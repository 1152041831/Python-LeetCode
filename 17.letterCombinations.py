import itertools
import math
def letterCombinations(digits):
    number = [[""],[""],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
    print(number)
    result = []
    listD = []
    count = []
    index = 0
    for e in digits:
        listD.append(e)
        count.append(int(e))
    if digits == "":
        print("[]")
        return []
    if len(digits) == 1:
        print(number[int(digits[0])])
        return number[int(digits[0])]
    if len(digits) == 2:
        for e in number[count[index]]:
            for e1 in number[count[index+1]]:
                s = e + e1
                result.append(s)
        return result
        print(result)
    if len(digits) == 3:
        for e in number[count[index]]:
            for e1 in number[count[index+1]]:
                for e2 in number[count[index + 2]]:
                    s = e + e1 + e2
                    result.append(s)
        return result
        print(result)
    if len(digits) == 4:
        for e in number[count[index]]:
            for e1 in number[count[index+1]]:
                for e2 in number[count[index + 2]]:
                    for e3 in number[count[index + 3]]:
                        s = e + e1 + e2 +e3
                        result.append(s)
        return result
        print(result)








if __name__ == '__main__':
    letterCombinations("234")