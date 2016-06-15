import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit

class Node(object):

	def __init__(self, d, t, i):
		self.date = d
		self.time = t
		self.id = i

def sessionTime(start, end): #Assumption on var is the session duration is never more than 24 hours

	#end = end.strip(' GMT').split(':')

	#if var:
	#	pass
	#else:
	#	end[0] = int(end[0]) + 24 #increase 24 hours 

	#end = int(end[0])*3600 + int(end[1])*60 + int(end[2])
	sec = end - start


	hh = format(sec/3600, '02') if sec/3600 else format(0, '02')
	sec = sec - int(hh) * 3600
	mm = format(sec/60, '02') if sec/60 else format(0, '02')
	sec = sec - int(mm) * 60
	ss= format(sec, '02')

	x = [str(hh), str(mm), str(ss)]

	return ':'.join(x)


#df.replace(r'\s+', np.nan, regex=True)
#dfmi.loc[:,('one','second')]

def main():

	time_start = timeit.default_timer()	
	a= ''
	for i in range(1048):
		a = a + str(i % 10)
 

	df = pd.read_csv("data.tsv", dtype = str, header=None, delimiter="\t", error_bad_lines = False)
	#df = df.replace(r'\s+', np.nan, regex=True)

	print df.head(2)

	#print df

	#df.to_csv("star1.tsv", index = False, sep='\t')

	print 'saved'


	#print df.head(10)
	"""
	for index in range(len(df)):
		temp = df.iloc[index, 6].strip(' GMT').split(':')
		if int(temp[2]) < 10:
			temp[2] = temp[2].zfill(2)
			df.iloc[index, 6]= ':'.join(temp) + ' GMT'
	"""

	#df.to_csv("data1.tsv", index = False, sep='\t')
	




	#print df

	#for i in range(7, len(df.columns)):  #delete unnecessary columns 
	#	del df[i]

	#df.sort_index

	df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete
	df = df.reset_index()

	arr1 = []
	arr2 = []

	for i in range(len(df[0])):
		arr2.append('00:00:00')


	#print df
	curr_date = df.iloc[0,6]
	curr_time = df.iloc[0,7].strip(' GMT').split(':')
	time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
	ses_time = time
	ses_index = 0
	curr_index = 0
	same_date = True

	arr1.append(1)
	arr2[0] = '00:00:00'

	
	for index in range(1, len(df)):
		
		temp1 = df.iloc[index-1, 7].strip(' GMT').split(':')
		sum_var1 = int(temp1[0])*3600 + int(temp1[1])*60 + int(temp1[2])
		#print df.iloc[index, 0], index
		if(df.iloc[index, 1] == df.iloc[index-1, 1]):
			temp = df.iloc[index, 7].strip(' GMT').split(':')
			sum_var = int(temp[0])*3600 + int(temp[1])*60 + int(temp[2])

			if (df.iloc[index-1, 6] == df.iloc[index, 6]):

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
					ses_time = df.iloc[index, 7].strip(' GMT').split(':')
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

					curr_date = df.iloc[index, 6]
					curr_time = temp
					time = sum_var
					curr_session = arr1[index-1]+1
		else:
			arr1.append(1)
			if same_date is False:
				ses_time -= 86400

			duration = sessionTime(ses_time, sum_var1)

			#if df.iloc[index, 0] == '0d4c9d5f1ba446c7b715d9f8e4bb2115':
			#	print ses_time, sum_var1, duration, df.iloc[index, 6]
				
			for i in range(ses_index, index):
				arr2[i] = duration

			curr_date = df.iloc[index, 6]
			curr_time = df.iloc[index, 7].strip(' GMT').split(':')
			time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
			ses_time = time
			ses_index = index
			curr_session = 1
			curr_index = index
			same_date = True



	del df['index']
	df.insert(1, 'a', arr1)
	df.insert(2, 'b', arr2)


	df = df.reset_index(drop=True)
	#df.columns = ['Exelate User ID', 'Session ID', 'Session Duration', 'City', 'State', 'Country', 'URL', 'Date', 'Time']

	#print df.head(25)
	
	df.to_csv("output.tsv", index = False, sep='\t')

	#time_stop = timeit.default_timer()

	time_stop = timeit.default_timer()

	print time_stop - time_start


if __name__=="__main__": main()
