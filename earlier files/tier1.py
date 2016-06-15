import pandas as pd
import collections
import operator
import sys
import timeit
import datetime

class Node(object):

	def __init__(self, t, s):
		self.tier = t
		self.sessions = s
		#self.id = i
	def addDuration(self, d):
		self.duration = d
	def avgDuration(self):
		sec = int(self.duration/self.sessions)
		#return str(datetime.timedelta(seconds=sec))
		return sec

def main():

	time_start = timeit.default_timer()	

 	"""read output1"""
	df = pd.read_csv("output.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	curr_user = df.iloc[0,0]
	curr_session = df.iloc[0,1]
	freq = 0
	url_list = []
	users = {} 
	sessions = {}
	tier1 =0 
	tier2=0 
	tier3 =0
	url_book = 'https://secure.celebritycruises.com/booking/paymentConfirmation'
	url_held = 'https://secure.celebritycruises.com/booking/courtesyHoldConfirmation'
	visits = [[0 for i in range(5)] for j in range(3)]#lists of lists
	duration_list = [[0 for i in range(5)] for j in range(3)]
	day_diff = [[0 for i in range(4)] for j in range(3)]
	duration = 0
	diff = []

	"""Creating Data Structure"""
	for i in range(1, len(df)):
		if df.iloc[i, 0] == curr_user and df.iloc[i, 6] not in url_list:
			url_list.append(df.iloc[i, 6])

		else:		
			if url_book in url_list or url_held in url_list:
				users[curr_user] = Node(0, df.iloc[i-1,1]) 
			else:
				users[curr_user] = Node(len(set(url_list)), df.iloc[i-1,1])

			curr_user = df.iloc[i, 0]
			del url_list[:]
			url_list.append(df.iloc[i, 6])




	"""filling values"""
	for node in users.values():
		if node.tier >= 2:
			tier2 += 1
			visits[1][index] += 1
		elif node.tier is 0:
			tier3 += 1
			visits[2][index] += 1
		else:
			tier1 += 1
			visits[0][index] += 1

	#duration_list = [[duration_list[j][i]/visits[j][i] for i in range(5)] for j in range(3)] #average







	"""output"""

	print tier1, tier2, tier3

	print '\n'

	print visits

	#print '\n'

	#print duration_list

	#print '\n'

	#print day_diff

	time_stop = timeit.default_timer()

	print time_stop - time_start


			










if __name__=="__main__": main()
