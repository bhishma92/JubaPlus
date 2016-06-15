import glob
from datetime import datetime

def main():
    lst = []
    path = '/home/starzott/Projects/StartzOTT/'
    allFiles = glob.glob(path + "/*.csv.gz")
    for file in allFiles:
        file = file.strip(path)
        file = file[18:28]
        if file not in lst:
            #date_object = datetime.strptime(file, '%Y-%M-%d').date()
            lst.append(file)
        else:
            print 'report error'
   
    lst = sorted(lst)
    for i in range(len(lst)):
        print lst[i]
    print lst[0], lst[len(lst)-1], len(lst)
if __name__ == '__main__': main()
