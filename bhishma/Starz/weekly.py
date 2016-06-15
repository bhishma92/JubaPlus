import xlrd
import MySQLdb
import csv
import glob
import gzip

PATH = '/home/starzott/Projects'

def openWriteFiles(ls, t):
      copy = ls
      if t:
            l = [open(PATH + '/TestFiltered/' + copy[i].strip('/home/starzott/Projects/Testfile/').strip('.gz') , 'w') for i in range(len(ls))]
      else:
            l = [open(PATH + '/weekly/' + copy[i].strip('/home/starzott/Projects/StartzOTTweekly/').strip('.gz')  ,  'w') for i in range(len(ls))]

      return l

def testing(t):
      if t:
            l = glob.glob(PATH + "/Testfile/*.csv.gz") 
      else:
            l = glob.glob(PATH + "/StartzOTTweekly/*.csv.gz")

      return l


def filterFiles(files, outFiles):
	err = 0
	files.sort()
	for index, file  in enumerate(files, 0):
                  
                  if index < 0:
                        pass
                  else:
                        print file, index, err
                        with gzip.open(file) as ip:
                              ip = csv.reader(ip)
                              outFiles[index] = csv.writer(outFiles[index])
                              try:
                                      for line in ip:
                                              t = line
                                              
                                              outFiles[index].writerow([t[0], t[1], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11], t[12], t[13], t[14], t[18], t[20], t[24], t[33], t[34], t[35], t[36], t[37], t[38], t[39], t[40], t[41], t[42], t[43], t[44], t[45], t[46], t[47], t[48]])
                              except csv.Error:
                                      err += 1
                                      continue                       
                        

def main():

      global PATH

      test = False

      allFiles = testing(test)
      
      print allFiles
      filteredFiles = openWriteFiles(allFiles, test)
     
      filterFiles(allFiles, filteredFiles)


     
if __name__ == '__main__': main()
