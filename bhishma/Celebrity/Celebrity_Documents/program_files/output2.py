import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
import csv
from array import array




def main():

	time_start = timeit.default_timer()	

 
 	
	df = pd.read_csv("sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	print 'file read'
	


			










if __name__=="__main__": main()
