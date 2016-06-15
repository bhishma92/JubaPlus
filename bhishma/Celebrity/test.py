import csv
import timeit
import glob
import gzip

def main():
	s = timeit.default_timer()
	count = 0
	path = '/home/account1/Projects/Exelate'
	allFiles = glob.glob(path + '/*.tsv.gz')
	c = 0
	for file in allFiles:
		print c
		with gzip.open(file, 'rb') as ip:
			ip = csv.reader(ip, dialect = 'excel-tab')
	
			

		c += 1
	print count
	e = timeit.default_timer()
	print e - s


if __name__ =="__main__": main()
