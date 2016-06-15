import csv
import glob
import gzip

PATH = '/home/starzott/Projects'
def main():
	c = 0
	global PATH
	allFiles = glob.glob(PATH + "/StarzOTTFiltered/*.csv")
	for file in allFiles:
		with open(file) as ip:
			ip = csv.reader(ip)
			for line in ip:
				c += 1
			c = c-1
			print c	
	print c

if __name__ == '__main__': main()
