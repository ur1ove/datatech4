# Sqoop to MySQL

1. Mysql 테이블 생성  
```sql
-- DB 및 사용자 추가
create database auctionDB;

GRANT ALL PRIVILEGES ON auctionDB.* TO datatech4@localhost IDENTIFIED BY 'datatech4';
```  

* MySQL 계정 접속  
```bash
# 계정 : datatech4/datatech4
mysql -u datatech4 -pdatatech4 auctionDB
```

* 원격접속 허용  
```bash
mysql -u root -proot
grant all privileges on *.* to 'datatech4'@'%' identified by 'datatech4';
```

* 테이블 생성
```sql
--테이블 생성
create table ctauInfo_out (
	status varchar(255),
	auctionCount int,
	auctionDate varchar(255),
	addr varchar(255),
	addr0 varchar(255),
	addr1 varchar(255),
	addr2 varchar(255),
	addr3 varchar(255),
	court varchar(255),
	courtCode varchar(255),
	itemNo int,
	remark varchar(255),
	caNo varchar(255),
	pyeong float,
	land1 float,
	land2 float,
	floor1 float,
	floor2 float,
	auctionInfo varchar(255),
	itemType varchar(255),
	appraisedValue bigint,
	minValue bigint,
	saleValue varchar(255),
	saleRate int,
	saleCount int
	);
```	
		
2. Hive ctauInfo 조회결과 저장
```sql
-- auctionDate 데이터 이상함.
-- saleValue 콤마 변환 필요    
-- 테이블 저장
CREATE TABLE ctauInfo_out
row format delimited fields terminated by '|'
AS SELECT * FROM ctauInfo;
```

3. Sqoop로 데이터 적재(Hive to Mysql)
~~~
# mysql connector 필요
[root@dn02 lib]# pwd
/opt/cloudera/parcels/CDH/lib/sqoop/lib

[root@dn02 lib]# wget http://www.java2s.com/Code/JarDownload/mysql/mysql-connector-java-5.1.15.jar.zip
[cloudera@dn01 ~]$ sqoop list-databases --connect jdbc:mysql://localhost --username datatech4 --password datatech4
[cloudera@dn01 ~]$ sqoop list-tables --connect jdbc:mysql://localhost/auctionDB --username datatech4 --password datatech4

# cloudera 유저로 수행) * 권한오류

sqoop export --connect jdbc:mysql://dn01:3306/auctionDB \
 --username datatech4 --password datatech4 \
 --table ctauInfo_out --export-dir '/user/hive/warehouse/auctiondb.db/ctauinfo_out' \
 --fields-terminated-by '|'

# 한글깨짐 조치 
[cloudera@dn01 ~]$ vi /etc/my.cnf
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8

[client]
default-character-set = utf8

[mysql]

default-character-set = utf8

[mysqldump]

default-character-set = utf8



ALTER DATABASE auctionDB DEFAULT CHARACTER SET utf8;

-- saleValue 콤마제거
update ctauInfo_out set saleValue = replace(saleValue,',','');


-- auctionDate 데이터 이상하여 처리함
select count(*)  from ctauInfo_out where length(auctionDate) > 10;
+----------+
| count(*) |
+----------+
|     2677 |
+----------+
1 row in set (0.16 sec)


mysql> select auctionDate  from ctauInfo_out where length(auctionDate) > 10 limit 10;
(2011-10-06∼2011-10-13)2011-10-19

SELECT right(auctionDate,10) from ctauInfo_out where length(auctionDate) > 10;

update ctauInfo_out set auctionDate = right(auctionDate,10) where length(auctionDate) > 10;
~~~