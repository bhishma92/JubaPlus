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

	time_start = timeit.default_timer()	


	path = '/home/account1/Projects/Exelate' #'/Users/bhishma/Documents/JubaPlus/Celebrity'


	allFiles = glob.glob(path + "/*.tsv.gz")

	
	files = [open('/home/account1/Projects/Exelate/Output/outputFFF%i.tsv' %i, 'w') for i in range(95)]
	#files = [open('/Users/bhishma/Documents/JubaPlus/Celebrity/buffer/outputF%i.tsv' %i, 'w') for i in range(2)]

	c = 0


	for file in allFiles:
		print file, c
		count = 0
		print file
		with gzip.open(file, 'rb') as ip :
			ip = csv.reader(ip, dialect = 'excel-tab')
			files[c]= csv.writer(files[c], dialect = 'excel-tab')
			"""
			for line in ip:
				count += 1
				t = line
				if(len(t) >= 7):
					files[c].writerow((t[0], t[1], t[2], t[3], t[4], t[5], t[6]))
	
			"""
		c += 1
	
		print count

	time_stop = timeit.default_timer()

	print time_stop - time_start

				


if __name__=="__main__": main()

