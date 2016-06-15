import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
import csv
from array import array


#PATH = '/users/bhishma/Documents/JubaPlus/Celebrity'



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
 
 	
	df = pd.read_csv("/home/dummy/try/SesOutFinalUS.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)
	
	df.columns = ['U','SES', 'DUR', 'SC','C','URL','D','T']

	#df = df.loc[df['C'] == 'US']

	#print df.head(100)

	print 'file read'

	seconds = df['T'].str.strip(' GMT').str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))
	secDur =  df['DUR'].str.strip(' GMT').str.split(':').apply(lambda x: int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2]))

	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'

	users = {}
	url_list = [] 
	usr_count = 0

	
	for row in df.itertuples():
		prev_row = row
		curr_user = row[1]
		url_list.append(row[6])
		break

	url_list.append(prev_row[6])

	for row in df.itertuples():
		try:
			g = 1/int(row[0])

			try:
				if row[1] == curr_user:
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

					curr_user = row[1]
					del url_list[:]
					url_list.append(row[6])

				prev_row = row			

			except KeyError:
				print 'error!'   

		except ZeroDivisionError as e:
			print 'exception raised'
			pass

        

	print 'Total number of Users are ' + str(usr_count)

	print users['0009561d1803097c4fbbf14a590ed46f'].tier, int(users['0009561d1803097c4fbbf14a590ed46f'].nRow)

	fivePlus = [0, 0, 0, 0]
	foTofi = [0, 0, 0, 0]
	tier1, tier2, tier3, tier4 = 0, 0, 0, 0
	visits = [[0 for i in range(5)] for j in range(4)]#lists of lists
	duration_list = [[0 for i in range(5)] for j in range(4)]
	day_diff = [[0 for i in range(4)] for j in range(4)]
	div_dur = [[0 for i in range(5)] for j in range(4)]


 


	#fivePlus = [0, 0, 365175, 38908]
	#print fivePlus

	#visits = [[870358, 0, 0, 0, 0], [1019927, 0, 0, 0, 0], [0, 147602, 59849, 31676, 69748], [1674, 965, 712, 593, 3502]]
	



	

	for node in users.values():
		if int(node.nRow[2]) >= 5:
			index = 4
			fivePlus[node.tier] += int(node.nRow[2]) - 4
			foTofi[node.tier] += 1
		else:
			index = int(node.nRow[2]) - 1

		if node.tier == 0:
			tier1 += 1
			visits[0][index] += 1
		elif node.tier == 1:
			tier2 += 1
			visits[1][index] += 1
		elif node.tier ==2:
			tier3 += 1
			visits[2][index] += 1
		else:
			tier4 += 1
			visits[3][index] += 1

	for i in range(4):
		for j in range(5):
			div_dur[i][j] = doSum(i, j, visits)

	print fivePlus



        """
	
	op = open(PATH + '/outputs/allCountryQC.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

	tier_list = [0,0,0,0]
	loc = {}

   	for key, value in users.items():
   		k = Location(value.nRow[5], value.nRow[4]) #5 country 4 state_city
   		
   		try:
   			loc[k][value.tier] += 1

   		except KeyError:
   			loc[k] = [0,0,0,0]
   			loc[k][value.tier] += 1


	for key, value in loc.items():
		
		op.writerow([key.country, key.stct, value[0], value[1], value[2], value[3]])

	"""




	for row in df.itertuples():
		prev_row = row
		curr_user = row[1]
		curr_session = row[2]
		temp = int(curr_session) - 1
		r = users[curr_user].tier
		duration_list[r][int(curr_session)] += secDur.at[row[0]]

		break


	c = 0
	for row in df.itertuples():

		if row[1] != curr_user:
			duration_list[users[curr_user].tier][temp] += secDur.at[prev_row[0]]

			curr_user = row[1]
			curr_session = row[2]
			temp = getTemp(int(curr_session))

		elif row[1] != curr_session:
			
			if temp != 4:

				sec = seconds.at[row[0]] - seconds.at[prev_row[0]]

				l1 = map(int, row[7].split('-'))
				l2 = map(int, prev_row[7].split('-'))


				d1 = date(l1[0], l1[1], l1[2])
				d2 = date(l2[0], l2[1], l2[2])
	
				d = (d1 - d2).days

				if sec < 0:
					d = d - 1
					#print d

				#print temp , users[curr_user].tier, c
				try:
					day_diff[users[curr_user].tier][temp] += d
				except KeyError:
					print 'we got a KeyError'
					print c, len(df.index)
					pass
			
			try:
				duration_list[users[curr_user].tier][temp] += secDur.at[prev_row[0]]
			except KeyError:
				pass
			curr_session = row[2]
			temp = getTemp(int(curr_session))


		prev_row = row
		c += 1

	for i in range(4):
		for j in range(5):
			if div_dur[i][j] == 0:
				duration_list[i][j] = 0
			else:
				if j == 4 and fivePlus[i] != 0:
					temp = fivePlus[i]
				else:
					temp = div_dur[i][j] 

				duration_list[i][j] = str(datetime.timedelta(seconds=int(duration_list[i][j]/temp)))
	
			

	
	for i in range(4):
		for j in range(4):
			if div_dur[i][j] == 0:
				day_diff[i][j] = 0
			else:
				if j == 3 and foTofi[i] != 0:
					temp = foTofi[i]
				else:
					temp = div_dur[i][j] 

				day_diff[i][j] = day_diff[i][j]/temp
	
	
	print tier1, tier2, tier3, tier4



	print '\n'

	print visits[0]
	print visits[1]
	print visits[2]
	print visits[3]

	
	
	print '\n'

	print div_dur[0]
	print div_dur[1]
	print div_dur[2]
	print div_dur[3]

	print '\n'

	print duration_list[0]
	print duration_list[1]
	print duration_list[2]
	print duration_list[3]

	print '\n'
	
	
	print day_diff[0]
	print day_diff[1]
	print day_diff[2]
	print day_diff[3]

	print '\n'
	

	print tier1*100/(tier1 + tier2 + tier3+tier4) 





	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()

