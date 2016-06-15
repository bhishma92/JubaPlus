#query 0
#4 
#3 [25309] Black Sails: Ep 301 - XIX (Episode), Black Sails: Ep 301 - XIX
#2 Ash vs Evil Dead: Ep 101 - El Jefe    [25309] Black Sails: Ep 301 - XIX (Episode)
# 1 [24829] Ash vs Evil Dead: Ep 101 - El Jefe (Episode  Outlander: Ep 109 - The Reckoning


#query1
create TABLE db3_1 (AccountID varchar(50));

select 'below is entry' as '';	

insert into db3_1 (AccountID) select distinct (AccountID) from dum2 where ErrorMsg = '' and TransactionStart between '2016-01-23' and '2016-01-30 23:59:59' and number = '25309';

create unique index i1 on db3_1(AccountID);

#query2
create TABLE db3_2 (AccountID varchar(50));

select 'below is entry' as '';

insert into db3_2 select distinct AccountID from dum2 where ErrorMsg = '' and TransactionStart between '2016-01-23' and '2016-01-23 23:59:59' and number != '25309';

create unique index i2 on db3_2(AccountID);


#query2.1
create TABLE db3_nonleadin (AccountID varchar(50));

insert into db3_nonleadin select AccountID from db3_1 where db3_1.AccountID not in (select AccountID from db3_2);

create unique index i21 on db3_nonleadin(AccountID);	


#query3

create TABLE db3_3 (AccountID varchar(50));

select 'below is entry' as '';

insert into db3_3 (AccountID) select db3_1.AccountID from db3_1 join db3_2 on db3_1.AccountID = db3_2.AccountID;

#quey4

create TABLE db3_4 (AccountID varchar(50));

select 'below is entry' as '';

insert into db3_4 (AccountID) select db3_1.AccountID from db3_1 join db3_nonleadin on db3_1.AccountID = db3_nonleadin.AccountID;

#query5

create unique index i511 on db3_3(AccountID);

create unique index i522 on db3_4(AccountID);

create TABLE db3_w (AccountID varchar(50));

insert into db3_w select distinct AccountID from dum2 where ErrorMsg = '' and TransactionStart between '2015-01-25' and '2015-12-25 23:59:59';

create unique index i533 on db3_w(AccountID);

select count(db3_4.AccountID) from db3_4 join db3_w on db3_4.AccountID = db3_w.AccountID;

#select count(db1_3.AccountID) from db1_3 join db1_w on db1_3.AccountID = db1_w.AccountID;

#drop tables

drop table db3_1;
drop table db3_2;
drop table db3_3;
drop table db3_4;
drop table db3_w;
drop table db3_nonleadin;









