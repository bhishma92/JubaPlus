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

	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']

	drop_list = []

	count = 0

	time_start = timeit.default_timer()	

 	
	df = pd.read_csv("file1.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	print len(df)
	#df.sort_index(by = 2, ascending = True, inplace = True)
	
	for i in range(len(df.index)):

		if df[2][i] in list1:
			drop_list.append(i)


	df.drop(df.index[drop_list], inplace=True)

	df.to_csv("dataSpecDelete.tsv", index = False, header= False, sep='\t')

	print len(df)

	print len(drop_list)

	#print df.head(10)

	#print df.tail(2000)

	time_stop = timeit.default_timer()

	print time_stop - time_start
	

			










if __name__=="__main__": main()

