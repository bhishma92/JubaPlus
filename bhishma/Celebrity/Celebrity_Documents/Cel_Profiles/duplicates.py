import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob
import csv
import fileinput

"""
files = [open('filename%i.txt' %i, 'w') for i in range(1,4)]
with open('filename.txt', 'r') as input:
    for line in input:
        columns = line.strip().split()
        for j in range(1,4):
            files[j-1].write('{:10}{:10}\n'.format(columns[0], columns[j]))
for f in files:
    f.close()


import fileinput
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('1.csv', inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file   


"""
def main():

	time_start = timeit.default_timer()	

	#f = gzip.open('sftp://64.237.51.251/home/account1/Projects/Exelate/exelate_celebrity_20160208.1.tsv.gz', 'rb')


	path = '/Users/bhishma/Documents/JubaPlus/Celebrity/buffer'


	allFiles = glob.glob(path + "/*.tsv")


	
	files = [open('outputF%i.tsv' %i, 'w') for i in range(1)]

	c = 0

	for file in allFiles:

		seen = set()

		for line in fileinput.FileInput(file, inplace=1):

			print line

			if line in seen: continue

			seen.add(line)
			files[0].write(line)



	


	time_stop = timeit.default_timer()

	print time_stop - time_start

				


if __name__=="__main__": main()
