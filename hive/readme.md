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
[cloudera@quickstart Log Files]$  
