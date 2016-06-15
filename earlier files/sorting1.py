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

	#f = gzip.open('sftp://64.237.51.251/home/account1/Projects/Exelate/exelate_celebrity_20160208.1.tsv.gz', 'rb')


	path =  '/Users/bhishma/Documents/JubaPlus/Celebrity'#'/home/account1/Projects/Exelate'


	allFiles = glob.glob(path + "/*.tsv.gz")

	
	#files = [open('/home/account1/Projects/Exelate/outputF%i.tsv' %i, 'w') for i in range(95)]
	files = [open('/Users/bhishma/Documents/JubaPlus/Celebrity/buffer/outputF%i.tsv' %i, 'w') for i in range(3)]

	c = 0
	count = 0

	for file in allFiles:
		count = 0
		with gzip.open(file, 'rb') as ip :
			ip = csv.reader(ip, dialect = 'excel-tab')
			files[c]= csv.writer(files[c], dialect = 'excel-tab')
			seen = dict()
			for line in ip:
				#v = ip.readline()
				#t = v.split('\t')
				#for line in ip:
				t = line
				if t[0] not in seen.keys():
					files[c].writerow(t[0:6])
					seen[t[0]] = t[6]
					count += 1
	

		c += 1
	
		print count

	time_stop = timeit.default_timer()

	print time_stop - time_start

				


if __name__=="__main__": main()
