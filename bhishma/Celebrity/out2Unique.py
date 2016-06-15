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


def mycsv_reader(csv_reader): 
	count = 0
  	while True: 
  		try: 
  			yield next(csv_reader) 
  		except csv.Error:
  			pass
  		continue

class Node(object):

    def __init__(self, t, ls):
        self.lis = ls
        self.tier = t



def main():

	time_start = timeit.default_timer()	
	
	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']
	
	path = '/home/account1/Projects/Exelate'

	allFiles = glob.glob(path + '/*.tsv.gz')
	#allFiles = ['/home/sample.tsv']
	#allFiles = ['/home/account1/Projects/Exelate/exelate_celebrity_20160208.95.tsv.gz', '/home/account1/Projects/Exelate/exelate_celebrity_20160208.72.tsv.gz']

	count = 0
	dic = {}
	out = {}
	users = {}
        #op = open("/home/account1/Projects/Exelate/Output2USEUSFINAL.tsv", 'w')	
	#op = open('Output3.tsv', 'w')

	#op = csv.writer(op, dialect = 'excel-tab')

        op = open("/home/account1/Projects/Exelate/sample/Outsame.tsv", 'w')
        sp = open("/home/account1/Projects/Exelate/sample/Insame.tsv", 'w')
        #op = open('OutputTU.tsv', 'w')

        op = csv.writer(op, dialect = 'excel-tab')
        sp = csv.writer(sp, dialect = 'excel-tab')

	#op.writerow(["Segment Code", "Frequency"])

        with open('/home/dummy/try/IDTierSessionsUS1.tsv', 'rb') as fp:
                fp = csv.reader(fp, dialect = 'excel-tab')
                for line in fp:
                        t = line
                        s = str(t[0])
                        users[s] = Node(t[1],[])



	print 'file read'

	cn = 0
	err = {}
	#ip = csv.reader(codecs.open(ip, 'rU', 'utf-16'))
	for file in allFiles:
		s = timeit.default_timer()
		if cn == 1:
			break
		print file
		with gzip.open(file, 'rb') as ip:
			ip = csv.reader(ip, dialect = 'excel-tab')
			dum = 0
			
			for line in ip:
				try:
					if dum == 0:
						rep = line[0]

					if line[5] not in list1 and line[3] == 'US' and len(line) >= 30 and line[0] == rep and dum <= 3:
						sp.writerow(line)
						c = 7
						t = line
						dum += 1
						
						while (c < len(line)):
							try:
								l = users[t[0]].lis
								if t[c] not in l:
									l.append(t[c])			
								#l = dic[t[0]]
								#if t[c] not in l:
								#	l.append(t[c])
								#	count += 1
							except KeyError, e:
								err[str(t[0])] =  1
								#dic[t[0]] = []
								#dic[t[0]].append(t[c])
								#count += 1
								pass
							finally:
								c += 2
				except IndexError:		
					pass
		cn += 1
		
		e = timeit.default_timer()
		
		print e - s, cn	
		print len(err)

	for key, value in users.items():
		for val in value.lis:
   			try:
   				out[val] += 1
   			except KeyError, e:
   				out[val] = 1
   				pass
   

   	#op.writerow(["Segment Code", "Frequency"])

   	for key, value in out.items():
   		op.writerow([key, value])


   	#print sum(dic.values())
	time_stop = timeit.default_timer()

	print count, sum(out.values())

	print time_stop - time_start

				


if __name__=="__main__": main()


