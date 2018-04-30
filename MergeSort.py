#!/usr/bin/python3

"""

    An implementation of Merge Sort Algorithm in Python 3
    ======================================================
    Usage : MergeSort.sort(<sequence>)

"""


class MergeSort:

    @staticmethod
    def sort(seq):

        n = len(seq)

        mid = int((n / 2))

        if(n < 2):
            return

        left = []
        right = []

        for i in range(0, mid):
            left.append(seq[i])

        for i in range(mid, n):
            right.append(seq[i])

        MergeSort.sort(left)
        MergeSort.sort(right)
        MergeSort.__merge(left, right, seq)

    def __merge(left, right, seq):

        i, j, k = 0, 0, 0

        while(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                seq[k] = left[i]
                k += 1
                i += 1
            else:
                seq[k] = right[j]
                j += 1
                k += 1
        while(i < len(left)):
            seq[k] = left[i]
            k += 1
            i += 1

        while(j < len(right)):
            seq[k] = right[j]
            k += 1
            j += 1


if __name__ == '__main__':
    a = [10, 1, 9, 81, 7]
    MergeSort.sort(a)
    print(a)
