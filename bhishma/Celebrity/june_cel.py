import pandas as pd
import collections
import operator
import sys
import timeit
import datetime
from datetime import date
import csv
from array import array


PATH = '/home/dummy/try'


	

def main():

	time_start = timeit.default_timer()	

	global PATH
 
 	
	df = pd.read_csv(PATH + '/SesOutFinalUS.tsv', dtype = object, header=None, delimiter="\t", error_bad_lines = False)
    
	df = df.head(10000)
	
	df.columns = ['U','SES', 'DUR', 'SC','C','URL','D','T']

        print df.head(10)
        
	ip = pd.read_csv(PATH + "/name.csv", dtype = object, header=None, error_bad_lines = False)
	ip.columns = ['user', 'tier']

        print ip.head(10)
        
	usrs = ip['user'].tolist()
	trs = ip['tier'].tolist()

	dic = dict(zip(usrs, trs)) 

	with open(PATH + '/jun_cel_output.csv', 'wb') as op:
	    op = csv.writer(op)


            print 'file read'

            
            for row in df.itertuples():
                    prev_row = row
                    curr_user = row[1]
                    break


            for row in df.itertuples():
                    try:
                            g = 1/int(row[0])

                            try:
                                    if row[1] != curr_user:
                                            if curr_user in dic.keys():
                                                    op.writerow([curr_user, dic[curr_user], prev_row[2]])


                                            curr_user = row[1]

                                    prev_row = row			

                            except KeyError:
                                    print 'error!'   

                    except ZeroDivisionError as e:
                            print 'exception raised'
                            pass






    	time_stop = timeit.default_timer()

	print time_stop - time_start





if __name__=="__main__": main()

