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
 	
	df = pd.read_csv(PATH + "/data/sesOut.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)


	print 'file read'
	
	nodeDic = {} 
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
	nodeDic = {}

	sess_duration = []


	with open(PATH + '/data/IDTierSessions.tsv', 'rb') as ip:
		ip = csv.reader(ip, dialect = 'excel-tab')

		for line in ip:
			l = line
			nodeDic[l[0]] = Node(l[1], l[2])


	   


	visits = [	[916107, 0, 0, 0, 0],
				[1021988, 0, 0, 0, 0],
				[343193, 343193, 180845, 114193, 78700],
				[7186, 5552, 4609, 3912, 3357]  ]
	

	

	curr_session = df[1][0]
	temp = int(curr_session) - 1
	curr_user = df[0][0]
	usr_page = df[3][0]
	r = nodeDic[curr_user].tier
	duration_list[r][int(curr_session)] += get_sec(df[2][0])


	for index, user in enumerate(df[0][1:len(df.index)], start=1):

		if user != curr_user:
			duration_list[nodeDic[curr_user].tier][temp] += get_sec(df[2][index-1])

			curr_user = user
			curr_session = df[1][index]
			temp = getTemp(int(curr_session))
			#usr_page = df[3][index]

		elif df[1][index] != curr_session:
			
			duration_list[nodeDic[curr_user].tier][temp] += get_sec(df[2][index-1])
			curr_session = df[1][index]
			temp = getTemp(int(curr_session))

		else:
			pass
	


	
	for i in range(4):
		for j in range(5):
			if visits[i][j] == 0:
				duration_list[i][j] = 0
			else:
				duration_list[i][j] = str(datetime.timedelta(seconds=int(duration_list[i][j]/visits[i][j])))
	
			

	
	
	
	print tier1, tier2, tier3, tier4



	print '\n'

	print visits[0]
	print visits[1]
	print visits[2]
	print visits[3]

	print '\n'

	print duration_list[0]
	print duration_list[1]
	print duration_list[2]
	print duration_list[3]

	print '\n'
	
	
	

	#print tier1*100/(tier1 + tier2 + tier3+tier4) 

	

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
