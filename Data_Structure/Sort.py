class Sort():
    # 冒泡法
    def bubbleSort(self, alist):
        for l in range(len(alist)-1, 0, -1):
            for i in range(l):
                if alist[i] > alist[i+1]:
                    alist[i], alist[i+1] = alist[i+1], alist[i]
        return alist

    # 快速冒泡法
    def shortBubbleSort(self, alist):
        exchanges = True
        passnum = len(alist) - 1
        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if alist[i] > alist[i+1]:
                    exchanges = True
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
            passnum = passnum - 1
        return alist

    # 选择排序
    def selectionSort(self, A):
        for i in range(len(A)-1, 0, -1):
            max_idx = 0
            for j in range(1, i+1):
                if A[j] > A[max_idx]:
                    max_idx = j

            temp = A[i]
            A[i] = A[max_idx]
            A[max_idx] = temp
        return A


sort = Sort()
a = [8, 6, 4, 2, 1]
b = sort.shortBubbleSort(a)
print(b)
