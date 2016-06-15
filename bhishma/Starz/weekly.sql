#ErrorMsg, @var2, AccountID, ClientID, SessionID,
#							DeviceID, Affiliate, Service, ISP, ASN, ClientIP, 
#							Country, State, City, DeviceType, ConnectionType, AssetName,
#							C25, C50, C75, C90, M2, M5, M10, M20, M40, M60, M90, M120, M150, M180


select count(*) from weekly;

select count(ErrorMsg) from weekly where ErrorMsg != '';

select count(distinct AccountID) from weekly;

select count(distinct SessionID) from weekly;

select count(distinct DeviceID) from weekly;

select count(distinct Affiliate) from weekly;

select count(distinct Service) from weekly;

select count(distinct ISP) from weekly;

select count(distinct ASN) from weekly;

select count(distinct ClientIP) from weekly;

select count(distinct Country) from weekly;

select count(distinct State) from weekly;

select count(distinct City) from weekly;

select count(distinct DeviceType) from weekly;

select count(distinct ConnectionType) from weekly;

select count(C25) from weekly where C25 = 1;

select count(C50) from weekly where C50 = 1;

select count(C75) from weekly where C75 = 1;

select count(C90) from weekly where C90 = 1;

select count(M2) from weekly where M2 = 1;

select count(M5) from weekly where M5 = 1;

select count(M10) from weekly where M10 = 1;

select count(M20) from weekly where M20 = 1;

select count(M40) from weekly where M40 = 1;

select count(M60) from weekly where M60 = 1;

select count(M90) from weekly where M90 = 1;

select count(M120) from weekly where M120 = 1;

select count(M150) from weekly where M150 = 1;

select count(M180) from weekly where M180 = 1;







