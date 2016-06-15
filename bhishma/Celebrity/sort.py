import pandas as pd
import numpy as np
import collections
import operator
import sys
import timeit
import gzip
import glob


def main():
	

	path = '/home/account1/Projects/Exelate/Output'
	#path = '/home/dummy/try'
	allFiles = glob.glob(path + "/*.tsv")
	#allFiles = [path + '/outputF38.tsv']
	
	list1 = ['2015-10-28', '2015-10-29', '2015-10-30', '2015-10-31', '2015-11-01', '2015-11-02', '2015-11-04', '2015-11-05', '2015-11-06', '2015-11-09', '2015-11-11', '2015-11-12', '2015-11-13', '2015-11-14', '2015-11-15', '2015-11-16']
	drop_dates = []
	c = 1
	dc = 0
	df = pd.DataFrame()
	#df.columns = ['A','B','C','D','E','F','G']
	
	for file in allFiles:
		
		print c	
		
		time_start = timeit.default_timer()	
		
		df1 = pd.read_csv(file, header=None, dtype = object, delimiter="\t", error_bad_lines = False)
		v1 = len(df1.index) 
		df1 = df1.dropna()
		dc += v1 - len(df1.index) 
		print len(df1.index), dc

		
		df1.columns = ['A','B','C','D','E','F','G']
			
		
		index = 0 
		count = 0
		drop_list = []

		for row in df1.itertuples():
			try:
			
				df1.set_value(row[0], 'C', row[3] + '_' + row[2])
	
				if len(row[7]) == 11:
				
					df1.set_value(row[0],'G', row[7][:6] + '0' + row[7][6:])
				
					
			except ValueError:
				print 'Value Error!', c
				pass

		#df1.drop('B', axis = 1, inplace = True)
	
		
		df1.to_csv('/home/dummy/try/unsortedSS'+str(c)+ '.tsv', index = False, header = None, sep='\t')
	
		df = df.append(df1)
		df1 = None	
 		c += 1
		
                time_stop = timeit.default_timer()

                print time_stop - time_start

	df.columns = ['A','B','C','D','E','F','G']
	df.drop('B', axis = 1, inplace = True)
	print 'done'
	print len(df.index)
	v1 = len(df.index)
	df = df.drop_duplicates(subset = ['A','F','G'], keep = 'first')
	dc += v1 - len(df.index)
	print len(df.index), dc


        #for row in df.itertuples():
	#	if row[6] in list1:
         #               drop_dates.append(int(row[0]))
	
	#df.drop(df.index[drop_dates], inplace = True)
	#print len(df.index)

	df['F'] = pd.to_datetime(df['F'])

        for row in df.itertuples():
                if row[6] in list1:
                        drop_dates.append(int(row[0]))

        df.drop(df.index[drop_dates], inplace = True)
        print len(df.index)
	
	df.sort_values(by = ['A', 'F', 'G'], ascending = [True, True, True], inplace = True) # sort complete
	print 'sort done'

	print df.head(10)
	print df.tail(10)
	df.to_csv('/home/dummy/try/fileNew'+ '.tsv', index = False, header = None, sep='\t')
	
if __name__=="__main__": main()

