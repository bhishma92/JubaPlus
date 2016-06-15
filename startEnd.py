import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
import csv
from array import array
import time

def get_sec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def getTemp(t):
	if t > 5:
		return 4
	else:
		return t - 1

def doSum(a, b, visits):
	s = 0
	while b != 5:
		s += visits[a][b]
		b += 1
	return s



class Node(object):

	def __init__(self, t, s):
		self.tier = t
		self.sessions = int(s)
		#self.id = i


def main():

	curr = '2016-11-17'
	currDate = time.strptime(curr, '%Y-%m-%d')

	count = 0

	time_start = timeit.default_timer()	

 	"""read output1"""
	df = pd.read_csv("/home/dummy/try/file1.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	print len(df)
	#df.sort_index(by = 2, ascending = True, inplace = True)

	for i in range(len(df.index)):
		temp = df[2][i]
		newdate = time.strptime(temp, '%Y-%m-%d')
		if newdate < currDate:
			df.drop(i)
			count += 1


	df.to_csv("/home/dummy/try/dataSpec.tsv", index = False, header= False, sep='\t')

	print len(df)

	print count, i

	#print df.head(10)

	#print df.tail(2000)

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()

