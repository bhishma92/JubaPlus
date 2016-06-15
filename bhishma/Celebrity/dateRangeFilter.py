import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob



def main():

	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']
        drop_dates = []

	df = pd.read_csv('/home/dummy/try/fileNew.tsv', header=None, dtype = object, delimiter="\t", error_bad_lines = False)
	"""
        for row in df.itertuples():
                if row[5] in list1:
                        drop_dates.append(int(row[0]))

	

        df.drop(df.index[drop_dates], inplace = True)
        print len(df.index), len(drop_dates)
	"""
	print df.head(10)
	print df.tail(10)

	#df.to_csv('/home/dummy/try/fileNewFinal'+ '.tsv', index = False, header = None, sep='\t')


if __name__=="__main__": main()
