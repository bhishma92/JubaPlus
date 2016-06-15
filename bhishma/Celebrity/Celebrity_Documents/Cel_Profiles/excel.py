import xlrd
import csv

def csv_from_excel():

	wb = xlrd.open_workbook('/Users/bhishma/Documents/JubaPlus/Celebrity/data/header.xlsx')
	sh = wb.sheet_by_name('Sheet1')
	your_csv_file = open('header.csv', 'wb')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
	
	for rownum in xrange(sh.nrows):
		wr.writerow(sh.row_values(rownum))

	your_csv_file.close()


def main():

	csv_from_excel()


if __name__ == '__main__':
	main()
