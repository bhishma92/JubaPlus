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
		self.tier = t
		self.sessions = int(s)
		#self.id = i


def main():

	time_start = timeit.default_timer()	

	global PATH
 
 	
	df = pd.read_csv(PATH + "/data/SesOutFinal.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	print 'file read'

	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'

	countries = {} 

	for row in df.itertuples():
		prev_row = row
		break

	for row in df.itertuples():
		try:
			g = 1/int(row[0])

			try:
				if row[1] != prev_row[1]:
					countries[prev_row[5]] += 1
					prev_row = row
			except KeyError:
				countries[prev_row[5]] = 1
				prev_row = row	    

		except ZeroDivisionError as e:
			print 'exception raised'
			pass


	op = open(PATH + '/outputs/countryFreqChart.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')


   	for key, value in countries.items():
   		op.writerow([key, value])


	

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
