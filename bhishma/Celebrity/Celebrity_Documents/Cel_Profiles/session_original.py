import pandas as pd
import collections
import operator
import sys
import timeit
import glob

class Node(object):

	def __init__(self, i):
		self.id = i
		self.days = []
		self.times = []
		self.sessions = []

	def addDayTime(self, d, t):


def sessionTime(start, end): #Assumption on var is the session duration is never more than 24 hours

	sec = end - start
	hh = format(sec/3600, '02') if sec/3600 else format(0, '02')
	sec = sec - int(hh) * 3600
	mm = format(sec/60, '02') if sec/60 else format(0, '02')
	sec = sec - int(mm) * 60
	ss= format(sec, '02')

	x = [str(hh), str(mm), str(ss)]

	return ':'.join(x)

def main():


	path = '/Users/bhishma/Documents/JubaPlus/Celebrity/compress' #'/home/account1/Projects/SortedOutput'

	allFiles = glob.glob(path + "/*.tsv")

	#files = [open('/home/account1/Projects/SessionOutput/outputS%i.tsv' %i, 'w') for i in range(95)]
	#files = [open('/Users/bhishma/Documents/JubaPlus/Celebrity/outputS%i.tsv' %i, 'w') for i in range(3)]
	files = open('/Users/bhishma/Documents/JubaPlus/Celebrity/sessionOutF.tsv', 'w')


	c = 0
	var = 0
	arr1 = []
	arr2 = []
	users = dict()

	for file in allFiles:

		print file

		time_start = timeit.default_timer()	

		df = pd.read_csv(file, header=None, delimiter="\t", error_bad_lines = False)

		for i in range(df.shape[0]):

			if df[0][i] in users.key():
				users[df[0][i]].addDayTime(df[5][i], df[6][i])
			else:
				users[df[0][i]] = Node(var+i)


		var += df.shape[0]



		for i in range(df.shape[0]):

			if df[0][i] in users.key():
				users[df[0][i]].addDayTime(df[5][i], df[6][i])
			else:
				users[df[0][i]] = Node(var+i)


		var += df.shape[0]




		"""

		for i in range(len(df[0])):
			arr2.append('00:00:00')

		curr_date = df[5][0]
		curr_time = df[6][0].strip(' GMT').split(':')
		time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
		ses_time = time
		ses_index = 0
		curr_index = 0
		same_date = True

		arr1.append(1)
		
		for index, i in enumerate(df[0][1:len(df)], start=1):
				temp1 = df[6][index-1].strip(' GMT').split(':')
				sum_var1 = int(temp1[0])*3600 + int(temp1[1])*60 + int(temp1[2])
		
				if(df[0][index] == df[0][index-1]):
					temp = df[6][index].strip(' GMT').split(':')
					sum_var = int(temp[0])*3600 + int(temp[1])*60 + int(temp[2])

					if (df[5][index-1] == df[5][index]):

						if not same_date:
							sum_var1 += 86400
						if sum_var - sum_var1 < 3600:
							arr1.append(arr1[index-1])
						else:
							arr1.append(arr1[index-1]+1)
							duration = sessionTime(ses_time, sum_var1) #True states they entries are the same date
							for i in range(ses_index, index):
								arr2[i] = duration

							ses_index = index
							ses_time = df[6][index].strip(' GMT').split(':')
							ses_time = int(ses_time[0])*3600 + int(ses_time[1])*60 + int(ses_time[2])
							curr_time = temp
							time = sum_var
							curr_session = arr1[index-1]+1
					else:
						same_date = False
						sum_var += 86400
						if sum_var - sum_var1 < 3600:
							arr1.append(arr1[index-1])
						else:	
							arr1.append(arr1[index-1]+1)	
							duration = sessionTime(ses_time, sum_var1)
							for i in range(ses_index, index):
								arr2[i] = duration

							ses_index = index
							#ses_time = temp
							ses_time = sum_var

							curr_date = df[5][index]
							curr_time = temp
							time = sum_var
							curr_session = arr1[index-1]+1
				else:
					arr1.append(1)
					if same_date is False:
						ses_time -= 86400

					duration = sessionTime(ses_time, sum_var1)

					for i in range(ses_index, index):
						arr2[i] = duration

					curr_date = df[5][index]
					curr_time = df[6][index].strip(' GMT').split(':')
					time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
					ses_time = time
					ses_index = index
					curr_session = 1
					curr_index = index
					same_date = True


		df.insert(1, 'a', arr1)
		df.insert(2, 'b', arr2)

		#df.columns = ['Exelate User ID', 'Session ID', 'Session Duration', 'City', 'State', 'Country', 'URL', 'Date', 'Time']

		print len(df)
			
		df.to_csv('sessionOut' + str(c) + '.tsv', index = False, header = None, sep='\t')
		"""
		time_stop = timeit.default_timer()

		print time_stop - time_start




if __name__=="__main__": main()
