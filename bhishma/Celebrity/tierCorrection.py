import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
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

 	"""read output1"""
	df = pd.read_csv("/home/dummy/sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	users = {} 
	curr_user = df.iloc[0,0]
	curr_session = df.iloc[0,1]
	freq = 0
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

	sess_duration = []

	"""Creating Data Structure"""

	for i in range(1, len(df.index)):

		if df[0][i] == curr_user:
			if df[3][i] not in url_list:
				url_list.append(df[3][i])
			
		else:
			count += 1
			if url_book in url_list or url_held in url_list:
				users[curr_user] = Node(3, df[1][i-1]) #2 is index of tier4
			else:
				if int(df[1][i-1]) == 1 and len(set(url_list)) == 1:
					tiers = 0

				elif int(df[1][i-1]) == 1 and len(set(url_list)) >= 2:
					tiers = 1 #index for tier2
				else:
					tiers = 2 #index for tier3

				users[curr_user] = Node(tiers, df[1][i-1])

			#curr_session = df[1][i]
			curr_user = df[0][i]
			
			del url_list[:]
			url_list.append(df[3][i])

	print count
	fplus = [0,0,0,0]

	"""filling values"""
	for node in users.values():
		if node.sessions > 5:
			fplus[node.tier] += 1
			index = 4 
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

	"""make divisions for average """

	for i in range(4):
		for j in range(5):
			div_dur[i][j] = doSum(i, j, visits) 

	
	

	""" duration visits """

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
			usr_page = df[3][index]

		elif df[1][index] != curr_session:
			#duration_list[users[curr_user].tier][temp] += get_sec(df[2][index-1])
			#if users[curr_user].tier == 2:
				#print df[2][index-1], index -1
				#count += 1

			if temp != 4:

				sec = get_sec(df[5][index].strip(' GMT')) - get_sec(df[5][index-1].strip(' GMT'))
			
				d1 = map(int, df.iloc[index, 4].split('-'))
				d2 = map(int, df.iloc[index-1, 4].split('-'))
				t1 = map(int, df.iloc[index, 5].strip(' GMT').split(':'))
				t2 = map(int, df.iloc[index-1, 5].strip(' GMT').split(':'))


				a = datetime.datetime(d1[2],d1[0],d1[1],t1[0],t1[1],t1[2])
				b = datetime.datetime(d2[2],d2[0],d2[1],t2[0],t2[1],t2[2])

				day_diff[users[curr_user].tier][temp] += int((a-b).total_seconds()/86400)

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
				duration_list[i][j] = str(datetime.timedelta(seconds=int(duration_list[i][j]/div_dur[i][j])))
			


	for i in range(4):
		for j in range(4):
			if j == 3:
				div_dur[i][j] -= fplus[i]
			else:
				if div_dur[i][j] == 0:
					day_diff[i][j] = 0
				else:
					day_diff[i][j] = day_diff[i][j]/div_dur[i][j]



	#duration_list = [[ str(datetime.timedelta(seconds=int(duration_list[i][j]/visits[i][j]))) for j in range(5) ] for i in range(3)] 

	#day_diff = [[ str(datetime.timedelta(seconds=int(day_diff[i][j]/visits[i][j]))) for j in range(4)] for i in range(3)] 
	

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

