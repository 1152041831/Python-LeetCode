def convert(s,num):
    print("当前的字符串为：",s)
    print("最大行数为：", num)
    if num == 1:
        print("当前的字符串为：",s)
        return s
    if num !=1 and num != 2:
        list = []
        c_list = ''
        for e in s:
            list.append(e)
        print("字符串长度为：", len(list))
        print("最大行数为：", num)
        con = len(list) % (2*num-2)
        count = int(len(list) / (2 * num - 2))
        print(f"划分的一组有 {2*num-2} 个元素")
        shengxia = len(list) - count * (num + num - 2)
        print("shengxia：", shengxia)
        zhongjian = num - 2
        index_x = 0
        index_y = 0
        xiebian = shengxia - num
        print("count:", count)
        if count > 0:
            if xiebian <= 0:
                A = [[''] * ((zhongjian + 1) * count + 1) for _ in range(num)]
                column = (zhongjian + 1) * count + 1
            else:
                A = [[''] * ((zhongjian + 1) * count + 1 + xiebian) for _ in range(num)]
                column = (zhongjian + 1) * count + 1 + xiebian
            for i in range(count):
                print(i)
                for j in range(num):
                    A[j][i * (num - 1)] = list.pop(0)
                for z in range(zhongjian):
                    A[num - 2 - z][i * (num - 1) + 1 + z] = list.pop(0)
                    index_x = num - 2 - z
                    index_y = i * (num - 1) + 1 + z
            print("剩余下来的斜边中元素个数为：", xiebian)
            # 向矩阵中添加
            if xiebian >= 0:
                for i in range(num):
                    A[i][index_y + 1] = list.pop(0)
                for j in range(xiebian):
                    A[num - 2 - j][index_y + 2 + j] = list.pop(0)
            else:
                for i in range(shengxia):
                    A[i][index_y + 1] = list.pop(0)

            print("剩下的个数为：", shengxia)

            for i in range(num):
                print(A[i])
                for j in range(column):
                    if A[i][j] != '':
                        c_list = c_list + A[i][j]

            print(c_list)

            return c_list
        else:
            print("list:",list)
            if len(list)-num <= 0:
                print(s)
                return s
            else:
                A = [[''] * (1+len(list)-num) for _ in range(num)]
                column = 1+len(list)-num
                xiebian = len(list) - num
                for i in range(num):
                    A[i][0] = list.pop(0)
                print("xiebian:",xiebian)
                for z in range(xiebian):
                    print("z:",z)
                    A[num - 2 - z][1 + z] = list.pop(0)
                for i in range(num):
                    print(A[i])
                    for j in range(column):
                        if A[i][j] != '':
                            c_list = c_list + A[i][j]

                print(c_list)

                return c_list
    if num == 2:
        list = []
        c_list = ''
        for e in s:
            list.append(e)
        count1=0
        count2=1
        while count1 < len(list):
            c_list = c_list + str(list[count1])
            print("count1:",count1)
            count1 = count1 + 2
            print("c_list:",c_list)
        while count2 < len(list):
            c_list = c_list + str(list[count2])
            print("count2:",count2)
            count2 = count2 + 2
            print("c_list:", c_list)

        print(c_list)
        return c_list









if __name__ == '__main__':
    convert("ABCDEF",2)