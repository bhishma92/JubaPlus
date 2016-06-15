import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob
import csv

def main():


        path = '/Users/bhishma/Documents/JubaPlus/Celebrity/compress'

        allFiles = glob.glob(path + "/*.tsv")


        c = 0

        for file in allFiles:

                print file

                time_start = timeit.default_timer()

                df = pd.read_csv(file, header=None, dtype = object, delimiter="\t", error_bad_lines = False)

                #print len(df[0])
                
                drop_list = []
                index = 0 
                count = 0
                
                while index != len(df):
                        val = True
                        for i in range(0, 7):
                                if isinstance(df[i][index], basestring) == False:
                                        val = False

                        if val == False:
                                drop_list.append(index)
                        else:
                        	if len(df.loc[index, 6]) != 12:
                        		temp = df.loc[index, 6].strip(' GMT').split(':')
                                if int(temp[2]) < 10:
                                        temp[2] = temp[2].zfill(2)
                                        df.loc[index, 6] = ':'.join(temp) + ' GMT'     


                        index += 1
                print drop_list

                df.drop(df.index[drop_list], inplace=True)
                

                df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete

                print len(df)

                df.to_csv('hellsorted' + str(c) + '.tsv', index = False, header = None, sep='\t')

                c += 1

                time_stop = timeit.default_timer()

                print time_stop - time_start


if __name__=="__main__": main()

