# HIVE to Elasticsearch

* Hadoop 에 필요한 Elasticsearch 연동용 StorageHandler jar 파일 등록 후 사용  

~~~
[eduuser@dn01 ~]$ sudo -u hive hadoop fs -ls /user/hive/
Found 3 items
drwx------   - hive hive          0 2018-04-24 19:05 /user/hive/.Trash
drwx------   - hive hive          0 2018-04-24 04:59 /user/hive/.staging
drwxrwxrwt   - hive hive          0 2018-04-23 22:41 /user/hive/warehouse
[eduuser@dn01 ~]$
[eduuser@dn01 ~]$ wget https://artifacts.elastic.co/downloads/elasticsearch-hadoop/elasticsearch-hadoop-6.2.4.zip
--2018-04-24 19:51:32--  https://artifacts.elastic.co/downloads/elasticsearch-hadoop/elasticsearch-hadoop-6.2.4.zip
Resolving artifacts.elastic.co (artifacts.elastic.co)... 23.21.67.46, 23.23.109.100, 184.72.242.47, ...
Connecting to artifacts.elastic.co (artifacts.elastic.co)|23.21.67.46|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 7692396 (7.3M) [application/zip]
Saving to: ‘elasticsearch-hadoop-6.2.4.zip’

100%[=====================================================================================================================================================>] 7,692,396   2.42MB/s   in 3.0s

2018-04-24 19:51:37 (2.42 MB/s) - ‘elasticsearch-hadoop-6.2.4.zip’ saved [7692396/7692396]

[eduuser@dn01 ~]$ unzip elasticsearch-hadoop-6.2.4.zip
Archive:  elasticsearch-hadoop-6.2.4.zip
   creating: elasticsearch-hadoop-6.2.4/
  inflating: elasticsearch-hadoop-6.2.4/README.md
  inflating: elasticsearch-hadoop-6.2.4/LICENSE.txt
  inflating: elasticsearch-hadoop-6.2.4/NOTICE.txt
   creating: elasticsearch-hadoop-6.2.4/dist/
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-cascading-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-cascading-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-cascading-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-hive-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-hive-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-hive-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-mr-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-mr-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-mr-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-pig-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-pig-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-pig-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-spark-20_2.11-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-spark-20_2.11-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-spark-20_2.11-6.2.4-javadoc.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-storm-6.2.4-sources.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-storm-6.2.4.jar
  inflating: elasticsearch-hadoop-6.2.4/dist/elasticsearch-storm-6.2.4-javadoc.jar
[eduuser@dn01 ~]$ cd elasticsearch-hadoop-6.2.4/dist/
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ sudo -u hive hadoop fs -mkdir /user/hive/aux_jars
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ sudo -u hive hadoop fs -ls /user/hive/
Found 4 items
drwx------   - hive hive          0 2018-04-24 19:05 /user/hive/.Trash
drwx------   - hive hive          0 2018-04-24 04:59 /user/hive/.staging
drwxr-xr-x   - hive hive          0 2018-04-24 19:53 /user/hive/aux_jars
drwxrwxrwt   - hive hive          0 2018-04-23 22:41 /user/hive/warehouse
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ sudo -u hive hadoop fs -chmod 1777 /user/hive/aux_jars
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ sudo -u hive hadoop fs -ls /user/hive/
Found 4 items
drwx------   - hive hive          0 2018-04-24 19:05 /user/hive/.Trash
drwx------   - hive hive          0 2018-04-24 04:59 /user/hive/.staging
drwxrwxrwt   - hive hive          0 2018-04-24 19:53 /user/hive/aux_jars
drwxrwxrwt   - hive hive          0 2018-04-23 22:41 /user/hive/warehouse
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ hadoop fs -put /home/eduuser/elasticsearch-hadoop-6.2.4/dist/elasticsearch-hadoop-6.2.4.jar /user/hive/aux_jars/
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ sudo -u hive hadoop fs -ls /user/hive/aux_jars
Found 1 items
-rw-r--r--   3 eduuser hive     890273 2018-04-24 19:55 /user/hive/aux_jars/elasticsearch-hadoop-6.2.4.jar
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$
[eduuser@dn01 dist]$ beeline --showDbInPrompt=true;
Beeline version 1.1.0-cdh5.14.2 by Apache Hive
beeline> !connect jdbc:hive2://dn02:10000
scan complete in 4ms
Connecting to jdbc:hive2://dn02:10000
Enter username for jdbc:hive2://dn02:10000: hive
Enter password for jdbc:hive2://dn02:10000: ****
Connected to: Apache Hive (version 1.1.0-cdh5.14.2)
Driver: Hive JDBC (version 1.1.0-cdh5.14.2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> show databases;
INFO  : Compiling command(queryId=hive_20180424195757_887d706b-1876-4378-9a85-78bf0c35aae0): show databases
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:database_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424195757_887d706b-1876-4378-9a85-78bf0c35aae0); Time taken: 0.075 seconds
INFO  : Executing command(queryId=hive_20180424195757_887d706b-1876-4378-9a85-78bf0c35aae0): show databases
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424195757_887d706b-1876-4378-9a85-78bf0c35aae0); Time taken: 0.032 seconds
INFO  : OK
+----------------+--+
| database_name  |
+----------------+--+
| assetdb        |
| auctiondb      |
| default        |
| readb          |
+----------------+--+
5 rows selected (0.313 seconds)
0: jdbc:hive2://dn02:10000> use auctiondb;
INFO  : Compiling command(queryId=hive_20180424195757_ba8a2651-bead-4e67-b896-3defb715fc4c): use auctiondb
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20180424195757_ba8a2651-bead-4e67-b896-3defb715fc4c); Time taken: 0.01 seconds
INFO  : Executing command(queryId=hive_20180424195757_ba8a2651-bead-4e67-b896-3defb715fc4c): use auctiondb
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424195757_ba8a2651-bead-4e67-b896-3defb715fc4c); Time taken: 0.011 seconds
INFO  : OK
No rows affected (0.044 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> add jar hdfs:///user/hive/aux_jars/elasticsearch-hadoop-6.2.4.jar;
INFO  : converting to local hdfs:///user/hive/aux_jars/elasticsearch-hadoop-6.2.4.jar
INFO  : Added [/tmp/9a6c93cd-6029-4e8a-a95c-4dcbd3600b62_resources/elasticsearch-hadoop-6.2.4.jar] to class path
INFO  : Added resources: [hdfs:///user/hive/aux_jars/elasticsearch-hadoop-6.2.4.jar]
No rows affected (0.045 seconds)
0: jdbc:hive2://dn02:10000> show tables;
INFO  : Compiling command(queryId=hive_20180424195959_5cf22187-0764-46d2-be35-c1299ae99da5): show tables
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:tab_name, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424195959_5cf22187-0764-46d2-be35-c1299ae99da5); Time taken: 0.005 seconds
INFO  : Executing command(queryId=hive_20180424195959_5cf22187-0764-46d2-be35-c1299ae99da5): show tables
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424195959_5cf22187-0764-46d2-be35-c1299ae99da5); Time taken: 0.015 seconds
INFO  : OK
+---------------+--+
|   tab_name    |
+---------------+--+
| ctauinfo      |
| ctauinfo_out  |
+---------------+--+
2 rows selected (0.055 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> desc formatted ctauinfo;
INFO  : Compiling command(queryId=hive_20180424200101_7ddaa768-d498-4736-9750-c05d67acf1c5): desc formatted ctauinfo
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:col_name, type:string, comment:from deserializer), FieldSchema(name:data_type, type:string, comment:from deserializer), FieldSchema(name:comment, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424200101_7ddaa768-d498-4736-9750-c05d67acf1c5); Time taken: 0.098 seconds
INFO  : Executing command(queryId=hive_20180424200101_7ddaa768-d498-4736-9750-c05d67acf1c5): desc formatted ctauinfo
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424200101_7ddaa768-d498-4736-9750-c05d67acf1c5); Time taken: 0.038 seconds
INFO  : OK
+-------------------------------+----------------------------------------------------+-----------------------+--+
|           col_name            |                     data_type                      |        comment        |
+-------------------------------+----------------------------------------------------+-----------------------+--+
| # col_name                    | data_type                                          | comment               |
|                               | NULL                                               | NULL                  |
| status                        | string                                             | from deserializer     |
| auctioncount                  | string                                             | from deserializer     |
| auctiondate                   | string                                             | from deserializer     |
| addr                          | string                                             | from deserializer     |
| addr0                         | string                                             | from deserializer     |
| addr1                         | string                                             | from deserializer     |
| addr2                         | string                                             | from deserializer     |
| addr3                         | string                                             | from deserializer     |
| court                         | string                                             | from deserializer     |
| courtcode                     | string                                             | from deserializer     |
| itemno                        | string                                             | from deserializer     |
| remark                        | string                                             | from deserializer     |
| cano                          | string                                             | from deserializer     |
| pyeong                        | string                                             | from deserializer     |
| land1                         | string                                             | from deserializer     |
| land2                         | string                                             | from deserializer     |
| floor1                        | string                                             | from deserializer     |
| floor2                        | string                                             | from deserializer     |
| auctioninfo                   | string                                             | from deserializer     |
| itemtype                      | string                                             | from deserializer     |
| appraisedvalue                | string                                             | from deserializer     |
| minvalue                      | string                                             | from deserializer     |
| salevalue                     | string                                             | from deserializer     |
| salerate                      | string                                             | from deserializer     |
| salecount                     | string                                             | from deserializer     |
|                               | NULL                                               | NULL                  |
| # Detailed Table Information  | NULL                                               | NULL                  |
| Database:                     | auctiondb                                          | NULL                  |
| Owner:                        | flume                                              | NULL                  |
| CreateTime:                   | Mon Apr 23 09:06:44 EDT 2018                       | NULL                  |
| LastAccessTime:               | UNKNOWN                                            | NULL                  |
| Protect Mode:                 | None                                               | NULL                  |
| Retention:                    | 0                                                  | NULL                  |
| Location:                     | hdfs://nn01:8020/flume/data3                       | NULL                  |
| Table Type:                   | EXTERNAL_TABLE                                     | NULL                  |
| Table Parameters:             | NULL                                               | NULL                  |
|                               | COLUMN_STATS_ACCURATE                              | false                 |
|                               | EXTERNAL                                           | TRUE                  |
|                               | numFiles                                           | 0                     |
|                               | numRows                                            | -1                    |
|                               | rawDataSize                                        | -1                    |
|                               | totalSize                                          | 0                     |
|                               | transient_lastDdlTime                              | 1524488804            |
|                               | NULL                                               | NULL                  |
| # Storage Information         | NULL                                               | NULL                  |
| SerDe Library:                | org.apache.hive.hcatalog.data.JsonSerDe            | NULL                  |
| InputFormat:                  | org.apache.hadoop.mapred.TextInputFormat           | NULL                  |
| OutputFormat:                 | org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat | NULL                  |
| Compressed:                   | No                                                 | NULL                  |
| Num Buckets:                  | -1                                                 | NULL                  |
| Bucket Columns:               | []                                                 | NULL                  |
| Sort Columns:                 | []                                                 | NULL                  |
| Storage Desc Params:          | NULL                                               | NULL                  |
|                               | serialization.format                               | 1                     |
+-------------------------------+----------------------------------------------------+-----------------------+--+
56 rows selected (0.232 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> CREATE EXTERNAL TABLE auction_es (
. . . . . . . . . . . . . >     status          STRING,
. . . . . . . . . . . . . >     auctionCount    int,
. . . . . . . . . . . . . >     auctionDate     timestamp,
. . . . . . . . . . . . . >     addr            STRING,
. . . . . . . . . . . . . >     addr0           STRING,
. . . . . . . . . . . . . >     addr1           STRING,
. . . . . . . . . . . . . >     addr2           STRING,
. . . . . . . . . . . . . >     addr3           STRING,
. . . . . . . . . . . . . >     court           STRING,
. . . . . . . . . . . . . >     courtCode       STRING,
. . . . . . . . . . . . . >     itemNo          int,
. . . . . . . . . . . . . >     remark          STRING,
. . . . . . . . . . . . . >     caNo            STRING,
. . . . . . . . . . . . . >     pyeong          int,
. . . . . . . . . . . . . >     land1           float,
. . . . . . . . . . . . . >     land2           float,
. . . . . . . . . . . . . >     floor1          float,
. . . . . . . . . . . . . >     floor2          float,
. . . . . . . . . . . . . >     auctionInfo     STRING,
. . . . . . . . . . . . . >     itemType        STRING,
. . . . . . . . . . . . . >     appraisedValue  bigint,
. . . . . . . . . . . . . >     minValue        bigint,
. . . . . . . . . . . . . >     saleValue       bigint,
. . . . . . . . . . . . . >     saleRate        int,
. . . . . . . . . . . . . >     saleCount       int)
. . . . . . . . . . . . . > COMMENT 'Auction ES Table'
. . . . . . . . . . . . . > STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
. . . . . . . . . . . . . > TBLPROPERTIES('es.resource' = 'auction_data/auction',
. . . . . . . . . . . . . >  'es.nodes'='dn01', 'es.port'='9201' );
INFO  : Compiling command(queryId=hive_20180424200303_5bc78e21-3952-40b3-9378-caaf52b9b125): CREATE EXTERNAL TABLE auction_es (
status          STRING,
auctionCount    int,
auctionDate     timestamp,
addr            STRING,
addr0           STRING,
addr1           STRING,
addr2           STRING,
addr3           STRING,
court           STRING,
courtCode       STRING,
itemNo          int,
remark          STRING,
caNo            STRING,
pyeong          int,
land1           float,
land2           float,
floor1          float,
floor2          float,
auctionInfo     STRING,
itemType        STRING,
appraisedValue  bigint,
minValue        bigint,
saleValue       bigint,
saleRate        int,
saleCount       int)
COMMENT 'Auction ES Table'
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
TBLPROPERTIES('es.resource' = 'auction_data/auction',
'es.nodes'='dn01', 'es.port'='9201' )
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:null, properties:null)
INFO  : Completed compiling command(queryId=hive_20180424200303_5bc78e21-3952-40b3-9378-caaf52b9b125); Time taken: 0.016 seconds
INFO  : Executing command(queryId=hive_20180424200303_5bc78e21-3952-40b3-9378-caaf52b9b125): CREATE EXTERNAL TABLE auction_es (
status          STRING,
auctionCount    int,
auctionDate     timestamp,
addr            STRING,
addr0           STRING,
addr1           STRING,
addr2           STRING,
addr3           STRING,
court           STRING,
courtCode       STRING,
itemNo          int,
remark          STRING,
caNo            STRING,
pyeong          int,
land1           float,
land2           float,
floor1          float,
floor2          float,
auctionInfo     STRING,
itemType        STRING,
appraisedValue  bigint,
minValue        bigint,
saleValue       bigint,
saleRate        int,
saleCount       int)
COMMENT 'Auction ES Table'
STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
TBLPROPERTIES('es.resource' = 'auction_data/auction',
'es.nodes'='dn01', 'es.port'='9201' )
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424200303_5bc78e21-3952-40b3-9378-caaf52b9b125); Time taken: 0.235 seconds
INFO  : OK
No rows affected (0.297 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> desc formatted auction_es;
INFO  : Compiling command(queryId=hive_20180424200404_4284a6ac-535d-4b87-b81d-a68305be36e9): desc formatted auction_es
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:col_name, type:string, comment:from deserializer), FieldSchema(name:data_type, type:string, comment:from deserializer), FieldSchema(name:comment, type:string, comment:from deserializer)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424200404_4284a6ac-535d-4b87-b81d-a68305be36e9); Time taken: 0.041 seconds
INFO  : Executing command(queryId=hive_20180424200404_4284a6ac-535d-4b87-b81d-a68305be36e9): desc formatted auction_es
INFO  : Starting task [Stage-0:DDL] in serial mode
INFO  : Completed executing command(queryId=hive_20180424200404_4284a6ac-535d-4b87-b81d-a68305be36e9); Time taken: 0.019 seconds
INFO  : OK
+-------------------------------+----------------------------------------------------+-------------------------------------------------+--+
|           col_name            |                     data_type                      |                     comment                     |
+-------------------------------+----------------------------------------------------+-------------------------------------------------+--+
| # col_name                    | data_type                                          | comment                                         |
|                               | NULL                                               | NULL                                            |
| status                        | string                                             | from deserializer                               |
| auctioncount                  | int                                                | from deserializer                               |
| auctiondate                   | timestamp                                          | from deserializer                               |
| addr                          | string                                             | from deserializer                               |
| addr0                         | string                                             | from deserializer                               |
| addr1                         | string                                             | from deserializer                               |
| addr2                         | string                                             | from deserializer                               |
| addr3                         | string                                             | from deserializer                               |
| court                         | string                                             | from deserializer                               |
| courtcode                     | string                                             | from deserializer                               |
| itemno                        | int                                                | from deserializer                               |
| remark                        | string                                             | from deserializer                               |
| cano                          | string                                             | from deserializer                               |
| pyeong                        | int                                                | from deserializer                               |
| land1                         | float                                              | from deserializer                               |
| land2                         | float                                              | from deserializer                               |
| floor1                        | float                                              | from deserializer                               |
| floor2                        | float                                              | from deserializer                               |
| auctioninfo                   | string                                             | from deserializer                               |
| itemtype                      | string                                             | from deserializer                               |
| appraisedvalue                | bigint                                             | from deserializer                               |
| minvalue                      | bigint                                             | from deserializer                               |
| salevalue                     | bigint                                             | from deserializer                               |
| salerate                      | int                                                | from deserializer                               |
| salecount                     | int                                                | from deserializer                               |
|                               | NULL                                               | NULL                                            |
| # Detailed Table Information  | NULL                                               | NULL                                            |
| Database:                     | auctiondb                                          | NULL                                            |
| Owner:                        | hive                                               | NULL                                            |
| CreateTime:                   | Tue Apr 24 20:03:45 EDT 2018                       | NULL                                            |
| LastAccessTime:               | UNKNOWN                                            | NULL                                            |
| Protect Mode:                 | None                                               | NULL                                            |
| Retention:                    | 0                                                  | NULL                                            |
| Location:                     | hdfs://nn01:8020/user/hive/warehouse/auctiondb.db/auction_es | NULL                                            |
| Table Type:                   | EXTERNAL_TABLE                                     | NULL                                            |
| Table Parameters:             | NULL                                               | NULL                                            |
|                               | COLUMN_STATS_ACCURATE                              | false                                           |
|                               | EXTERNAL                                           | TRUE                                            |
|                               | comment                                            | Auction ES Table                                |
|                               | es.nodes                                           | dn01                                            |
|                               | es.port                                            | 9201                                            |
|                               | es.resource                                        | auction_data/auction                            |
|                               | numFiles                                           | 0                                               |
|                               | numRows                                            | -1                                              |
|                               | rawDataSize                                        | -1                                              |
|                               | storage_handler                                    | org.elasticsearch.hadoop.hive.EsStorageHandler  |
|                               | totalSize                                          | 0                                               |
|                               | transient_lastDdlTime                              | 1524614625                                      |
|                               | NULL                                               | NULL                                            |
| # Storage Information         | NULL                                               | NULL                                            |
| SerDe Library:                | org.elasticsearch.hadoop.hive.EsSerDe              | NULL                                            |
| InputFormat:                  | null                                               | NULL                                            |
| OutputFormat:                 | null                                               | NULL                                            |
| Compressed:                   | No                                                 | NULL                                            |
| Num Buckets:                  | -1                                                 | NULL                                            |
| Bucket Columns:               | []                                                 | NULL                                            |
| Sort Columns:                 | []                                                 | NULL                                            |
| Storage Desc Params:          | NULL                                               | NULL                                            |
|                               | serialization.format                               | 1                                               |
+-------------------------------+----------------------------------------------------+-------------------------------------------------+--+
61 rows selected (0.153 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> select
. . . . . . . . . . . . . >     status,
. . . . . . . . . . . . . >     cast(auctionCount as int),
. . . . . . . . . . . . . >     cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
. . . . . . . . . . . . . >     addr,
. . . . . . . . . . . . . >     addr0,
. . . . . . . . . . . . . >     addr1,
. . . . . . . . . . . . . >     addr2,
. . . . . . . . . . . . . >     addr3,
. . . . . . . . . . . . . >     court,
. . . . . . . . . . . . . >     courtCode,
. . . . . . . . . . . . . >     cast(itemNo as int),
. . . . . . . . . . . . . >     remark,
. . . . . . . . . . . . . >     caNo,
. . . . . . . . . . . . . >     cast(pyeong  as int),
. . . . . . . . . . . . . >     cast(land1  as float),
. . . . . . . . . . . . . >     cast(land2  as float),
. . . . . . . . . . . . . >     cast(floor1  as float),
. . . . . . . . . . . . . >     cast(floor2 as float),
. . . . . . . . . . . . . >     auctionInfo,
. . . . . . . . . . . . . >     itemType,
. . . . . . . . . . . . . >     cast(appraisedValue as bigint),
. . . . . . . . . . . . . >     cast(minValue  as bigint),
. . . . . . . . . . . . . >     cast(regexp_replace(saleValue, ',','') as bigint),
. . . . . . . . . . . . . >     cast(saleRate as int),
. . . . . . . . . . . . . >     cast(saleCount as int)
. . . . . . . . . . . . . > from ctauinfo
. . . . . . . . . . . . . > limit 10;
INFO  : Compiling command(queryId=hive_20180424200505_ee18d082-f904-4045-a042-de46314f015a): select
status,
cast(auctionCount as int),
cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
addr,
addr0,
addr1,
addr2,
addr3,
court,
courtCode,
cast(itemNo as int),
remark,
caNo,
cast(pyeong  as int),
cast(land1  as float),
cast(land2  as float),
cast(floor1  as float),
cast(floor2 as float),
auctionInfo,
itemType,
cast(appraisedValue as bigint),
cast(minValue  as bigint),
cast(regexp_replace(saleValue, ',','') as bigint),
cast(saleRate as int),
cast(saleCount as int)
from ctauinfo
limit 10
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:status, type:string, comment:null), FieldSchema(name:auctioncount, type:int, comment:null), FieldSchema(name:_c2, type:timestamp, comment:null), FieldSchema(name:addr, type:string, comment:null), FieldSchema(name:addr0, type:string, comment:null), FieldSchema(name:addr1, type:string, comment:null), FieldSchema(name:addr2, type:string, comment:null), FieldSchema(name:addr3, type:string, comment:null), FieldSchema(name:court, type:string, comment:null), FieldSchema(name:courtcode, type:string, comment:null), FieldSchema(name:itemno, type:int, comment:null), FieldSchema(name:remark, type:string, comment:null), FieldSchema(name:cano, type:string, comment:null), FieldSchema(name:pyeong, type:int, comment:null), FieldSchema(name:land1, type:float, comment:null), FieldSchema(name:land2, type:float, comment:null), FieldSchema(name:floor1, type:float, comment:null), FieldSchema(name:floor2, type:float, comment:null), FieldSchema(name:auctioninfo, type:string, comment:null), FieldSchema(name:itemtype, type:string, comment:null), FieldSchema(name:appraisedvalue, type:bigint, comment:null), FieldSchema(name:minvalue, type:bigint, comment:null), FieldSchema(name:_c22, type:bigint, comment:null), FieldSchema(name:salerate, type:int, comment:null), FieldSchema(name:salecount, type:int, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424200505_ee18d082-f904-4045-a042-de46314f015a); Time taken: 0.157 seconds
INFO  : Executing command(queryId=hive_20180424200505_ee18d082-f904-4045-a042-de46314f015a): select
status,
cast(auctionCount as int),
cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
addr,
addr0,
addr1,
addr2,
addr3,
court,
courtCode,
cast(itemNo as int),
remark,
caNo,
cast(pyeong  as int),
cast(land1  as float),
cast(land2  as float),
cast(floor1  as float),
cast(floor2 as float),
auctionInfo,
itemType,
cast(appraisedValue as bigint),
cast(minValue  as bigint),
cast(regexp_replace(saleValue, ',','') as bigint),
cast(saleRate as int),
cast(saleCount as int)
from ctauinfo
limit 10
INFO  : Query ID = hive_20180424200505_ee18d082-f904-4045-a042-de46314f015a
INFO  : Total jobs = 1
INFO  : Launching Job 1 out of 1
INFO  : Starting task [Stage-1:MAPRED] in serial mode
INFO  : Number of reduce tasks is set to 0 since there's no reduce operator
INFO  : number of splits:1
INFO  : Submitting tokens for job: job_1523845385074_0063
INFO  : The url to track the job: http://nn01:8088/proxy/application_1523845385074_0063/
INFO  : Starting Job = job_1523845385074_0063, Tracking URL = http://nn01:8088/proxy/application_1523845385074_0063/
INFO  : Kill Command = /opt/cloudera/parcels/CDH-5.14.2-1.cdh5.14.2.p0.3/lib/hadoop/bin/hadoop job  -kill job_1523845385074_0063
INFO  : Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
INFO  : 2018-04-24 20:05:56,876 Stage-1 map = 0%,  reduce = 0%
INFO  : 2018-04-24 20:06:05,664 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 3.36 sec
INFO  : MapReduce Total cumulative CPU time: 3 seconds 360 msec
INFO  : Ended Job = job_1523845385074_0063
INFO  : MapReduce Jobs Launched:
INFO  : Stage-Stage-1: Map: 1   Cumulative CPU: 3.36 sec   HDFS Read: 76093 HDFS Write: 4882 SUCCESS
INFO  : Total MapReduce CPU Time Spent: 3 seconds 360 msec
INFO  : Completed executing command(queryId=hive_20180424200505_ee18d082-f904-4045-a042-de46314f015a); Time taken: 16.411 seconds
INFO  : OK
+---------+---------------+------------------------+--------------------------------------------+--------+--------+--------+--------+---------+------------+---------+---------+--------------+---------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+-----------+-----------------+-----------+------------+-----------+------------+--+
| status  | auctioncount  |          _c2           |                    addr                    | addr0  | addr1  | addr2  | addr3  |  court  | courtcode  | itemno  | remark  |     cano     | pyeong  |        land1        |        land2        |       floor1        |       floor2        |                 auctioninfo                  | itemtype  | appraisedvalue  | minvalue  |    _c22    | salerate  | salecount  |
+---------+---------------+------------------------+--------------------------------------------+--------+--------+--------+--------+---------+------------+---------+---------+--------------+---------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+-----------+-----------------+-----------+------------+-----------+------------+--+
| 배당종결    | 2             | 2008-01-25 00:00:00.0  | 부산광역시 동래구 온천동 1444-1궁전아이브 5층 505호          | 부산광역시  | 동래구    | 온천동    |        | 부산지방법원  | B01        | 1       | 관련사건    | 2007타경6344   | 10      | 10.569999694824219  | 3.200000047683716   | 84.54000091552734   | 25.56999969482422   | 35평형,토지 10.57㎡(3.2평),건물 84.54㎡(25.57평)       | 아파트       | 176000000       | NULL      | NULL       | NULL      | NULL       |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 북구 덕천동 250-9덕천한성맨션 2동 1층 112호        | 부산광역시  | 북구     | 덕천동    |        | 부산지방법원  | B01        | 1       |         | 2007타경9220   | 39      | 39.49599838256836   | 11.949999809265137  | 44.72999954223633   | 13.529999732971191  | 16평형,토지 39.496㎡(11.95평),건물 44.73㎡(13.53평)    | 아파트       | 44000000        | NULL      | 36399900   | 83        | 4          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 연제구 연산동 57-134연산부전타워 101동 2층 2-202호  | 부산광역시  | 연제구    | 연산동    |        | 부산지방법원  | B01        | 1       |         | 2007타경15720  | 20      | 20.049999237060547  | 6.070000171661377   | 59.91999816894531   | 18.1299991607666    | 25평형,토지 20.05㎡(6.07평),건물 59.92㎡(18.13평)      | 아파트       | 76000000        | NULL      | 65999000   | 87        | 2          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 사하구 장림동 산21-2장림우림그린빌라 101동 9층 907호   | 부산광역시  | 사하구    | 장림동    |        | 부산지방법원  | B01        | 1       |         | 2007타경20951  | 79      | 79.98269653320312   | 24.190000534057617  | 132.5399932861328   | 40.09000015258789   | 50평형,토지 79.9827㎡(24.19평),건물 132.54㎡(40.09평)  | 아파트       | 120000000       | NULL      | 99100000   | 83        | 3          |
| 배당종결    | 2             | 2008-01-25 00:00:00.0  | 부산광역시 서구 암남동 81-12송도자유비치아파트 3층 307호        | 부산광역시  | 서구     | 암남동    |        | 부산지방법원  | B01        | 1       |         | 2007타경23424  | 17      | 17.540000915527344  | 5.309999942779541   | 48.630001068115234  | 14.710000038146973  | 20평형,토지 17.54㎡(5.31평),건물 48.63㎡(14.71평)      | 아파트       | 58000000        | NULL      | 42850000   | 74        | 2          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 사하구 다대동 94삼환2차아파트 102동 10층 1005호     | 부산광역시  | 사하구    | 다대동    |        | 부산지방법원  | B01        | 1       |         | 2007타경26645  | 14      | 14.73900032043457   | 4.460000038146973   | 84.98999786376953   | 25.709999084472656  | 32평형,토지 14.739㎡(4.46평),건물 84.99㎡(25.71평)     | 아파트       | 120000000       | NULL      | 102899000  | 86        | 6          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 부산진구 부전동 450네오스포 20층 2024호           | 부산광역시  | 부산진구   | 부전동    |        | 부산지방법원  | B01        | 1       |         | 2007타경29422  | 12      | 12.92199993133545   | 3.9100000858306885  | 84.6449966430664    | 25.610000610351562  | 38평형,토지 12.922㎡(3.91평),건물 84.645㎡(25.61평)    | 아파트       | 120000000       | NULL      | 102349000  | 85        | 5          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 사상구 모라동 75모라주공아파트 402동 7층 702호       | 부산광역시  | 사상구    | 모라동    |        | 부산지방법원  | B01        | 1       |         | 2007타경30903  | 55      | 55.0                | 16.639999389648438  | 49.939998626708984  | 15.109999656677246  | 21평형,토지 55㎡(16.64평),건물 49.94㎡(15.11평)        | 아파트       | 62000000        | NULL      | 55290000   | 89        | 4          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 부산진구 당감동 516주공아파트 307동 15층 1502호     | 부산광역시  | 부산진구   | 당감동    |        | 부산지방법원  | B01        | 1       |         | 2007타경31494  | 51      | 51.75               | 15.649999618530273  | 79.06999969482422   | 23.920000076293945  | 31평형,토지 51.75㎡(15.65평),건물 79.07㎡(23.92평)     | 아파트       | 105000000       | NULL      | 97000000   | 92        | 5          |
| 배당종결    | 1             | 2008-01-25 00:00:00.0  | 부산광역시 부산진구 범천동 944-1범천경남아파트 101동 3층 307호   | 부산광역시  | 부산진구   | 범천동    |        | 부산지방법원  | B01        | 1       |         | 2007타경31890  | 17      | 17.339500427246094  | 5.25                | 59.942501068115234  | 18.1299991607666    | 24평형,토지 17.3395㎡(5.25평),건물 59.9425㎡(18.13평)  | 아파트       | 90000000        | NULL      | 77450000   | 86        | 3          |
+---------+---------------+------------------------+--------------------------------------------+--------+--------+--------+--------+---------+------------+---------+---------+--------------+---------+---------------------+---------------------+---------------------+---------------------+----------------------------------------------+-----------+-----------------+-----------+------------+-----------+------------+--+
10 rows selected (16.742 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> INSERT OVERWRITE TABLE auction_es
. . . . . . . . . . . . . > select
. . . . . . . . . . . . . >     status,
. . . . . . . . . . . . . >     cast(auctionCount as int),
. . . . . . . . . . . . . >     cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
. . . . . . . . . . . . . >     addr,
. . . . . . . . . . . . . >     addr0,
. . . . . . . . . . . . . >     addr1,
. . . . . . . . . . . . . >     addr2,
. . . . . . . . . . . . . >     addr3,
. . . . . . . . . . . . . >     court,
. . . . . . . . . . . . . >     courtCode,
. . . . . . . . . . . . . >     cast(itemNo as int),
. . . . . . . . . . . . . >     remark,
. . . . . . . . . . . . . >     caNo,
. . . . . . . . . . . . . >     cast(pyeong  as int),
. . . . . . . . . . . . . >     cast(land1  as float),
. . . . . . . . . . . . . >     cast(land2  as float),
. . . . . . . . . . . . . >     cast(floor1  as float),
. . . . . . . . . . . . . >     cast(floor2 as float),
. . . . . . . . . . . . . >     auctionInfo,
. . . . . . . . . . . . . >     itemType,
. . . . . . . . . . . . . >     cast(appraisedValue as bigint),
. . . . . . . . . . . . . >     cast(minValue  as bigint),
. . . . . . . . . . . . . >     cast(regexp_replace(saleValue, ',','') as bigint),
. . . . . . . . . . . . . >     cast(saleRate as int),
. . . . . . . . . . . . . >     cast(saleCount as int)
. . . . . . . . . . . . . > from ctauinfo;
INFO  : Compiling command(queryId=hive_20180424203636_5b7587ff-ed1c-4aa4-9506-c57a7174f11f): INSERT OVERWRITE TABLE auction_es
select
status,
cast(auctionCount as int),
cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
addr,
addr0,
addr1,
addr2,
addr3,
court,
courtCode,
cast(itemNo as int),
remark,
caNo,
cast(pyeong  as int),
cast(land1  as float),
cast(land2  as float),
cast(floor1  as float),
cast(floor2 as float),
auctionInfo,
itemType,
cast(appraisedValue as bigint),
cast(minValue  as bigint),
cast(regexp_replace(saleValue, ',','') as bigint),
cast(saleRate as int),
cast(saleCount as int)
from ctauinfo
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:status, type:string, comment:null), FieldSchema(name:auctioncount, type:int, comment:null), FieldSchema(name:_c2, type:timestamp, comment:null), FieldSchema(name:addr, type:string, comment:null), FieldSchema(name:addr0, type:string, comment:null), FieldSchema(name:addr1, type:string, comment:null), FieldSchema(name:addr2, type:string, comment:null), FieldSchema(name:addr3, type:string, comment:null), FieldSchema(name:court, type:string, comment:null), FieldSchema(name:courtcode, type:string, comment:null), FieldSchema(name:itemno, type:int, comment:null), FieldSchema(name:remark, type:string, comment:null), FieldSchema(name:cano, type:string, comment:null), FieldSchema(name:pyeong, type:int, comment:null), FieldSchema(name:land1, type:float, comment:null), FieldSchema(name:land2, type:float, comment:null), FieldSchema(name:floor1, type:float, comment:null), FieldSchema(name:floor2, type:float, comment:null), FieldSchema(name:auctioninfo, type:string, comment:null), FieldSchema(name:itemtype, type:string, comment:null), FieldSchema(name:appraisedvalue, type:bigint, comment:null), FieldSchema(name:minvalue, type:bigint, comment:null), FieldSchema(name:_c22, type:bigint, comment:null), FieldSchema(name:salerate, type:int, comment:null), FieldSchema(name:salecount, type:int, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424203636_5b7587ff-ed1c-4aa4-9506-c57a7174f11f); Time taken: 0.157 seconds
INFO  : Executing command(queryId=hive_20180424203636_5b7587ff-ed1c-4aa4-9506-c57a7174f11f): INSERT OVERWRITE TABLE auction_es
select
status,
cast(auctionCount as int),
cast(case when length(auctionDate) > 10 then substr(auctionDate,length(auctionDate)-9) else auctionDate end  as timestamp),
addr,
addr0,
addr1,
addr2,
addr3,
court,
courtCode,
cast(itemNo as int),
remark,
caNo,
cast(pyeong  as int),
cast(land1  as float),
cast(land2  as float),
cast(floor1  as float),
cast(floor2 as float),
auctionInfo,
itemType,
cast(appraisedValue as bigint),
cast(minValue  as bigint),
cast(regexp_replace(saleValue, ',','') as bigint),
cast(saleRate as int),
cast(saleCount as int)
from ctauinfo
INFO  : Query ID = hive_20180424203636_5b7587ff-ed1c-4aa4-9506-c57a7174f11f
INFO  : Total jobs = 1
INFO  : Launching Job 1 out of 1
INFO  : Starting task [Stage-0:MAPRED] in serial mode
INFO  : Number of reduce tasks is set to 0 since there's no reduce operator
INFO  : number of splits:1
INFO  : Submitting tokens for job: job_1523845385074_0068
INFO  : The url to track the job: http://nn01:8088/proxy/application_1523845385074_0068/
INFO  : Starting Job = job_1523845385074_0068, Tracking URL = http://nn01:8088/proxy/application_1523845385074_0068/
INFO  : Kill Command = /opt/cloudera/parcels/CDH-5.14.2-1.cdh5.14.2.p0.3/lib/hadoop/bin/hadoop job  -kill job_1523845385074_0068
INFO  : Hadoop job information for Stage-0: number of mappers: 1; number of reducers: 0
INFO  : 2018-04-24 20:37:06,539 Stage-0 map = 0%,  reduce = 0%
INFO  : 2018-04-24 20:37:23,773 Stage-0 map = 26%,  reduce = 0%, Cumulative CPU 13.66 sec
INFO  : 2018-04-24 20:37:29,124 Stage-0 map = 44%,  reduce = 0%, Cumulative CPU 17.37 sec
INFO  : 2018-04-24 20:37:35,530 Stage-0 map = 63%,  reduce = 0%, Cumulative CPU 21.11 sec
INFO  : 2018-04-24 20:37:41,941 Stage-0 map = 81%,  reduce = 0%, Cumulative CPU 24.78 sec
INFO  : 2018-04-24 20:37:47,279 Stage-0 map = 96%,  reduce = 0%, Cumulative CPU 28.43 sec
INFO  : 2018-04-24 20:37:48,350 Stage-0 map = 100%,  reduce = 0%, Cumulative CPU 28.62 sec
INFO  : MapReduce Total cumulative CPU time: 28 seconds 620 msec
INFO  : Ended Job = job_1523845385074_0068
INFO  : MapReduce Jobs Launched:
INFO  : Stage-Stage-0: Map: 1   Cumulative CPU: 28.62 sec   HDFS Read: 141856578 HDFS Write: 0 SUCCESS
INFO  : Total MapReduce CPU Time Spent: 28 seconds 620 msec
INFO  : Completed executing command(queryId=hive_20180424203636_5b7587ff-ed1c-4aa4-9506-c57a7174f11f); Time taken: 49.646 seconds
INFO  : OK
No rows affected (49.895 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> select status, addr, cano from auction_es limit 10;
INFO  : Compiling command(queryId=hive_20180424203838_8c92fe0d-c0ac-4187-8ef0-e0137395204d): select status, addr, cano from auction_es limit 10
INFO  : Semantic Analysis Completed
INFO  : Returning Hive schema: Schema(fieldSchemas:[FieldSchema(name:status, type:string, comment:null), FieldSchema(name:addr, type:string, comment:null), FieldSchema(name:cano, type:string, comment:null)], properties:null)
INFO  : Completed compiling command(queryId=hive_20180424203838_8c92fe0d-c0ac-4187-8ef0-e0137395204d); Time taken: 0.096 seconds
INFO  : Executing command(queryId=hive_20180424203838_8c92fe0d-c0ac-4187-8ef0-e0137395204d): select status, addr, cano from auction_es limit 10
INFO  : Completed executing command(queryId=hive_20180424203838_8c92fe0d-c0ac-4187-8ef0-e0137395204d); Time taken: 0.002 seconds
INFO  : OK
+---------+--------------------------------------------------+--------------+--+
| status  |                       addr                       |     cano     |
+---------+--------------------------------------------------+--------------+--+
| 배당종결    | 경상남도 창녕군 남지읍 남지리 293-1 푸른마을아파트 나동 9층 1008호       | 2007타경7169   |
| 배당종결    | 경상남도 밀양시 교동 1225 아침해오름아파트 101동 5층 503호           | 2008타경1502   |
| 취하      | 경상남도 진주시 칠암동 277 현대아파트 나동 1층 101호                | 2008타경16614  |
| 배당종결    | 광주광역시 북구 동림동 1147-1 동림푸른마을주공3단지아파트 301동 4층 403호  | 2008타경45154  |
| 취하      | 광주광역시 광산구 도산동 1136-1 호반아파트 101동 12층 1203호        | 2008타경45307  |
| 배당종결    | 전라북도 진안군 진안읍 군상리 200-1 고향마을아파트 105동 11층 1106호    | 2008타경9384   |
| 배당종결    | 광주광역시 서구 풍암동 1096 현대삼환아파트 105동 1층 105호           | 2008타경47778  |
| 배당종결    | 전라북도 김제시 만경읍 몽산리 79-4 만경영광아파트 101동 7층 702호       | 2008타경11097  |
| 배당종결    | 광주광역시 동구 용산동 147-1 호반아파트 13층 1413호               | 2008타경48245  |
| 배당종결    | 전라북도 김제시 만경읍 몽산리 79-4 만경영광아파트 102동 3층 302호       | 2008타경11097  |
+---------+--------------------------------------------------+--------------+--+
10 rows selected (0.352 seconds)
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> !list
1 active connection:
 #0  open     jdbc:hive2://dn02:10000
0: jdbc:hive2://dn02:10000>
0: jdbc:hive2://dn02:10000> 
0: jdbc:hive2://dn02:10000> !quit
Closing: 0: jdbc:hive2://dn02:10000
[eduuser@dn01 dist]$
~~~


### 참고
---
[Apache Hive integrationedit
](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/hive.html)  
[ES-Hadoop](https://www.elastic.co/kr/downloads/hadoop)

