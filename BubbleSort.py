#!/usr/bin/python3

"""

    An implementation of Bubble Sort Algorithm in Python 3
    ======================================================
    Usage : BubbleSort.sort(<sequence>)

"""


class BubbleSort:

    @staticmethod
    def sort(seq):
        for i in range(0, (len(seq) - 1)):

            flag = True

            for j in range(0, (len(seq)-i-1)):

                if(seq[j] > seq[j + 1]):

                    flag = False
                    temp = seq[j]
                    seq[j] = seq[j + 1]
                    seq[j + 1] = temp

            if(flag):
                break
