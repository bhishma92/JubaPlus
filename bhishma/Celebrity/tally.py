import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
import csv
from array import array


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

	count = 0

	time_start = timeit.default_timer()	

 	"""read output1"""
	df = pd.read_csv("/home/dummy/file.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	#df.sort_index(by = 2, ascending = True, inplace = True)

	for i in range(len(df.index)):
		#print df[2][i]
		if df[2][i] == '12-31-2016' or df[2][i] == '01-01-2016':
			count +=1


	print count, i

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()

