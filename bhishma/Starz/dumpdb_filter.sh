#!/bin/sh
	
	mysql starz -e " create table weekly(ErrorMsg varchar(100), TransactionStart DATETIME DEFAULT NULL, AccountID  varchar(50), ClientID  varchar(50), SessionID varchar(50),
							DeviceID varchar(50), Affiliate varchar(50), Service varchar(50), ISP varchar(50), ASN varchar(50), ClientIP varchar(50), 
							Country varchar(50), State varchar(16), City varchar(50), DeviceType  varchar(50), ConnectionType varchar(50), AssetName  varchar(255),
							C25 INT, C50 INT, C75 INT, C90 INT, M2 INT, M5 INT, M10 INT, M20 INT, M40 INT, M60 INT, M90 INT, M120 INT, M150 INT, M180 INT)"




# 




#AvgBitrate	AvgBandwidth	AvgRendering	resErrs	
cd /home/starzott/Projects/weekly/
for f in *.csv
do 
	SUBSTRING=$(echo $f| cut -c 19-28)
	#arr+=($SUBSTRING)
	echo $SUBSTRING
	#echo $arr
	mysql starz -e "load data local infile '"$f"' into table weekly fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS
	                (ErrorMsg, @var2, AccountID, ClientID, SessionID,
							DeviceID, Affiliate, Service, ISP, ASN, ClientIP, 
							Country, State, City, DeviceType, ConnectionType, AssetName,
							C25, C50, C75, C90, M2, M5, M10, M20, M40, M60, M90, M120, M150, M180)
	                
	                SET TransactionStart = STR_TO_DATE(@var2,'%Y-%m-%d %H:%i:%s')" -u root
	
done





