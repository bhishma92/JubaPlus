import xlrd
import MySQLdb
import csv

#PATH = '/users/bhishma/Documents/JubaPlus/Celebrity'


def main():


      # Establish a MySQL connection
      database = MySQLdb.connect (host="64.237.51.251", user = "root", passwd = "2016juba", db = "mysqlPython")

      # Get the cursor, which is used to traverse the database, line by line
      cursor = database.cursor()

      # Create the INSERT INTO sql query
      #query = """INSERT INTO orders (product, customer_type, rep, date, actual, expected, open_opportunities, closed_opportunities, city, state, zip, population, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
      query = """INSERT INTO orders (TransactionStart, TransactionEnd, AccountID, ClientID, SessionID, DeviceID, Affiliate, Service , ISP, ASN, Country,State, City, DeviceType , DeviceModel ,connectionType , AssetName , Title, seriesName , episodeName, season , ContentID,   ContentType, Rating, AccessType , CompleteView25Pct, CompleteView50Pct, CompleteView75Pct, CompleteView90Pct, Minute0To2 , Minute2To5 , Minute5To10 ,Minute10To20 ,Minute20To40  ,Minute40To60, Minute60To90, Minute90To120 , Minute120To150, Minute150To180, MinuteGT180 ,TotalPlayTimeSec) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

      # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers

      # Open the workbook and define the worksheet
      with open('/home/example.csv') as ip:
            ip = csv.reader(ip)
            #TransactionStart TransactionEnd    AccountID   ClientID    SessionID   DeviceID    Affiliate   Service     ISP   ASN   Country     State City
            


            for line, index in enumerate(ip, 3):

                  TransactionStart = line[1]
                  TransactionEnd = line[2]
                  AccountID = line[3]
                  ClientID = line[4]
                  SessionID = line[5]
                  DeviceID = line[6]
                  Affiliate = line[7]
                  Service = line[8]
                  ISP = line[9]
                  ASN = line[10]
                  Country = line[11]
                  State = line[12]
                  City = line[13]
                  OS = line[15]

                  #DeviceType  DeviceModel connectionType 

                  DeviceType = line[17]
                  DeviceModel = line[18]
                  connectionType = line[19]
                  #AssetName  Title seriesName  episodeName season      ContentID   ContentType Rating      AccessType  CompleteView25Pct CompleteView50Pct CompleteView75Pct CompleteView90Pct Minute0To2  Minute2To5  Minute5To10 Minute10To20      Minute20To40      Minute40To60      Minute60To90      Minute90To120     Minute120To150    Minute150To180    MinuteGT180 


                  AssetName = line[23]
                  Title = line[24]
                  seriesName = line[25]
                  episodeName = line[26]
                  season = line[27]
                  ContentID = line[28]
                  ContentType = line[29]
                  Rating = line[30]
                  AccessType = line[31]
                  CompleteView25Pct = line[32]
                  CompleteView50Pct = line[33]
                  CompleteView75Pct = line[34]
                  CompleteView90Pct = line[35]
                  Minute0To2 = line[36]
                  Minute2To5 = line[37]
                  Minute5To10 = line[38]
                  Minute10To20 = line[39]
                  Minute20To40 = line[40]
                  Minute40To60 = line[41]
                  Minute60To90 = line[42]
                  Minute90To120 = line[43]
                  Minute120To150 = line[44]
                  Minute150To180 = line[45]
                  MinuteGT180 = line[46]
                  TotalPlayTimeSec = line[50]


            # Assign values from each row
            values = (TransactionStart, TransactionEnd, AccountID, ClientID, SessionID, DeviceID, Affiliate, Service , ISP, ASN, Country,State, City, DeviceType , DeviceModel ,connectionType , AssetName , Title, seriesName , episodeName, season , ContentID,   ContentType, Rating, AccessType , CompleteView25Pct, CompleteView50Pct, CompleteView75Pct, CompleteView90Pct, Minute0To2 , Minute2To5 , Minute5To10 ,Minute10To20 ,Minute20To40  ,Minute40To60, Minute60To90, Minute90To120 , Minute120To150, Minute150To180, MinuteGT180 ,TotalPlayTimeSec)
            #values = (TransactionStart, TransactionEnd, AccountID)
            # Execute sql Query
            cursor.execute(query, values)

      # Close the cursor
      cursor.close()

      # Commit the transaction
      database.commit()

      # Close the database connection
      database.close()

      # Print results
      print ""
      print "All Done! Bye, for now."
      print ""
      columns = str(sheet.ncols)
      rows = str(sheet.nrows)
      #print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"

if __name__ == '__main__': main()
