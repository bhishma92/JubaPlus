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

	"""
	path = '/home/account1/Projects/Exelate'


	allFiles = glob.glob(path + "/*.tsv.gz")

	
	files = [open('/home/account1/Projects/Exelate/outputF%i.tsv' %i, 'w') for i in range(95)]

	c = 0

	for file in allFiles:

		with gzip.open(file, 'rb') as ip :
			ip = csv.reader(ip, dialect = 'excel-tab')
			files[c]= csv.writer(files[c], dialect = 'excel-tab')

			for row in ip:
				#final.writerows(row[0:2])
				del row[7:]
				files[c].writerow(row)

		c += 1

	"""

	time_start = timeit.default_timer()	

	path = '/Users/bhishma/Documents/JubaPlus/Celebrity' #'ExelateOutput'


	allFiles = glob.glob(path + "/*.tsv.gz")

	#files = [open('/home/account1/Projects/Exelate/SortedOutputF%i.tsv' %i, 'w') for i in range(95)]
	files = [open('outputF%i.tsv' %i, 'w') for i in range(2)]

	c = 0	

	for file in allFiles:

		with gzip.open(file, 'rb') as ip :
				ip = csv.reader(file, dialect = 'excel-tab')
				op = csv.writer(op, dialect = 'excel-tab')

				for line in ip:
					#final.writerows(row[0:2])
					del line[7:]
					op.writerow(line)
				

				"""

				drop_list = []
				index = 0 
				count = 0
				
				while index != len(df):
					val = True
					for i in range(0, 7):
						if isinstance(df.iloc[index, i], basestring) == False:
							val = False
							#print index, df.iloc[index, i]

					if val == False:
						drop_list.append(index)
					else:
						count += 1
						temp = df.iloc[index, 6].strip(' GMT').split(':')
						if int(temp[2]) < 10:
							temp[2] = temp[2].zfill(2)
							df.iloc[index, 6] = ':'.join(temp) + ' GMT'	


					index += 1


				df.drop(df.index[drop_list], inplace=True)
				
				

				df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete

				print len(df)

				df.to_csv('sorted1.tsv', index = False, header = None, sep='\t')

				"""


	time_stop = timeit.default_timer()

	print time_stop - time_start

				


if __name__=="__main__": main()
