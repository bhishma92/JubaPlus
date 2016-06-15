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



class Node(object):

	def __init__(self, t, s):
		self.tier = int(t)
		self.sessions = int(s)
		#self.id = i


def main():

	time_start = timeit.default_timer()	

 	global PATH

 	op = open(PATH + '/outputs/sample.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

	with open(PATH + '/data/sampleBig.tsv', 'rb') as ip:
		ip = csv.reader(ip, dialect = 'excel-tab')
		del1 = 0
		count = 0
		for line in ip:
			count += 1
			if count < 61:
				pass
			else:	
				if del1 < 3:
					op.writerow(line)
				else:
					break
				del1 += 1

	

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
