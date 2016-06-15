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


class Location(object):

	def __init__(self, c, sc):
		self.country = c
		self.stct = sc

	def __hash__(self):
		return hash((self.country, self.stct))

	def __eq__(self, other):
		return (self.country, self.stct) == (other.country, other.stct)
	
	def __ne__(self, other):
		# Not strictly necessary, but to avoid having both x==y and x!=y
		# True at the same time
		return not(self == other)

class Node(object):

	def __init__(self, t, r):
		self.tier = int(t)
		self.nRow = r
		


def main():

	time_start = timeit.default_timer()	

	global PATH
 
 	
	df = pd.read_csv(PATH + "/data/SesOutFinal.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)
	
	df.columns = ['U','SES', 'DUR', 'SC','C','URL','D','T']

	#df = df.loc[df['C'] == 'US']

	#print df.head(100)

	print 'file read'

	#seconds = df['T'].str.strip(' GMT').str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))
	#secDur =  df['DUR'].str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))
	#print df['DUR'].head(10)
	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'

	users = {}
	url_list = [] 
	usr_count = 0

	
	for row in df.itertuples():
		prev_row = row
		curr_user = row[1] + row[5]
		url_list.append(row[6])
		curr_country = row[5]
		break

	url_list.append(prev_row[6])

	for row in df.itertuples():
		try:
			g = 1/int(row[0])

			try:
				if row[1] + row[5] == curr_user:
					if row[6] not in url_list:
						url_list.append(row[6])
						
				else:
					usr_count += 1
					if (url_book in url_list) or (url_held in url_list):
						users[curr_user] = Node(3, prev_row)
						tiers = 3
					else:

						if int(prev_row[2]) == 1 and len(set(url_list)) in [0,1]:
							tiers = 0
						elif int(prev_row[2]) == 1 and len(set(url_list)) >= 2:
							tiers = 1
						else:
							tiers = 2

						users[curr_user] = Node(tiers, prev_row)

					curr_user = row[1] + row[5]
					

					del url_list[:]
					url_list.append(row[6])

				prev_row = row			

			except KeyError:
				print 'error!'   

		except ZeroDivisionError as e:
			print 'exception raised'
			pass

	#last user

	usr_count += 1
	if (url_book in url_list) or (url_held in url_list):
		users[curr_user] = Node(3, prev_row)
		tiers = 3
	else:

		if int(prev_row[2]) == 1 and len(set(url_list)) in [0,1]:
			tiers = 0
		elif int(prev_row[2]) == 1 and len(set(url_list)) >= 2:
			tiers = 1
		else:
			tiers = 2

		users[curr_user] = Node(tiers, prev_row)	



	print 'Total number of Users are ' + str(usr_count)

	fivePlus = [0, 0, 0, 0]
	foTofi = [0, 0, 0, 0]
	tier1, tier2, tier3, tier4 = 0, 0, 0, 0
	visits = [[0 for i in range(5)] for j in range(4)]#lists of lists
	duration_list = [[0 for i in range(5)] for j in range(4)]
	day_diff = [[0 for i in range(4)] for j in range(4)]
	div_dur = [[0 for i in range(5)] for j in range(4)]



	
	op = open(PATH + '/outputs/allCountryQCNew.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

	tier_list = [0,0,0,0]
	loc = {}

   	for key, value in users.items():
   		cn += 1
   		k = Location(value.nRow[5], value.nRow[4]) #5 country 4 state_city
   	
   		try:
   			loc[k][value.tier] += 1

   		except KeyError:
   			loc[k] = [0,0,0,0]
   			loc[k][value.tier] += 1

   	print 'reading complete'


	for key, value in loc.items():
		
		op.writerow([key.country, key.stct, value[0], value[1], value[2], value[3]])




	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
