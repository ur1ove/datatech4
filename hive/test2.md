~~~
hive (hivedemo)> CREATE EXTERNAL TABLE page_views_ext (logtime STRING, userid INT, ip STRING, page STRING, ref STRING, os STRING, os_ver STRING, agent STRING)
               > PARTITIONED BY (y STRING, m STRING, d STRING)
               > ROW FORMAT DELIMITED
               > FIELDS TERMINATED BY '\t'
               > LOCATION '/user/cloudera/logs/pv_ext/';
OK
Time taken: 0.072 seconds
hive (hivedemo)> show tables;
OK
orders_no_partition
page_views_ext
Time taken: 0.027 seconds, Fetched: 2 row(s)
hive (hivedemo)> select * from page_views_ext;
OK
Time taken: 0.084 seconds
hive (hivedemo)> ALTER TABLE page_views_ext ADD PARTITION (y='2016', m='06', d='13')
               > LOCATION '/user/cloudera/logs/pv_ext/2012/06/13/log/data';
OK
Time taken: 0.1 seconds
hive (hivedemo)> select * from page_views_ext;
......
06/13/2012 16:11:48     418     97.95.79.96     Automotive      Google.com      AndroiHTC      2016    06      13
06/13/2012 16:11:48     506     125.134.148.76  DetailPage      Google.com      AndroiiPhone   2016    06      13
06/13/2012 16:11:48     541     95.34.142.85    ShoppingCart    Google.com      Win8  iPhone   2016    06      13
06/13/2012 16:11:48     509     103.201.27.216  DetailPage      Google.com      AndroiHTC      2016    06      13
06/13/2012 16:11:48     596     146.130.61.120  Electronics     Google.com      AndroiSamsung  2016    06      13
Time taken: 0.074 seconds, Fetched: 2000 row(s)
hive (hivedemo)> 
~~~
~~~
hive (hivedemo)> ALTER TABLE page_views_ext DROP PARTITION (y='2016', m='06', d='13');
Dropped the partition y=2016/m=06/d=13
OK
Time taken: 0.348 seconds
hive (hivedemo)> show tables;
OK
orders_no_partition
page_views_ext
Time taken: 0.027 seconds, Fetched: 2 row(s)
hive (hivedemo)> select * from page_views_ext;
OK
Time taken: 0.108 seconds
hive (hivedemo)> exit;
WARN: The method class org.apache.commons.logging.impl.SLF4JLogFactory#release() was invoked.
WARN: Please see http://www.slf4j.org/codes.html#release for an explanation.
~~~
