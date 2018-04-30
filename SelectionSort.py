#!/usr/bin/python3

"""

    An implementation of Selection Sort Algorithm in Python 3
    ======================================================
    Usage : SelectionSort.sort(<sequence>)

"""


class SelectionSort:

    @staticmethod
    def sort(seq):
        for i in range(0, len(seq) - 1):

            min_key = i

            for j in range(i+1, len(seq)):
                if(seq[j] < seq[min_key]):
                    min_key = j

            temp = seq[i]
            seq[i] = seq[min_key]
            seq[min_key] = temp
