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
		self.tier = int(t) + 1
		#self.sessions = int(s)
		self.list = ls

class Node1(object):

    def __init__(self, ls, t):
        self.list = ls
        self.tier = t


def main():

	time_start = timeit.default_timer()	

	""" find nodes fir tiers"""

	#df = pd.read_csv("/home/dummy/try/sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)
	print 'file read'


	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'

	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']


	users = {} 
	url_list = []
	
	session_list = []
	count = 0

	codes = []
	codec = {}
	codesSrt = []
	
	with open('/home/dummy/try/SelectedCodes.csv', 'rb') as sc:
		sc = csv.reader(sc)
		for line in sc:
		
			t = line
			s = str(t[0])
			codesSrt.append(int(t[0]))
			for i in line:
				if i != '':
					codes.append(str(i))
					
					try:
						codec[s].append(str(i))
						
					except KeyError:
						codec[s] = [] 

	#print codes
	#print len(codes)
	#print len(codec)

	#for k in codec.keys():
	#	codesSrt.append(int(k))
	#codesSrt = list(codec.keys())
	codesSrt = sorted(codesSrt)
	
	lst = []
	qc = {}
	#print codesSrt
	#print len(codesSrt)
	with open("/home/account1/Projects/Exelate/sample/UsersSegCodeListFinal.tsv", 'rb') as fp:
		fp = csv.reader(fp, dialect = 'excel-tab')
		for line in fp:
		
			t = line
			s = str(t[0])
			users[s] = Node(t[1],[])
			#print line
			#for index, i in enumerate(line, 2):
			#	print i
			#	lst.append(i)
			lst = line[2:]
			#print lst
			lst = map(int, lst)
			lst = sorted(lst)
			i = 0
			for k in codesSrt:
				if i == len(line) - 2:
					users[s].list.append(str(0))
				else: 
					if lst[i] == k:
						users[s].list.append(str(1))
						try:
							qc[lst[i]] += 1
						except KeyError:
							qc[lst[i]] = 1
						i += 1
				
					else:
						users[s].list.append(str(0))
			#del lst[:]
			#print users[s].list

	print 'append done'
	with open('/home/qc.csv' , 'w') as qp:
		qp = csv.writer(qp)
		qp.writerow(['segment code', 'freq'])
		for key, value in qc.items():
			qp.writerow([key, value])

	path = '/home/account1/Projects/Exelate'
	
	#allFiles = glob.glob(path + '/*.tsv.gz')
	
	#allFiles = ['/home/account1/Projects/Exelate/exelate_celebrity_20160208.1.tsv.gz']
	#allFiles = ['/home/account1/Projects/Exelate/exelate_celebrity_20160208.95.tsv.gz', '/home/account1/Projects/Exelate/exelate_celebrity_20160208.72.tsv.gz']
	count = 0
	dic = {}
	out = {}

	#op = open("/home/account1/Projects/Exelate/sample/UsersSegCodeListBinary1.tsv", 'w')
	#sp = open("/home/account1/Projects/Exelate/sample/InputUserSegCodeQC2.tsv", 'w')
	#op = open('OutputTU.tsv', 'w')

	#op = csv.writer(op, dialect = 'excel-tab')
	#sp = csv.writer(sp, dialect = 'excel-tab')
	#op.writerow(["Segment Code", "Frequency"])

	cn = 0
	qc = 0
	err = {}
	#ip = csv.reader(codecs.open(ip, 'rU', 'utf-16'))
	"""
	for file in allFiles:
		s = timeit.default_timer()
		with gzip.open(file, 'rb') as ip:
			ip = csv.reader(ip, dialect = 'excel-tab')
						
					try:	
					if line[5] not in list1 and line[3] == 'US':
						#sp.writerow(line)
						#qc += 1					
						c = 7
						t = line		
						while (c < len(line)):
							try:
								kk = str(t[0])
								node = users[kk]
								if t[c] in codes:
									for key, value in codec.items():
										if t[c] in value and key not in node.list:			
											node.list.append(key)
											break
				
							except KeyError, e:
								err[str(t[0])] =  1
								#print kk
							finally:
								c += 2
				except IndexError:
					pass
			
	
		e = timeit.default_timer()
		cn += 1
		print e - s, cn
		print len(err)
		#print err.keys() 
		#err = 0
	
	for key, value in users.items():
		for val in value.list:
   			try:
   				out[val][value.tier] += 1
   			except KeyError, e:
   				out[val] = [0, 0, 0, 0]
   				out[val][value.tier] = 1
   				pass
   

   	#op.writerow(["Segment Code", "Frequency"])
	"""
	hdr = ['User ID', 'Tier']
	with open('/home/header.csv') as hd:
		hd = csv.reader(hd)
		for line in hd:
			hdr.append(line[1])	
	
	

	files = [open('/home/binary%i.tsv' %i, 'w') for i in range(10)]
	
	#codesSrt = map(str, codesSrt)
	files[0]= csv.writer(files[0], dialect = 'excel-tab')
	files[0].writerow(hdr)
	f = 0
	c = 0
   	for key, value in users.items():
		count += 1
		c += 1
		if value.list:
			value.list.insert(0, value.tier)	
			value.list.insert(0, key)
			if c == 100000:
				f += 1
				c = 0
				files[f]= csv.writer(files[f], dialect = 'excel-tab')
				files[f].writerow(hdr)
			
   			files[f].writerow(value.list)
	print count

   	#print sum(dic.values())
	time_stop = timeit.default_timer()

	#print count, sum(out.values())

	print time_stop - time_start

				


if __name__=="__main__": main()


