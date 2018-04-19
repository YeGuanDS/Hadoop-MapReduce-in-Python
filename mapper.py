# -*- coding: utf-8 -*-
"""
Hadoop mapper in Python
"""
import sys

def read_input(file):
    for line in file:
        # split the line into words
        # using yield for lazy evaluation
        yield line.split()

def main(separator='\t'):
    # input from STDIN
    data = read_input(sys.stdin)
    for words in data:
        # print the results to STDOUT
        # what we output here will be the input for reducer
        # tab-delimited
        for word in words:
            print '%s%s%d' % (word, separator, 1)

if __name__ == "__main__":
    main()
