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
 
 	
	df = pd.read_csv(PATH + "/data/SesOutFinalUS.tsv", dtype = object, header=None, delimiter="\t", error_bad_lines = False)

	df = df.head(200)

	#df.to_csv(PATH + "/data/visitsSample200.tsv", index = False, header= False, sep='\t')

	#df1 = df.head(200)

	#df1.to_csv(PATH + "/outputs/sampleOut1.tsv", index = False, header= None, sep='\t')

	print 'file read'
	#['U','SES', 'DUR', 'SC','C','URL','D','T']
	df.columns = [0,1,2,8,9,3,4,5]

	
	
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
				

				elif int(df[1][i-1]) == 1 and len(set(url_list)) >= 2:
					tiers = 1 #index for tier2
				else:
					tiers = 2 #index for tier3

				users[curr_user] = Node(tiers, df[1][i-1])

			session_f[tiers] += int(df[1][i-1]) 

			curr_user = df[0][i]
			
			del url_list[:]
			url_list.append(df[3][i])
	
	count += 1
	if url_book in url_list or url_held in url_list:
		users[curr_user] = Node(3, df[1][len(df.index)-1]) #2 is index of tier4
		tiers = 3
	else:
		if int(df[1][len(df.index)-1]) == 1 and len(set(url_list)) in [0,1]:
			tiers = 0
			

		elif int(df[1][len(df.index)-1]) == 1 and len(set(url_list)) >= 2:
			tiers = 1 #index for tier2
		else:
			tiers = 2 #index for tier3

		users[curr_user] = Node(tiers, df[1][len(df.index)-1])

	session_f[tiers] += int(df[1][len(df.index)-1])
	
	print 'Total number of Users are ' + str(count)

	print len(users)


	time_stop = timeit.default_timer()

	print time_stop - time_start

	
	op = open(PATH + '/outputs/IDTierSessionsUSafterQC.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

  	for key, value in users.items():
   		op.writerow([key, value.tier, value.sessions])

   	

   	print "it's over"
   	
   	"""

	with open(PATH + '/outputs/IDTierSessionsUS1.tsv', 'rb') as fp:
		fp = csv.reader(fp, dialect = 'excel-tab')
		for line in fp:
			t = line
			s = str(t[0])
			if s in df[0]:
				users[s] = Node(t[1],t[2])
	
	

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
			
				l1 = map(int, df.iloc[index, 6].split('-'))
				l2 = map(int, df.iloc[index-1, 6].split('-'))


				d1 = date(l1[0], l1[1], l1[2])
				d2 = date(l2[0], l2[1], l2[2])
	
				d = (d1 - d2).days

				if sec < 0:
					d = d - 1

				day_diff[users[curr_user].tier][temp] += d
			
			duration_list[users[curr_user].tier][temp] += get_sec(df[2][index-1])
			last_session = curr_session
			last_index = index
			curr_session = df[1][index]
			temp = getTemp(int(curr_session))

		else:
			pass

		#last_session = df[1][index]

	#print last_session

	if last_session != curr_session:
		if temp != 4:
			sec = get_sec(df[5][last_index +1].strip(' GMT')) - get_sec(df[5][last_index].strip(' GMT'))

			l1 = map(int, df.iloc[last_index + 1, 6].split('-'))
			l2 = map(int, df.iloc[last_index, 6].split('-'))


			d1 = date(l1[0], l1[1], l1[2])
			d2 = date(l2[0], l2[1], l2[2])
	
			d = (d1 - d2).days

			if sec < 0:
				d = d - 1

			day_diff[users[curr_user].tier][temp] += d

		duration_list[users[curr_user].tier][temp] += get_sec(df[2][last_index+1])
	
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
			if div_dur[i][j+1] == 0:
				day_diff[i][j] = 0
			else:
				if j == 3 and foTofi[i] != 0:
					temp = foTofi[i]
				else:
					temp = div_dur[i][j+1] 

				day_diff[i][j] = day_diff[i][j]/temp


	op = open(PATH + '/outputs/Outpu1afterQC.tsv', 'w')
	op = csv.writer(op, dialect = 'excel-tab')

	op.writerow(['', '', '', '#visits(sessions)', '', '', '','', 'Duration over that vists',  '', '', '','', 'day difference', '', '', '', 'Session Frequency', 'Frequency Ratio'])

	op.writerow(['value visitors',	'Total #unique IDs',	'',	'1 session','2  sessions',	'3  sessions',	'4  sessions',	'5 sessions+',	'1 session'	,'2  sessions',	'3  sessions',	'4  sessions',	'5 sessions+',	'1~2',	'2~3', 	'3~4',	'4~5',	'', ''])

	op.writerow(['tier1:bouncer (1 session/one page only)', tier1, '', div_dur[0][0], div_dur[0][1], div_dur[0][2], div_dur[0][3], div_dur[0][3], duration_list[0][0], duration_list[0][1], duration_list[0][2], duration_list[0][3], duration_list[0][4], day_diff[0][0], day_diff[0][1], day_diff[0][2], day_diff[0][3], session_f[0]])

	op.writerow(['tier2: 1x Session/ 2+ pages', tier2, '', div_dur[1][0], div_dur[1][1], div_dur[1][2], div_dur[1][3],div_dur[1][4], duration_list[1][0], duration_list[1][1], duration_list[1][2], duration_list[1][3], duration_list[1][4], day_diff[1][0], day_diff[1][1], day_diff[1][2], day_diff[1][3], session_f[1]])

	op.writerow(['tier3: High value visitors (2+ sessions/2+ pages)', tier3, '', div_dur[2][0], div_dur[2][1], div_dur[2][2], div_dur[2][3], div_dur[2][4], duration_list[2][0], duration_list[2][1], duration_list[2][2], duration_list[2][3], duration_list[2][4],day_diff[2][0], day_diff[2][1], day_diff[2][2], day_diff[2][3], session_f[2]])

	op.writerow(['tier4: converters (book or held online)', tier4, '', div_dur[3][0], div_dur[3][1], div_dur[3][2], div_dur[3][3], div_dur[3][4],duration_list[3][0], duration_list[3][1], duration_list[3][2], duration_list[3][3], duration_list[3][4], day_diff[3][0], day_diff[3][1], day_diff[3][2], day_diff[3][3], session_f[3]])

	op.writerow(['User count', count])
	
	
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
