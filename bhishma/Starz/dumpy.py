#!/usr/bin/python

import MySQLdb
import glob
import datetime
import csv
import sys
from warnings import filterwarnings

def getStartDate():
    s = raw_input("Enter Start Date in YYYY-mm-dd format")
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()
    
    

def getEndDate():
    e = raw_input("Enter End Date in YYYY-mm-dd format")
    return datetime.datetime.strptime(e, '%Y-%m-%d').date()

def day_difference(s, e):
    return (e-s).days



def getDates(allFiles, path):
    day_file = {}
    for f in allFiles:
        d  = f.strip(path)
        d = d[18:28]
        #f = datetime.datetime.strptime(f, '%Y-%m-%d').date()
        day_file[d] = f

    return day_file
        
    lst.sort()
    return lst

def check_dates(day_file, s, e, d, report):
    new_files = []
    missing_dates = []
    for i in range(d+1):
        if (str(s + datetime.timedelta(days=i))) not in day_file.keys():
            #print str(s + datetime.timedelta(days=i))
            missing_dates.append(str(s + datetime.timedelta(days=i)))
        else:
            k = str(s + datetime.timedelta(days=i))
            new_files.append(day_file[k])
                
    if not missing_dates:
        return new_files
    else:
        report.writerow(["missing dates", missing_dates])
        return new_files
    

def openWriteFile(s, e):
    op = open("/home/report_" + "s_" + "e.csv", 'w')
    return csv.writer(op)

def getValue(cursor):
    for item in cursor.fetchone():
        return item
    
def main():

    filterwarnings('ignore', category = MySQLdb.Warning)
    
    path = '/home/starzott/Projects/StarzOTTFiltered'
    allFiles = glob.glob(path + "/*.csv")
    allFiles.sort()
    #start_date = getStartDate()
    start_date = datetime.datetime.now().date() - datetime.timedelta(842)
    print start_date

    #end_date = getEndDate()
    end_date = datetime.datetime.now().date() - datetime.timedelta(3) #this is the date when report gets generated.
    print end_date

    d = day_difference(start_date, end_date)
 
    
    new_week= []

    report = openWriteFile(start_date, end_date)

    day_file = getDates(allFiles, path)
           
    new_files= check_dates(day_file, start_date, end_date, d, report)

    #print new_files        

    #sys.exit("exit taken")

    
    
    db = MySQLdb.connect('localhost','root', '2016juba','starz', connect_timeout=2000000000)

   

    #db = MySQLdb.connect(host = localhost, user = root, passwd = 2016juba, db = starz)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.

    #db.execute("SELECT DATE_FORMAT(snapdate,'%%%%Y-%%%%m-%%%%d') AS date, SUM( population ) AS accountpopulation, count( blockid ) AS number_block FROM %s WHERE blockid = %%s GROUP BY snapdate ORDER BY snapdate DESC LIMIT 7" % table, (blockid,))
    """
    cursor.execute(" create table ottNew(ErrorMsg TEXT, TransactionStart DATETIME DEFAULT NULL, TransactionEnd  DATETIME DEFAULT NULL, AccountID  TEXT, ClientID  TEXT, SessionID  BIGINT, DeviceID  TEXT, Affiliate  TEXT, Service  TEXT, ISP  TEXT, ASN  INT, Country  TEXT, State  TEXT, City TEXT, OS  TEXT, DeviceType  TEXT, DeviceModel  TEXT, ConnectionType TEXT, AssetName  TEXT, Title  TEXT, seriesName  TEXT, episodeName  TEXT, season  SMALLINT(3), ContentID  INT(8), ContentType  TEXT, Rating TEXT, AccessType  TEXT,CompleteView25Pct  BOOL, CompleteView50Pct  BOOL, CompleteView75Pct  BOOL, CompleteView90Pct  BOOL, Minute0To2  BOOL, Minute2To5  BOOL, Minute5To10  BOOL, Minute10To20  BOOL, Minute20To40  BOOL, Minute40To60  BOOL, Minute60To90  BOOL, Minute90To120  BOOL, Minute120To150  BOOL, Minute150To180  BOOL, MinuteGT180  BOOL, TotalPlayTimeSec  FLOAT(9,3))" )

    cursor.execute('SET GLOBAL connect_timeout=288000')
    cursor.execute('SET GLOBAL wait_timeout=288000')
    cursor.execute('SET GLOBAL interactive_timeout=288000')
    cursor.execute('SET GLOBAL max_allowed_packet=1073741824')
    
    
    
    for file in new_files:
        print file
        cursor.execute("USE starz")
        cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' identified by '2016juba' WITH GRANT OPTION;")
        
        cursor.execute("load data local infile %s into table ottNew fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (@var1, @var2, @var3, AccountID, ClientID, SessionID, DeviceID, Affiliate, Service, ISP, ASN, Country,  State, City, OS, DeviceType, DeviceModel, ConnectionType, AssetName, Title, seriesName, episodeName, season, ContentID, ContentType, Rating, AccessType, CompleteView25Pct, CompleteView50Pct, CompleteView75Pct, CompleteView90Pct, Minute0To2, Minute2To5, Minute5To10, Minute10To20, Minute20To40, Minute40To60, Minute60To90, Minute90To120, Minute120To150, Minute150To180, MinuteGT180, TotalPlayTimeSec) SET ErrorMsg = @var1, TransactionStart = STR_TO_DATE(@var2,'%%Y-%%m-%%d %%H:%%i:%%s'), TransactionEnd = STR_TO_DATE(@var3,'%%Y-%%m-%%d %%H:%%i:%%s')", [file])
    """
    #cursor.execute("CREATE INDEX a1 ON ott ( AccountID, ErrorMsg, ClientID, SessionID )")
    
    cursor.execute("select distinct count( AccountID) from ott where ErrorMsg = '' and AccountID != '' ")
    report.writerow(["Distinct AccountIDs", getValue(cursor)])


    
    cursor.execute("select distinct count( ClientID) from ott where ErrorMsg = '' and ClientID != '' and AccountID != '' ")
    report.writerow(["Distinct ClientIDs", getValue(cursor)])
        

    
    
    #for item in cursor.fetchone():
        
        
    #report.writerow(["Distinct ClientIDs", res])
    
    #Sessions = cursor.execute("select distinct count( SessionID) from ott where ErrorMsg = '' and AccountID != '' ")
    """
    Devices = cursor.execute("select distinct count( DeviceID) from ott where ErrorMsg = '' and AccountID != '' ")
    Services = cursor.execute("select distinct count( Service) from ott where ErrorMsg = '' and AccountID != '' ")
    ISP = cursor.execute("select distinct count( ISP) from ott where ErrorMsg = '' and AccountID != '' and ISP != 'UNKNOWN' ")
    ASN = cursor.execute("select distinct count( ASN) from ott where ErrorMsg = '' and AccountID != '' and ASN != 0 ")
    Countries = cursor.execute("select distinct count( Country) from ott where ErrorMsg = '' and AccountID != '' and Country != '' ")
    States = cursor.execute("select distinct count( State) from ott where ErrorMsg = '' and AccountID != '' and State != '' ")
    Cities = cursor.execute("select distinct count( City) from ott where ErrorMsg = '' and AccountID != '' and City != '' ")
    OS = cursor.execute("select distinct count( OS) from ott where ErrorMsg = '' and AccountID != '' and OS != '' ")
    DeviceType = cursor.execute("select distinct count( DeviceType) from ott where ErrorMsg = '' and AccountID != '' and DeviceType != '' ")
    DeviceModel = cursor.execute("select distinct count( DeviceModel) from ott where ErrorMsg = '' and AccountID != '' and DeviceModel != '' ")
    ConnectionType = cursor.execute("select distinct count( ConnectionType) from ott where ErrorMsg = '' and AccountID != '' and ConnectionType != '' ")
    AssetName = cursor.execute("select distinct count( AssetName) from ott where ErrorMsg = '' and AccountID != '' and AssetName != '' ")
    Title = cursor.execute("select distinct count( Title) from ott where ErrorMsg = '' and AccountID != '' and Title != '' ")
    seriesName = cursor.execute("select distinct count( seriesName) from ott where ErrorMsg = '' and AccountID != '' and seriesName != '' ")
    episodename = cursor.execute("select distinct count( episodeName) from ott where ErrorMsg = '' and AccountID != '' and episodeName != '' ")
    contentID = cursor.execute("select distinct count( contentID) from ott where ErrorMsg = '' and AccountID != '' and contentID != '' ")
    contentType = cursor.execute("select distinct count( contentType) from ott where ErrorMsg = '' and AccountID != '' and contentType != '' ")
    Rating = cursor.execute("select distinct count( Rating) from ott where ErrorMsg = '' and AccountID != '' and Rating != '' ")
    
    """
    
    
    
    
    

    #report.writerow(["Distinct AccountIDs", cursor.fetchone()])
    #report.writerow(["Distinct ClientIDs", cursor.fetchone()])
    #report.writerow(["Distinct SessionIDs", Sessions])
    #report.writerow(["Distinct DeviceIDs", Devices])
    #report.writerow(["Distinct Services", Services])
    #report.writerow(["Distinct ISPs", ISP])
    #report.writerow(["Distinct ASNs", ASN])
    

    
    
    

    cursor.close()
    # disconnect from server
    db.close()
   
    
if __name__=="__main__": main()
