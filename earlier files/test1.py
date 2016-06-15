import pandas as pd
import collections
import operator

class Node(object):

	def __init__(self, d, t, i):
		self.date = d
		self.time = t
		self.id = i

def main():

	df = pd.read_csv("example.txt", header=None, delimiter="\t")


	#print df

	for i in range(7, len(df.columns)):  #delete unnecessary columns 
		del df[i]

	#df.sort_index

	df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete

	arr1 = []
	arr2 = []

	arr1.append(1)
	arr2.append(0)
	"""
	sf = DataFrame(df[0], 21, 0)

	print sf

	for index, i in enumerate(df[0], start=0):

		if index is not 0:

			print df[0][index], index

			if(df[0][index] == df[0][index-1]):
				
				if (curr_date == df[5][index]):
					temp = df[6][index].strip(' GMT').split(':')
					sum_var = int(temp[0])*3600 + int(temp[1])*60 + int(temp[2])

					if sum_var - time < 3600:
						arr1.append(arr1[index-1])
					else:
						arr1.append(arr1[index-1]+1)
						curr_time = temp
						time = sum_var
						curr_session = arr1[index-1]+1
				else:
					arr1.append(arr1[index-1]+1)
					curr_date = df[5][index]
					curr_time = df[6][index].strip(' GMT').split(':')
					time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
					curr_session = arr1[index-1]+1
			else:
				arr1.append(1)
				curr_date = df[5][index].split('/')
				curr_time = df[6][index].strip(' GMT').split(':')
				time = int(curr_time[0])*3600 + int(curr_time[1])*60 + int(curr_time[2])
				curr_session = 1




	df.insert(1, 'Session ID', arr1)
	#df.insert(2, 'Session Duration', arr2)

	#print df
	"""


	#tsvin.to_csv('output2.tsv')
	#print df[5][0]
	entry_list = {}
	session = {}

	for index, i in enumerate(df[0], start=0):

		val = int(index)

 		temp = str(df[5][index])
 		temp = temp.split('/')
 		temp1 = str(df[6][index])
 		temp1 = temp1.strip(' GMT')
 		temp1 = temp1.split(':')

 		dt = temp + temp1 # date and time for 01/03/1992 3:45:34 -> 01, 03, 1992, 3, 45, 54

		if i in entry_list.keys():
			entry_list[i][index] = tuple(dt)
		else:
 			entry_list[i] = {index : tuple(dt)}
 
 	for index, i in enumerate(entry_list.keys(), start=0):

 		temp = entry_list[i]
 		entry_list[i] = collections.OrderedDict(sorted(temp.items(), key=lambda t: t[1])) #sort by value
 		print entry_list[i]
 		#s

 		#for entry in entry_list[i]:
 	"""
 	for index, value in enumerate(entry_list.values(), start=0):

 		for ind, val in enumerate(value.values(), start=0):
 	"""



 

 


 		

			











if __name__=="__main__": main()
