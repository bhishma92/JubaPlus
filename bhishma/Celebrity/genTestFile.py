import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
import csv
from array import array
import time


def main():


        time_start = timeit.default_timer()

        """read output1"""
        df = pd.read_csv('/home/dummy/try/SesOutFinal'+ '.tsv', dtype = object, header=None, delimiter="\t", error_bad_lines = False)
        print len(df.index)
        print 'file read'

        #df.columns = ['A','B','C','D','E','F','G']
        #df.drop('B',axis = 1, inplace = True)
        #df['F'] = pd.to_datetime(df['F'])
        df2 =  df.head(1000000)
        #df.sort_index(by = ['A','F','G'], ascending = [True, True, True], inplace = True) # sort complete

        #print df.head(10)

        #print df.tail(10)

        df2.to_csv("/home/dummy/try/testSesFinal.tsv", index = False, header= False, sep='\t')

        #print count, i

        #print df.head(10)

        #print df.tail(2000)

        time_stop = timeit.default_timer()

        print time_stop - time_start













if __name__=="__main__": main()


