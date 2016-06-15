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
	df = pd.read_csv("file.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)


	df[2] =pd.to_datetime(df[2])

	df.sort_index(by = [0, 2, 3], ascending = [True, True, True], inplace = True) # sort complete

	df.to_csv("file10.tsv", index = False, header= False, sep='\t')

	#print count, i

	#print df.head(10)

	#print df.tail(2000)

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
