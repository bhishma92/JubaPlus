#query 0
#4 
#3 [25309] Black Sails: Ep 301 - XIX (Episode), Black Sails: Ep 301 - XIX
#2 Ash vs Evil Dead: Ep 101 - El Jefe    [24829] Ash vs Evil Dead: Ep 101 - El Jefe (Episode)
# 1 [23382] Outlander: Ep 109 - The Reckoning (Episode)  Outlander: Ep 109 - The Reckoning

#query1
create TABLE db5_1 (AccountID varchar(50));

select 'below is entry' as '';	

insert into db5_1 (AccountID) select distinct (AccountID) from ott where ErrorMsg = '' and TransactionStart between '2016-04-10' and '2016-04-17 23:59:59' and episodeName = 'The Girlfriend Experience';

create unique index i1 on db5_1(AccountID);

#query2
create TABLE db5_2 (AccountID varchar(50));

select 'below is entry' as '';

insert into db5_2 select distinct AccountID from ott where ErrorMsg = '' and TransactionStart between '2016-04-10' and '2016-04-10 23:59:59' and episodeName != 'The Girlfriend Experience' and AccountID != '';

create unique index i2 on db5_2(AccountID);


#query2.1
create TABLE db5_nonleadin (AccountID varchar(50));

insert into db5_nonleadin select AccountID from db5_1 where db5_1.AccountID not in (select AccountID from db5_2);

create unique index i21 on db5_nonleadin(AccountID);	


#query3

create TABLE db5_3 (AccountID varchar(50));

select 'below is entry' as '';

insert into db5_3 (AccountID) select db5_1.AccountID from db5_1 join db5_2 on db5_1.AccountID = db5_2.AccountID;

#quey4

create TABLE db5_4 (AccountID varchar(50));

select 'below is entry' as '';

insert into db5_4 (AccountID) select db5_1.AccountID from db5_1 join db5_nonleadin on db5_1.AccountID = db5_nonleadin.AccountID;

#query5

create unique index i511 on db5_3(AccountID);

create unique index i522 on db5_4(AccountID);

create TABLE db5_w (AccountID varchar(50));

insert into db5_w select distinct AccountID from ott where ErrorMsg = '' and TransactionStart between '2015-04-11' and '2016-03-11 23:59:59';

create unique index i533 on db5_w(AccountID);

select count(db5_4.AccountID) from db5_4 join db5_w on db5_4.AccountID = db5_w.AccountID;

#select count(db1_3.AccountID) from db1_3 join db1_w on db1_3.AccountID = db1_w.AccountID;

#drop tables

drop table db5_1;
drop table db5_2;
drop table db5_3;
drop table db5_4;
drop table db5_w;
drop table db5_nonleadin;









