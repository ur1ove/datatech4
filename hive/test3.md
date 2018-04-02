~~~
[cloudera@quickstart Log Files]$ hdfs dfs -mkdir logs/multi_insert;
[cloudera@quickstart Log Files]$ hdfs dfs -put log_2012613_161117.log log_2013711_155354.log logs/multi_insert;
[cloudera@quickstart Log Files]$ hive

Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j.properties
WARNING: Hive CLI is deprecated and migration to Beeline is recommended.
hive> use hivedemo;
OK
Time taken: 0.393 seconds
hive> CREATE EXTERNAL TABLE page_views (logtime STRING, userid INT, ip STRING, page STRING, ref STRING, os STRING, os_ver STRING, agent STRING)
    > PARTITIONED BY (y STRING, m STRING, d STRING)
    > ROW FORMAT DELIMITED
    > FIELDS TERMINATED BY '\t';
OK
Time taken: 0.33 seconds
hive> CREATE EXTERNAL TABLE staging (
    > logtime STRING,
    > userid INT,
    > ip STRING,
    > page STRING,
    > ref STRING,
    > os STRING,
    > os_ver STRING,
    > agent STRING
    > )
    > ROW FORMAT DELIMITED
    > FIELDS TERMINATED BY '\t'
    > LOCATION '/user/cloudera/logs/multi_insert';
OK
Time taken: 0.086 seconds
hive> 
~~~
~~~
hive> set hive.exec.dynamic.partition.mode=nonstrict;
hive> INSERT INTO TABLE page_views PARTITION (y, m, d)
    > SELECT logtime, userid, ip, page, ref, os, os_ver, agent, substr(logtime, 7, 4), substr(logtime, 1, 2), substr(logtime, 4, 2) FROM staging;
Query ID = cloudera_20180401214343_7dc7f078-0cb7-40d4-83fa-95fa1bf98c03
Total jobs = 3
Launching Job 1 out of 3
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1522635581972_0002, Tracking URL = http://quickstart.cloudera:8088/proxy/application_1522635581972_0002/
Kill Command = /usr/lib/hadoop/bin/hadoop job  -kill job_1522635581972_0002
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
2018-04-01 21:43:28,937 Stage-1 map = 0%,  reduce = 0%
2018-04-01 21:43:39,987 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 3.33 sec
MapReduce Total cumulative CPU time: 3 seconds 330 msec
Ended Job = job_1522635581972_0002
Stage-4 is selected by condition resolver.
Stage-3 is filtered out by condition resolver.
Stage-5 is filtered out by condition resolver.
Moving data to: hdfs://quickstart.cloudera:8020/user/hive/warehouse/hivedemo.db/page_views/.hive-staging_hive_2018-04-01_21-43-17_043_8116903762627685094-1/-ext-10000
Loading data to table hivedemo.page_views partition (y=null, m=null, d=null)
         Time taken for load dynamic partitions : 324
        Loading partition {y=2012, m=06, d=13}
        Loading partition {y=2013, m=07, d=11}
         Time taken for adding to write entity : 4
Partition hivedemo.page_views{y=2012, m=06, d=13} stats: [numFiles=1, numRows=2000, totalSize=149325, rawDataSize=147325]
Partition hivedemo.page_views{y=2013, m=07, d=11} stats: [numFiles=1, numRows=10000, totalSize=732440, rawDataSize=722440]
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 3.33 sec   HDFS Read: 899160 HDFS Write: 881925 SUCCESS
Total MapReduce CPU Time Spent: 3 seconds 330 msec
OK
Time taken: 24.977 seconds
~~~
