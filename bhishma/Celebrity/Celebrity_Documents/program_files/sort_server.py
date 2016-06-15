import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob


def main():


	path = '/Users/bhishma/Documents/JubaPlus/Celebrity/buffer'  #'/home/account1/Projects/Exelate'

	allFiles = glob.glob(path + "/*.tsv")
	
	
	c = 0

	df = pd.DataFrame()
	#df = pd.DataFrame({"ID": range(0)}, {"URL": range(0)}, {"Date": range(0)}, {"Time": range(0)} )

	for file in allFiles:
		
		print file
       
		time_start = timeit.default_timer()	

		df1 = pd.read_csv(file, header=None, dtype = object, delimiter="\t", error_bad_lines = False)
		df1 = df1.drop_duplicates(subset=[0, 6], keep=False)
		df1 = df1.drop(df1.columns[[ 1, 2, 3]], axis=1)
		df1.columns = [0,1,2,3]

		index = 0 
		count = 0
		drop_list = []
	
		while index != len(df.index):
			val = True
			for i in range(0, 4):
				if isinstance(df[i][index], basestring) == False:
					val = False

			if val == False:
				drop_list.append(index)
			else: 
				temp = df.iloc[index, 6].strip(' GMT').split(':')
				if int(temp[2]) < 10:
					temp[2] = temp[2].zfill(2)
					df.iloc[index, 6] = ':'.join(temp) + ' GMT'	


			index += 1
		print drop_list

		df.drop(df.index[drop_list], inplace=True)
		
		df1.sort_index(by = [0, 2, 3], ascending = [True, True, True], inplace = True)
		#df1.to_csv('/home/dummy/hhmmss'+str(c)+ '.tsv', index = False, header = False, sep='\t')
		
		df = df.append(df1)
		
 		c += 1
		
                time_stop = timeit.default_timer()

                print time_stop - time_start

		
		"""

		"""
	#print df.head(20)
	df.sort_index(by = [0, 2, 3], ascending = [True, True, True], inplace = True) # sort complete
	print df.head()
	print '\n'
	print len(df)
	#df.to_csv('/home/dummy/file'+ '.tsv', index = False, header = None, sep='\t')

if __name__=="__main__": main()

