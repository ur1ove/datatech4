[cloudera@quickstart Downloads]$ ls
~~~
Log Files.zip
~~~
[cloudera@quickstart Downloads]$ unzip Log\ Files.zip 
~~~
Archive:  Log Files.zip
   creating: Log Files/
  inflating: Log Files/log_2012613_161117.log  
  inflating: Log Files/log_2013711_155354.log  
  inflating: Log Files/log_2013720_162256.log  
  inflating: Log Files/log_2013803_15590.log  
  inflating: Log Files/log_2013805_16210.log  
  inflating: Log Files/log_2013811_16136.log  
~~~
[cloudera@quickstart Downloads]$ cd Log\ Files
~~~
[cloudera@quickstart Log Files]$ ls
log_2012613_161117.log  log_2013720_162256.log  log_2013805_16210.log
log_2013711_155354.log  log_2013803_15590.log   log_2013811_16136.log
~~~
[cloudera@quickstart Log Files]$ ls -al
~~~
total 4084
drwxrwxr-x 2 cloudera cloudera    4096 Dec 18  2015 .
drwxr-xr-x 3 cloudera cloudera    4096 Apr  1 21:02 ..
-rw-rw-r-- 1 cloudera cloudera  151325 Aug 11  2013 log_2012613_161117.log
-rw-rw-r-- 1 cloudera cloudera  742440 Aug 11  2013 log_2013711_155354.log
-rw-rw-r-- 1 cloudera cloudera  457917 Aug 11  2013 log_2013720_162256.log
-rw-rw-r-- 1 cloudera cloudera  744458 Aug 11  2013 log_2013803_15590.log
-rw-rw-r-- 1 cloudera cloudera 1305943 Aug 11  2013 log_2013805_16210.log
-rw-rw-r-- 1 cloudera cloudera  764624 Aug 11  2013 log_2013811_16136.log
~~~
[cloudera@quickstart Log Files]$ hdfs dfs -mkdir -p /user/cloudera/logs/pv_ext/2012/06/13/log/data   
[cloudera@quickstart Log Files]$ hdfs dfs -put log_2012613_161117.log logs/pv_ext/2012/06/13/log/data  
[cloudera@quickstart Log Files]$ hdfs dfs -ls logs/pv_ext/2012/06/13/log/data  
~~~
Found 1 items
-rw-r--r--   1 cloudera cloudera     151325 2018-04-01 21:08 logs/pv_ext/2012/06/13/log/data/log_2012613_161117.log
~~~
[cloudera@quickstart Log Files]$ hive
~~~
Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j.properties
WARNING: Hive CLI is deprecated and migration to Beeline is recommended.
hive> 
~~~
~~~
hive> set hive.cli.print.current.db=true  
    > ;  
hive (default)> use hivedemo;
OK
Time taken: 0.399 seconds
hive (hivedemo)> CREATE EXTERNAL TABLE page_views_ext (logtime STRING, userid INT, ip STRING, page STRING, ref STRING, os STRING, os_ver STRING, agent STRING)
               > ROW FORMAT DELIMITED
               > FIELDS TERMINATED BY '\t'
               > LOCATION '/user/cloudera/logs/pv_ext/';
OK
Time taken: 0.329 seconds
hive (hivedemo)> describe formatted page_views_ext;
OK
# col_name              data_type               comment             
                 
logtime                 string                                      
userid                  int                                         
ip                      string                                      
page                    string                                      
ref                     string                                      
os                      string                                      
os_ver                  string                                      
agent                   string                                      
                 
# Detailed Table Information             
Database:               hivedemo                 
Owner:                  cloudera                 
CreateTime:             Sun Apr 01 21:15:14 PDT 2018     
LastAccessTime:         UNKNOWN                  
Protect Mode:           None                     
Retention:              0                        
Location:               hdfs://quickstart.cloudera:8020/user/cloudera/logs/pv_ext      
Table Type:             EXTERNAL_TABLE           
Table Parameters:                
        COLUMN_STATS_ACCURATE   false               
        EXTERNAL                TRUE                
        numFiles                1                   
        numRows                 -1                  
        rawDataSize             -1                  
        totalSize               151325              
        transient_lastDdlTime   1522642514          
                 
# Storage Information            
SerDe Library:          org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe       
InputFormat:            org.apache.hadoop.mapred.TextInputFormat         
OutputFormat:           org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat     
Compressed:             No                       
Num Buckets:            -1                       
Bucket Columns:         []                       
Sort Columns:           []                       
Storage Desc Params:             
        field.delim             \t                  
        serialization.format    \t                  
Time taken: 0.245 seconds, Fetched: 40 row(s)
hive (hivedemo)> 
~~~
~~~
hive (hivedemo)> EXPLAIN SELECT * FROM page_views_ext WHERE userid = 13;
OK
STAGE DEPENDENCIES:
  Stage-0 is a root stage

STAGE PLANS:
  Stage: Stage-0
    Fetch Operator
      limit: -1
      Processor Tree:
        TableScan
          alias: page_views_ext
          Statistics: Num rows: 214 Data size: 151325 Basic stats: COMPLETE Column stats: NONE
          Filter Operator
            predicate: (userid = 13) (type: boolean)
            Statistics: Num rows: 107 Data size: 75662 Basic stats: COMPLETE Column stats: NONE
            Select Operator
              expressions: logtime (type: string), 13 (type: int), ip (type: string), page (type: string), ref (type: string), os (type: string), os_ver (type: string), agent (type: string)
              outputColumnNames: _col0, _col1, _col2, _col3, _col4, _col5, _col6, _col7
              Statistics: Num rows: 107 Data size: 75662 Basic stats: COMPLETE Column stats: NONE
              ListSink

Time taken: 0.572 seconds, Fetched: 20 row(s)
hive (hivedemo)> drop table page_views_ext;
OK
Time taken: 0.804 seconds
hive (hivedemo)> show tables;
OK
orders
orders_no_partition
Time taken: 0.076 seconds, Fetched: 2 row(s)
hive (hivedemo)> 
~~~
