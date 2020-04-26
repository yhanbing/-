# 大数相加
class BigNumAdd(object):
    def addNum(self, l1:int, l2:int):
        l1 = list(map(int, reversed(str(l1))))
        l2 = list(map(int, reversed(str(l2))))
        l1, l2 = self.judgeLen(l1, l2)
        add_nums = []
        for i in range(len(l1)):
            add_num, flag = self.judgeCarry(l1[i], l2[i])
            if flag == 0:
                add_nums.append(add_num)
            else:
                add_nums.append(add_num)
                try:
                    l1[i + 1] = l1[i + 1] + 1
                except:
                    add_nums.append(1)
        if add_nums[-1] == 0:
            add_nums.append(1)
        return ''.join(map(str,list(reversed(add_nums))))

    def judgeCarry(self, a, b):
        if a + b > 9:
            return [(a + b) % 10, 1]
        else:
            return [a + b, 0]

    def judgeLen(self, l1, l2):
        lenl1 = len(l1)
        lenl2 = len(l2)

        if lenl1 >= lenl2:
            for i in range(abs(lenl2 - lenl1)):
                l2.append(0)
            return [l1, l2]
        else:
            for i in range(abs(lenl2 - lenl1)):
                l1.append(0)
            return [l2, l1]

