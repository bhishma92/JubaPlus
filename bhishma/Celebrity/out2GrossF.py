import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob
import csv
import itertools

def mycsv_reader(csv_reader): 
	count = 0 
	flip = True
  	while True: 
  		try: 
  			yield next(csv_reader) 
  		except csv.Error:
			#count +=1
			#if count > 1000 and flip:
				#print "errors"
				#flip = False
  			pass
  		continue


def main():

	time_start = timeit.default_timer()	

	path = '/home/account1/Projects/Exelate'
	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']

	allFiles = glob.glob(path + '/*.tsv.gz')
	#allFiles = ['data.tsv']
	print len(allFiles)
	count = 0
	dic = {}

	op = open("/home/account1/Projects/Exelate/Output2SE.tsv", 'w')
	#op = open('Output2SE.tsv', 'w')

	op = csv.writer(op, dialect = 'excel-tab')

	op.writerow(["Segment Code", "Frequency"])


	for file in allFiles:
		s = timeit.default_timer() 
		with gzip.open(file, 'rb') as ip:
			#ip = mycsv_reader( csv.reader(ip, dialect = 'excel-tab') )
			ip = csv.reader(ip, dialect = 'excel-tab')
			
			for line in ip:
				try:
					if line[5] not in list1:
					
						c = 7
						t = line
						while (c < len(line)):
							if t[c] not in dic:
								dic[t[c]] = 1
							else:
								dic[t[c]] += 1
							c += 2
				except IndexError:
					pass

		e = time_start = timeit.default_timer() 
		print e-s, len(dic)

	for key, value in dic.items():
   		op.writerow([key, value])
   


	time_stop = timeit.default_timer()

	print time_stop - time_start

				


if __name__=="__main__": main()


