#TEE /root/bhishma/Starz/output2.csv
create table results (result BIGINT);

create table columns (col text);

insert into columns select column_name from information_schema.columns where table_name='ott';

#errorMsg	TransactionStart	TransactionEnd startUpType	StartUpTimeSec	WaitTimeBeforeExitSec	TotalPlayTimeSec	BufferRatio	AvgBitrate	AvgBandwidth	AvgRendering	resErrs	
insert into results select count(distinct AccountID) from ott;
insert into results select count(distinct ClientID) from ott;
insert into results select count(distinct SessionID) from ott;
insert into results select count(distinct DeviceID) from ott;
insert into results select count(distinct Affiliate) from ott;
insert into results select count(distinct Service) from ott;
insert into results select count(distinct ISP) from ott;
insert into results select count(distinct ASN) from ott;
insert into results select count(distinct Country) from ott;
insert into results select count(distinct State) from ott;
insert into results select count(distinct City) from ott;
insert into results select count(distinct OS) from ott;
insert into results select count(distinct DeviceType) from ott;
insert into results select count(distinct DeviceModel) from ott;
insert into results select count(distinct connectionType) from ott;
insert into results select count(distinct AssetName) from ott;
insert into results select count(distinct Title) from ott;
insert into results select count(distinct seriesName) from ott;
insert into results select count(distinct episodeName) from ott;
insert into results select count(distinct season) from ott;
insert into results select count(distinct ContentID) from ott;
insert into results select count(distinct ContentType) from ott;
insert into results select count(distinct Rating) from ott;
insert into results select count(distinct AccessType) from ott;
insert into results select count(CompleteView25Pct) from ott where CompleteView25Pct = 1;
insert into results select count(CompleteView50Pct) from ott where CompleteView50Pct = 1;
insert into results select count(CompleteView75Pct) from ott where CompleteView75Pct = 1;
insert into results select count(CompleteView90Pct) from ott where CompleteView90Pct = 1;
insert into results select count(Minute0To2) from ott where Minute0To2 = 1;
insert into results select count(Minute2To5) from ott where Minute2To5 = 1;
insert into results select count(Minute5To10) from ott where Minute5To10 = 1;
insert into results select count(Minute10To20) from ott where Minute10To20= 1;
insert into results select count(Minute20To40) from ott where Minute20To40 = 1;
insert into results select count(Minute40To60) from ott where Minute40To60 = 1;
insert into results select count(Minute60To90) from ott where Minute60To90 = 1;
insert into results select count(Minute90To120) from ott where Minute90To120 = 1;	
insert into results select count(Minute120To150) from ott where Minute120To150 = 1;
insert into results select count(Minute150To180) from ott where Minute150To180 = 1;
insert into results select count(MinuteGT180) from ott where MinuteGT180 = 1;
#insert into results select count(distinct TotalPlayTimeSec) from ott;


select * from columns union select * from results into outfile 'output4.csv' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
#NOTEE
#drop table results;