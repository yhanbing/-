class BigNumMult(object):
    def numMult(self, l1: int, l2: int):
        l1 = list(map(int, reversed(str(l1))))
        l2 = list(map(int, reversed(str(l2))))
        l3 = [0 for i in range(0, len(l1) + len(l2))]

        for i in range(0, len(l1)):
            for j in range(0, len(l2)):
                l3[i + j] += l1[i] * l2[j]

        for i in range(0, len(l3)):
            if l3[i] > 9:
                l3[i + 1] += l3[i] // 10
                l3[i] = l3[i] % 10

        l3.reverse()
        return int(''.join(map(str, l3)))