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

	dates = {}


	count = 0

	time_start = timeit.default_timer()	

 	"""read output1"""
	df = pd.read_csv("file.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	#df = df.sort_index(by = 5, ascending = True, inplace = True) # sort complete

	print len(df.index)
	
	for i in range(len(df.index)):
		if df[2][i] not in dates:
			dates[df[2][i]] = 1
		else:
			dates[df[2][i]] += 1

	out = pd.DataFrame(dates.items())
	





	out.to_csv("clean.tsv", index = False, header= False, sep='\t')

	#print count, i

	#print df.head(10)

	#print df.tail(2000)

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
