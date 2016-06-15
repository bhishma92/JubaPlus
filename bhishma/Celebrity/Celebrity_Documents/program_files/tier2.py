import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
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

	time_start = timeit.default_timer()	

 
 	
	df = pd.read_csv("sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	print 'file read'
	
	users = {} 
	curr_user = df.iloc[0,0]
	curr_session = df.iloc[0,1]
	url_list = []
	
	session_list = []
	tier1 =0 
	tier2=0 
	tier3 =0
	tier4 = 0
	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'
	visits = [[0 for i in range(5)] for j in range(4)]#lists of lists
	duration_list = [[0 for i in range(5)] for j in range(4)]
	day_diff = [[0 for i in range(4)] for j in range(4)]
	div_dur = [[0 for i in range(5)] for j in range(4)]
	duration = get_sec(df.loc[0,2])
	temp = True
	count = 0
	c = 0
	session_f = [0, 0, 0, 0]

	sess_duration = []


	for i in range(1, len(df.index)):

		if df[0][i] == curr_user:
			if df[3][i] not in url_list:
				url_list.append(df[3][i])
			
		else:
			count += 1
			if url_book in url_list or url_held in url_list:
				users[curr_user] = Node(3, df[1][i-1]) #2 is index of tier4
				tiers = 3
			else:
				if int(df[1][i-1]) == 1 and len(set(url_list)) in [0,1]:
					tiers = 0
					c += 1

				elif int(df[1][i-1]) == 1 and len(set(url_list)) >= 2:
					tiers = 1 #index for tier2
				else:
					tiers = 2 #index for tier3

				users[curr_user] = Node(tiers, df[1][i-1])

			session_f[tiers] += int(df[1][i-1]) 

			#curr_session = df[1][i]
			curr_user = df[0][i]
			
			del url_list[:]
			url_list.append(df[3][i])

	print 'Total number of Users are ' + str(count)

	op = open('IDTierSessions.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')


   	for key, value in users.items():
   		op.writerow([key, value.tier, value.sessions])

   	"""

	fivePlus = [0, 0, 0, 0]
	foTofi = [0, 0, 0, 0]

	for node in users.values():
		if node.sessions >= 5:
			index = 4
			fivePlus[node.tier] += (node.sessions - 4) 
			foTofi[node.tier] += 1
		else:
			index = node.sessions - 1

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

	print fivePlus




	for i in range(4):
		for j in range(5):
			div_dur[i][j] = doSum(i, j, visits) 

	
	

	

	curr_session = df[1][0]
	temp = int(curr_session) - 1
	curr_user = df[0][0]
	usr_page = df[3][0]
	r = users[curr_user].tier
	duration_list[r][int(curr_session)] += get_sec(df[2][0])


	for index, user in enumerate(df[0][1:len(df.index)], start=1):

		if user != curr_user:
			duration_list[users[curr_user].tier][temp] += get_sec(df[2][index-1])

			curr_user = user
			curr_session = df[1][index]
			temp = getTemp(int(curr_session))
			#usr_page = df[3][index]

		elif df[1][index] != curr_session:
			
			if temp != 4:

				sec = get_sec(df[5][index].strip(' GMT')) - get_sec(df[5][index-1].strip(' GMT'))
			
				l1 = map(int, df.iloc[index, 4].split('-'))
				l2 = map(int, df.iloc[index-1, 4].split('-'))


				d1 = date(l1[0], l1[1], l1[2])
				d2 = date(l2[0], l2[1], l2[2])
	
				d = (d1 - d2).days

				if sec < 0:
					d = d - 1

				day_diff[users[curr_user].tier][temp] += d
			
			duration_list[users[curr_user].tier][temp] += get_sec(df[2][index-1])
			curr_session = df[1][index]
			temp = getTemp(int(curr_session))

		else:
			pass
	


	
	for i in range(4):
		for j in range(5):
			if visits[i][j] == 0:
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

	print session_f[0]
	print session_f[1]
	print session_f[2]
	print session_f[3]

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

	"""

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
