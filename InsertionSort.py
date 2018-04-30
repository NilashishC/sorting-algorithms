#!/usr/bin/python3

"""

    An implementation of Insertion Sort Algorithm in Python 3
    ======================================================
    Usage : InsertionSort.sort(<sequence>)

"""


class InsertionSort:

    @staticmethod
    def sort(seq):

        for i in range(1, len(seq)):

            hole = i
            value = seq[hole]

            while(hole > 0 and seq[hole - 1] > value):
                seq[hole] = seq[hole - 1]
                hole -= 1

            seq[hole] = value
