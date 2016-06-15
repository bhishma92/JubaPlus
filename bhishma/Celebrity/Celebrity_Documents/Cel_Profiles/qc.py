import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
import csv
from array import array



PATH = '/users/bhishma/Documents/JubaPlus/Celebrity'

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

def method(m, l, r, nn):
	su = 0
	for i in range(m, nn):
		su += l[i][r]
	return su 


class Node(object):

	def __init__(self, t, s):
		self.tier = int(t)
		self.sessions = int(s)
		#self.id = i


def main():

	time_start = timeit.default_timer()	

	global PATH
 
 	
	df = pd.read_csv(PATH + "/data/visitsSample200.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	#df = df1.head(200)

	#df.to_csv(PATH + "/data/visitsSample200.tsv", index = False, header= False, sep='\t')

	#df1 = df.head(200)

	#df1.to_csv(PATH + "/outputs/sampleOut1.tsv", index = False, header= None, sep='\t')

	
	users = {}
	us = []

	ls = [[0 for i in range(5)] for j in range(6)]

	print 'file read'

	for a in df[0]:
		if a not in us:
			us.append(a)

	
	df.columns = [0,1,2,8,9,3,4,5]

	with open(PATH + '/outputs/IDTierSessionsUSafterQC.tsv', 'rb') as fp:
		fp = csv.reader(fp, dialect = 'excel-tab')
		for line in fp:
			t = line
			s = str(t[0])
			if s in us:
				users[s] = Node(t[1],t[2])
				ls[int(t[2])-1][int(t[1])+1] += 1
	n = 0


	for value in users.values():
		if value.sessions > n:
			n = value.sessions

	

	print n

	for i in range(n):
		ls[i][1] = method(i, ls, 1, n)
		ls[i][2] = method(i, ls, 2, n)
		ls[i][3] = method(i, ls, 3, n)
		ls[i][4] = method(i, ls, 4, n)
	#print m		
	for i in range(n):
		ls[i][0] = i+1


	op1 = open(PATH + '/outputs/visits1QC200.tsv', 'w')
	op1 = csv.writer(op1, dialect = 'excel-tab')

	op1.writerows(ls)

	

	print 'tier file read'

	

	

	time_stop = timeit.default_timer()

	print time_stop - time_start

	
			










if __name__=="__main__": main()
