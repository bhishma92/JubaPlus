import pandas as pd
import collections
import operator

class Node(object):

	def __init__(self, d, t, i):
		self.date = d
		self.time = t
		self.id = i

def sessionTime(start, end):

	end = end.strip(' GMT').split(':')
	end = int(end[0])*3600 + int(end[1])*60 + int(end[2])

	sec = end - start
	#print start, end, sec
	hh = format(sec/3600, '02') if sec/3600 else format(0, '02')
	sec = sec - int(hh) * 3600
	mm = format(sec/60, '02') if sec/60 else format(0, '02')
	sec = sec - int(mm) * 60

	ss= format(sec, '02')

	x = [str(hh), str(mm), str(ss)]

	return ':'.join(x)


	


def main():

	df = pd.read_csv("example.txt", header=None, delimiter="\t", error_bad_lines = False)

	#print df

	for i in range(7, len(df.columns)):  #delete unnecessary columns 
		del df[i]

	#df.sort_index

	df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete
	df = df.reset_index()

	arr1 = []
	arr2 = []

	for i in range(len(df[0])):
		arr2.append('00:00:00')

	#print df
	curr_date = df[5][0]
	curr_time = df[6][0].strip(' GMT').split(':')
	time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
	ses_time = time
	ses_index = 0
	curr_index = 0

	arr1.append(1)
	arr2[0] = '00:00:00'
	
	for index, i in enumerate(df[0][1:len(df)], start=1):
		
		#print df[0][index], index
		if(df[0][index] == df[0][index-1]):
			temp = df[6][index].strip(' GMT').split(':')
			sum_var = int(temp[0])*3600 + int(temp[1])*60 + int(temp[2])

			if (df[5][index-1] == df[5][index]):
				if sum_var - time < 3600:
					arr1.append(arr1[index-1])
				else:
					arr1.append(arr1[index-1]+1)
					duration = sessionTime(ses_time, df[6][index-1])
					for i in range(ses_index, index):
						arr2[i] = duration

					ses_index = index
					ses_time = df[6][index].strip(' GMT').split(':')
					ses_time = int(ses_time[0])*3600 + int(ses_time[1])*60 + int(ses_time[2])
					curr_time = temp
					time = sum_var
					curr_session = arr1[index-1]+1
			else:
				arr1.append(arr1[index-1]+1)
				
				duration = sessionTime(ses_time, df[6][index-1])
				
				for i in range(ses_index, index):
					arr2[i] = duration

				ses_index = index
				ses_time = temp
				ses_time = sum_var

				curr_date = df[5][index]
				curr_time = temp
				time = sum_var
				curr_session = arr1[index-1]+1
		else:
			arr1.append(1)

			duration = sessionTime(ses_time, df[6][index-1])
				
			for i in range(ses_index, index):
				arr2[i] = duration

			curr_date = df[5][index]
			curr_time = df[6][index].strip(' GMT').split(':')
			time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
			ses_time = time
			ses_index = index
			curr_session = 1
			curr_index = index



	del df['index']
	df.insert(1, 'a', arr1)
	df.insert(2, 'b', arr2)


	df = df.reset_index(drop=True)
	df.columns = ['Exelate User ID', 'Session ID', 'Session Duration', 'City', 'State', 'Country', 'URL', 'Date', 'Time']

	print df.head(25)
	
	df.to_csv("output.tsv", index = False, sep='\t')



if __name__=="__main__": main()
