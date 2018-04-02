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
