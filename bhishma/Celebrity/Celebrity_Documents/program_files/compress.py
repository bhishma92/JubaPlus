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
import codecs


class Node(object):

	def __init__(self, t, ls):
		self.tier = t
		#self.sessions = int(s)
		self.list = ls

class Node1(object):

    def __init__(self, ls, t):
        self.list = ls
        self.tier = t


def main():

	time_start = timeit.default_timer()	

	""" find nodes fir tiers"""

	df = pd.read_csv("/home/dummy/try/sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)
	print 'file read'


	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'

	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']


	users = {} 
	curr_user = df.iloc[0,0]
	curr_session = df.iloc[0,1]
	url_list = []
	
	session_list = []
	count = 0

	for i in range(1, len(df.index)):

		if df[0][i] == curr_user:
			if df[3][i] not in url_list:
				url_list.append(df[3][i])
			
		else:
			count += 1
			if url_book in url_list or url_held in url_list:
				users[curr_user] = Node(3, []) #2 is index of tier4
			else:
				if int(df[1][i-1]) == 1 and len(set(url_list)) in [0,1]:
					tiers = 0

				elif int(df[1][i-1]) == 1 and len(set(url_list)) >= 2:
					tiers = 1 #index for tier2

				else:
					tiers = 2 #index for tier3

				users[curr_user] = Node(tiers, [])

		

			curr_user = df[0][i]
			
			del url_list[:]
			url_list.append(df[3][i])

	print 'Total number of Users are ' + str(count)




	path = '/home/account1/Projects/Exelate'

	allFiles = glob.glob(path + '/*.tsv.gz')
	#allFiles = ['data.tsv']

	count = 0
	dic = {}
	out = {}

	op = open("/home/account1/Projects/Exelate/Output2TU.tsv", 'w')
	#op = open('OutputTU.tsv', 'w')

	op = csv.writer(op, dialect = 'excel-tab')

	#op.writerow(["Segment Code", "Frequency"])

	c = 0

	#ip = csv.reader(codecs.open(ip, 'rU', 'utf-16'))
	for file in allFiles:
		s = timeit.default_timer()
		with open(file, 'rb') as ip:
			ip = csv.reader(ip, dialect = 'excel-tab')
			
			
			for line in ip:
				try:
					if line[5] not in list1:
						c = 7
						t = line
						
						while (c < len(line)):
							try:
								node = users[t[0]]
								if t[c] not in node.list:
									node.list.append(t[c])
									count += 1
							except KeyError, e:
								pass
							finally:
								c += 2
				except IndexError:
					pass


		e = timeit.default_timer()
		c += 1
		print e - s, c


	for key, value in users.items():
		for val in value.list:
   			try:
   				out[val][value.tier] += 1
   			except KeyError, e:
   				out[val] = [0, 0, 0, 0]
   				out[val][value.tier] = 1
   				pass
   

   	#op.writerow(["Segment Code", "Frequency"])

   	for key, value in out.items():
   		op.writerow([key, value[0], value[1], value[2], value[3]])


   	#print sum(dic.values())
	time_stop = timeit.default_timer()

	#print count, sum(out.values())

	print time_stop - time_start

				


if __name__=="__main__": main()

