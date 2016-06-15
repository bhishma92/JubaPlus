import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob


def main():


	path = '/home/account1/Projects/Exelate'

	allFiles = glob.glob(path + "/*.tsv")
	

	c = 0

	for file in allFiles:

		time_start = timeit.default_timer()	

		df = pd.read_csv(file, header=None, dtype = object, delimiter="\t", error_bad_lines = False)

		drop_list = []
		index = 1 
		count = 0
		val = True		

		for i in range(0, 7):
			if isinstance(df[i][0], basestring) == False:
				val = False

		if val == False:
			drop_list.append(0)
		else:
			temp = df.iloc[0, 6].strip(' GMT').split(':')
			if int(temp[2]) < 10:
				temp[2] = temp[2].zfill(2)
				df.iloc[0, 6] = ':'.join(temp) + ' GMT'	

		
		while index != len(df):
			if df[6][index] == df[6][index-1]:
				df.drop(index)
				index = index -1

			else:
				val = True
				for i in range(0, 7):
					if isinstance(df[i][index], basestring) == False:
						val = False

				if val == False:
					drop_list.append(index)
				else:
					count += 1
					temp = df.iloc[index, 6].strip(' GMT').split(':')
					if int(temp[2]) < 10:
						temp[2] = temp[2].zfill(2)
						df.iloc[index, 6] = ':'.join(temp) + ' GMT'	


			index += 1


		df.drop(df.index[drop_list], inplace=True)
		

		df.sort_index(by = [0, 5, 6], ascending = [True, True, True], inplace = True) # sort complete

		print len(df)

		df.to_csv('/home/account1/Projects/SortedOutput'+'Sorted' + str(c) + '.tsv', index = False, header = None, sep='\t')

		c += 1

		time_stop = timeit.default_timer()

		print time_stop - time_start


if __name__=="__main__": main()

