#!/bin/sh
	
	mysql starz -e " create table ottTest(ErrorMsg varchar(100), TransactionStart DATETIME DEFAULT NULL, TransactionEnd  DATETIME DEFAULT NULL, AccountID  varchar(50), ClientID  varchar(50), 
	SessionID  BIGINT, DeviceID  varchar(50), Affiliate  varchar(50), Service  varchar(50), ISP  TEXT, ASN  INT, ClientIP varchar(50),
	Country  varchar(50), State  varchar(8), City  varchar(50), playerVersion varchar(50), OS  varchar(32), OsVersion varchar(32), DeviceType  varchar(16), DeviceModel  varchar(32), 
	ConnectionType  varchar(16), Browser varchar(32), BrowserVersion varchar(32), CDN varchar(50), AssetName  varchar(255), Title  varchar(255), seriesName  varchar(255), episodeName  varchar(255), 
	season  SMALLINT(3), ContentID  INT(8), ContentType  varchar(16), Rating  varchar(8), AccessType  varchar(32),
	CompleteView25Pct  BOOL, CompleteView50Pct  BOOL, CompleteView75Pct  BOOL, CompleteView90Pct  BOOL, 
	Minute0To2  BOOL, Minute2To5  BOOL, Minute5To10  BOOL, Minute10To20  BOOL, Minute20To40  BOOL, 
	Minute40To60  BOOL, Minute60To90  BOOL, Minute90To120  BOOL, Minute120To150  BOOL, Minute150To180  BOOL, 
	MinuteGT180  BOOL, startUpType varchar(32), StartUpTimeSec varchar(32), WaitTimeBeforeExitSec varchar(32), TotalPlayTimeSec  FLOAT(9,3), BufferRatio varchar(50), 
	AvgBitrate	varchar(50), AvgBandwidth varchar(50),	AvgRendering varchar(32), resErrs varchar(50)	)"




# 




#AvgBitrate	AvgBandwidth	AvgRendering	resErrs	
cd /home/starzott/Projects/TestFiltered/
for f in *.csv
do 
	SUBSTRING=$(echo $f| cut -c 19-28)
	#arr+=($SUBSTRING)
	echo $SUBSTRING
	#echo $arr
	mysql starz -e "load data local infile '"$f"' into table ottTest fields TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS
	                (@var1, @var2, @var3, AccountID, ClientID, SessionID, DeviceID, Affiliate, Service, ISP, ASN, ClientIP, Country,  State, City,  playerVersion, OS, OsVersion, DeviceType, DeviceModel, ConnectionType, Browser, BrowserVersion,	CDN, AssetName,
	                Title, seriesName, episodeName, season, ContentID, ContentType, Rating, AccessType, CompleteView25Pct, CompleteView50Pct, CompleteView75Pct, CompleteView90Pct, 
	Minute0To2, Minute2To5, Minute5To10, Minute10To20, Minute20To40, 
	Minute40To60, Minute60To90, Minute90To120, Minute120To150, Minute150To180, 
	MinuteGT180, startUpType,	StartUpTimeSec,	WaitTimeBeforeExitSec, TotalPlayTimeSec, BufferRatio, AvgBitrate, AvgBandwidth, AvgRendering, resErrs)
	                
	                SET ErrorMsg = @var1, TransactionStart = STR_TO_DATE(@var2,'%Y-%m-%d %H:%i:%s'), TransactionEnd = STR_TO_DATE(@var3,'%Y-%m-%d %H:%i:%s')" -u root
	
done





