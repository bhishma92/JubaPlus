import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
import csv
from array import array
import glob

PATH = '/users/bhishma/Documents/JubaPlus/Celebrity'

def get_sec(s):
    l = s.strip(' GMT').split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def findDays(a, b):
	
	l1 = map(int, b.split('-'))
	l2 = map(int, a.split('-'))


	d1 = date(l1[0], l1[1], l1[2])
	d2 = date(l2[0], l2[1], l2[2])
		
	return (d1 - d2).days



class Node(object):

	def __init__(self, t, d, s):
		self.tier = int(t)
		self.days = int(d)
		self.sessions = int(s)


def method(m, l, r):
	su = 0
	for i in range(m, 288):
		su += l[i][r]
	return su 

def main():

	global PATH
	m = 0
	users = {}
	ls = [[0 for j in range(5)] for i in range(288)]


			#ls[int(t[2])-1][int(t[1])+1] += 1
	
	"""
	for i in range(288):
		ls[i][1] = method(i, ls, 1)
		ls[i][2] = method(i, ls, 2)
		ls[i][3] = method(i, ls, 3)
		ls[i][4] = method(i, ls, 4)
	#print m		
	for i in range(288):
		ls[i][0] = i+1


	op1 = open(PATH + '/outputs/visits1.tsv', 'w')
	op1 = csv.writer(op1, dialect = 'excel-tab')

	op1.writerows(ls)

	

	print 'tier file read'

	"""
	df = pd.read_csv(PATH + "/data/dayDifference300Samples.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)
	
	#df.columns = ['U','SES', 'DUR', 'SC','C','URL','D','T']

	us = [] #qc


	for a in df[0]:i
		if a not in us:
			us.append(a)


	with open(PATH + '/outputs/IDTierSessionsUS1.tsv', 'rb') as fp:
		fp = csv.reader(fp, dialect = 'excel-tab')
		for line in fp:
			t = line
			s = str(t[0])
			if s in us:
				users[s] = Node(t[1], 0, t[2])

	#print df.head(10)

	#df = df.head(300)

	#df.to_csv(PATH + "/data/dayDifference300Samples.tsv", index = False, header= False, sep='\t')

	maxd = 0

	print 'file read'

	for row in df.itertuples():
		prev_row = row
		curr_user = row[1]
		start_date = row[7]
		start_time = row[8]
		curr_session = int(prev_row[2])
		last_session = int(row[2])
		break

	for row in df.itertuples():
		try:
			g = 1/int(row[0])

			if row[1] != curr_user:
				if users[prev_row[1]].sessions != 1:
					#print users[prev_row[1]].sessions
					end_date = prev_row[7]
					end_time = prev_row[8]

					sec = get_sec(end_time) - get_sec(start_time)

					d = findDays(start_date, end_date)

					if sec < 0:
						d = d - 1

					if maxd < d:
						maxd = d

					print d

					users[prev_row[1]].days = d
				else:
					users[prev_row[1]].days = 0

				curr_session = int(row[2])	
				curr_user = row[1]
				start_date = row[7]
				start_time = row[8]

			prev_row = row
			last_session = int(row[2])

		except (ZeroDivisionError, KeyError) as e:
			print 'exception raised'

			pass


	end_date = prev_row[7]
	end_time = prev_row[8]

	sec = get_sec(end_time) - get_sec(start_time)

	d = findDays(start_date, end_date)

	if sec < 0:
		d = d - 1

	if maxd < d:
		maxd = d


	if last_session != curr_session:
		users[curr_user].days = d
	else:
		users[curr_user].days = 0

	print maxd

	table = [[0 for j in range(4)] for i in range(maxd+1)]

	for key, value in users.items():
		try:
			table[value.days][value.tier] += 1

		except IndexError:
			print value.days, value.tier

	op = open(PATH + '/outputs/DayDifferenceOutputQC.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

	op.writerows(table)
	













if __name__=="__main__": main()