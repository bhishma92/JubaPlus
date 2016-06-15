import pandas as pd
import collections
import operator
import sys
import timeit
import glob

class Node(object):

	def __init__(self, d, t, i):
		self.date = d
		self.time = t
		self.id = i

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

	time_start = timeit.default_timer()	

	path = '/home/account1/Projects/SortedOutput'

	allFiles = glob.glob(path + "/*.tsv")
 
	df = pd.read_csv("hhmmss0.tsv", header=None, delimiter="\t", error_bad_lines = False)

	print len(df)

	arr1 = []
	arr2 = []

	for i in range(len(df[0])):
		arr2.append('00:00:00')

	curr_date = df[2][0]
	curr_time = df[3][0].strip(' GMT').split(':')
	time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
	ses_time = time
	ses_index = 0
	curr_index = 0
	same_date = True

	arr1.append(1)
	arr2[0] = '00:00:00'


	for index, i in enumerate(df[0][1:len(df.index)], start=1):

			temp1 = df[3][index-1].strip(' GMT').split(':')
			sum_var1 = int(temp1[0])*3600 + int(temp1[1])*60 + int(temp1[2])
			
			temp = df[3][index].strip(' GMT').split(':')
			sum_var = int(temp[0])*3600 + int(temp[1])*60 + int(temp[2])

			if(df[0][index] == df[0][index-1]):

				if (df[2][index-1] == df[2][index]):

					if sum_var - sum_var1 < 3600:
						arr1.append(arr1[index-1])
					else:
						arr1.append(arr1[index-1]+1)
						if ses_day == df[2][index-1]:
							duration = sessionTime(ses_time, sum_var1)
						else:
							a = df[2][index-1].split('-')
							b = df[2][ses_index].split('-')
							
							d1 = datetime.datetime(a[2],a[0],a[1])
    						d2 = datetime.datetime(b[2],b[0],b[1])
							d = (d1 - d2).days
							s_var = sum_var1 + (d*86400)
							duration = sessionTime(ses_time, s_var)


						for i in range(ses_index, index):
							arr2[i] = duration

						ses_day = df[2][index]
						ses_index = index
						ses_time = sum_var
						curr_time = temp
						time = sum_var
						curr_session = arr1[index-1]+1
				else:

					d1 = map(int, df.iloc[index, 2].split('-'))
					d2 = map(int, df.iloc[index-1, 2].split('-'))
					t1 = map(int, df.iloc[index, 3].strip(' GMT').split(':'))
					t2 = map(int, df.iloc[index-1, 3].strip(' GMT').split(':'))

					a = datetime.datetime(d1[2],d1[0],d1[1],t1[0],t1[1],t1[2])
					b = datetime.datetime(d2[2],d2[0],d2[1],t2[0],t2[1],t2[2])

					secs = int((a-b).total_seconds())

					if secs < 3600:
						arr1.append(arr1[index-1])
					else:	
						arr1.append(arr1[index-1]+1)	
						duration = sessionTime(0, secs)
						for i in range(ses_index, index):
							arr2[i] = duration

						ses_index = index
						ses_time = sum_var
						ses_day = df[2][index]
						curr_date = df[2][index]
						curr_time = temp
						time = sum_var
						curr_session = arr1[index-1]+1
			else:
				arr1.append(1)

				a = df[2][index-1].split('-')
				b = df[2][ses_index].split('-')
							
				d1 = datetime.datetime(a[2],a[0],a[1])
    			d2 = datetime.datetime(b[2],b[0],b[1])
							
				d = (d1 - d2).days
				s_var = sum_var1 + (d*86400)

				duration = sessionTime(ses_time, s_var)

				for i in range(ses_index, index):
					arr2[i] = duration

				curr_date = df[2][index]
				curr_time = df[3][index].strip(' GMT').split(':')
				time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
				ses_time = time
				ses_day = df[2][index]
				ses_index = index
				curr_session = 1
				curr_index = indexs


	df.insert(1, 'a', arr1)
	df.insert(2, 'b', arr2)

	#df.columns = ['Exelate User ID', 'Session ID', 'Session Duration', 'City', 'State', 'Country', 'URL', 'Date', 'Time']



	print len(df)
		
	df.to_csv("output.tsv", index = False, header= False, sep='\t')


	time_stop = timeit.default_timer()

	print time_stop - time_start




if __name__=="__main__": main()
