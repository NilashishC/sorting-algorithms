#!/usr/bin/python3

"""

    An implementation of Quick Sort Algorithm with Randomized Pivot in Python 3
    ===========================================================================
    Usage : QuickSort.sort(<sequence>)

"""

from random import randint


class QuickSort:

    @staticmethod
    def __qsort(seq, start, end):

        if(start < end):
            pIndex = QuickSort.__partition(seq, start, end)
            QuickSort.__qsort(seq, start, pIndex - 1)
            QuickSort.__qsort(seq, pIndex + 1, end)

    @staticmethod
    def sort(seq):
        QuickSort.__qsort(seq, 0, (len(seq) - 1))

    @staticmethod
    def __partition(seq, start, end):
        # pivot = seq[end]
        pivot = randint(start, end)  # Randomized Pivot
        seq[end], seq[pivot] = seq[pivot], seq[end]

        pIndex = start

        for i in range(start, end):
            if(seq[i] <= seq[end]):
                seq[i], seq[pIndex] = seq[pIndex], seq[i]
                pIndex += 1

        seq[pIndex], seq[end] = seq[end], seq[pIndex]
        return pIndex
