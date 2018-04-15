## Elastic Stack  
  
1) Elasticsearch 6.2.3 설치  
  
[esadmin@dn01 ~]$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.zip  
~~~
--2018-04-14 09:47:26--  https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.zip
Resolving artifacts.elastic.co (artifacts.elastic.co)... 184.72.242.47, 54.235.82.130, 23.23.109.100, ...
Connecting to artifacts.elastic.co (artifacts.elastic.co)|184.72.242.47|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 29091467 (28M) [application/zip]
Saving to: ‘elasticsearch-6.2.3.zip’

100%[=================================================================================>] 29,091,467   177KB/s   in 3m 11s 

2018-04-14 09:50:40 (148 KB/s) - ‘elasticsearch-6.2.3.zip’ saved [29091467/29091467]
~~~
[esadmin@dn01 ~]$ unzip elasticsearch-6.2.3.zip  
~~~
Archive:  elasticsearch-6.2.3.zip
   creating: elasticsearch-6.2.3/
   creating: elasticsearch-6.2.3/lib/
  inflating: elasticsearch-6.2.3/lib/elasticsearch-6.2.3.jar  
  inflating: elasticsearch-6.2.3/lib/elasticsearch-core-6.2.3.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-core-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-analyzers-common-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-backward-codecs-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-grouping-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-highlighter-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-join-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-memory-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-misc-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-queries-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-queryparser-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-sandbox-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-spatial-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-spatial-extras-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-spatial3d-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/lucene-suggest-7.2.1.jar  
  inflating: elasticsearch-6.2.3/lib/securesm-1.2.jar  
  inflating: elasticsearch-6.2.3/lib/hppc-0.7.1.jar  
  inflating: elasticsearch-6.2.3/lib/joda-time-2.9.9.jar  
  inflating: elasticsearch-6.2.3/lib/snakeyaml-1.17.jar  
  inflating: elasticsearch-6.2.3/lib/jackson-core-2.8.10.jar  
  inflating: elasticsearch-6.2.3/lib/jackson-dataformat-smile-2.8.10.jar  
  inflating: elasticsearch-6.2.3/lib/jackson-dataformat-yaml-2.8.10.jar  
  inflating: elasticsearch-6.2.3/lib/jackson-dataformat-cbor-2.8.10.jar  
  inflating: elasticsearch-6.2.3/lib/t-digest-3.0.jar  
  inflating: elasticsearch-6.2.3/lib/HdrHistogram-2.1.9.jar  
  inflating: elasticsearch-6.2.3/lib/spatial4j-0.6.jar  
  inflating: elasticsearch-6.2.3/lib/jts-1.13.jar  
  inflating: elasticsearch-6.2.3/lib/log4j-api-2.9.1.jar  
  inflating: elasticsearch-6.2.3/lib/log4j-core-2.9.1.jar  
  inflating: elasticsearch-6.2.3/lib/log4j-1.2-api-2.9.1.jar  
  inflating: elasticsearch-6.2.3/lib/jna-4.5.1.jar  
  inflating: elasticsearch-6.2.3/lib/elasticsearch-cli-6.2.3.jar  
  inflating: elasticsearch-6.2.3/lib/jopt-simple-5.0.2.jar  
  inflating: elasticsearch-6.2.3/lib/plugin-classloader-6.2.3.jar  
  inflating: elasticsearch-6.2.3/lib/elasticsearch-launchers-6.2.3.jar  
  inflating: elasticsearch-6.2.3/lib/plugin-cli-6.2.3.jar  
   creating: elasticsearch-6.2.3/config/
  inflating: elasticsearch-6.2.3/config/jvm.options  
  inflating: elasticsearch-6.2.3/config/elasticsearch.yml  
  inflating: elasticsearch-6.2.3/config/log4j2.properties  
   creating: elasticsearch-6.2.3/bin/
  inflating: elasticsearch-6.2.3/bin/elasticsearch  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-env  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-plugin  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-translog  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-keystore  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-plugin.bat  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-env.bat  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-keystore.bat  
  inflating: elasticsearch-6.2.3/bin/elasticsearch.bat  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-service.bat  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-translog.bat  
  inflating: elasticsearch-6.2.3/LICENSE.txt  
  inflating: elasticsearch-6.2.3/README.textile  
  inflating: elasticsearch-6.2.3/NOTICE.txt  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-service-x64.exe  
  inflating: elasticsearch-6.2.3/bin/elasticsearch-service-mgr.exe  
   creating: elasticsearch-6.2.3/modules/
   creating: elasticsearch-6.2.3/modules/parent-join/
  inflating: elasticsearch-6.2.3/modules/parent-join/parent-join-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/parent-join/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/tribe/
  inflating: elasticsearch-6.2.3/modules/tribe/plugin-descriptor.properties  
  inflating: elasticsearch-6.2.3/modules/tribe/tribe-6.2.3.jar  
   creating: elasticsearch-6.2.3/modules/transport-netty4/
  inflating: elasticsearch-6.2.3/modules/transport-netty4/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-handler-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-transport-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-resolver-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/transport-netty4-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-codec-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-common-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-buffer-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/netty-codec-http-4.1.16.Final.jar  
  inflating: elasticsearch-6.2.3/modules/transport-netty4/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/rank-eval/
  inflating: elasticsearch-6.2.3/modules/rank-eval/plugin-descriptor.properties  
  inflating: elasticsearch-6.2.3/modules/rank-eval/rank-eval-6.2.3.jar  
   creating: elasticsearch-6.2.3/modules/lang-expression/
  inflating: elasticsearch-6.2.3/modules/lang-expression/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/lang-expression/asm-5.0.4.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/asm-commons-5.0.4.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/lang-expression-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/antlr4-runtime-4.5.1-1.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/asm-tree-5.0.4.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/lucene-expressions-7.2.1.jar  
  inflating: elasticsearch-6.2.3/modules/lang-expression/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/percolator/
  inflating: elasticsearch-6.2.3/modules/percolator/percolator-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/percolator/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/aggs-matrix-stats/
  inflating: elasticsearch-6.2.3/modules/aggs-matrix-stats/aggs-matrix-stats-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/aggs-matrix-stats/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/reindex/
  inflating: elasticsearch-6.2.3/modules/reindex/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/reindex/commons-logging-1.1.3.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/httpasyncclient-4.1.2.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/httpcore-nio-4.4.5.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/elasticsearch-rest-client-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/httpcore-4.4.5.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/commons-codec-1.10.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/plugin-descriptor.properties  
  inflating: elasticsearch-6.2.3/modules/reindex/httpclient-4.5.2.jar  
  inflating: elasticsearch-6.2.3/modules/reindex/reindex-6.2.3.jar  
   creating: elasticsearch-6.2.3/modules/analysis-common/
  inflating: elasticsearch-6.2.3/modules/analysis-common/analysis-common-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/analysis-common/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/mapper-extras/
  inflating: elasticsearch-6.2.3/modules/mapper-extras/mapper-extras-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/mapper-extras/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/lang-painless/
  inflating: elasticsearch-6.2.3/modules/lang-painless/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/lang-painless/elasticsearch-scripting-painless-spi-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/lang-painless/asm-debug-all-5.1.jar  
  inflating: elasticsearch-6.2.3/modules/lang-painless/plugin-descriptor.properties  
  inflating: elasticsearch-6.2.3/modules/lang-painless/antlr4-runtime-4.5.3.jar  
  inflating: elasticsearch-6.2.3/modules/lang-painless/lang-painless-6.2.3.jar  
   creating: elasticsearch-6.2.3/modules/lang-mustache/
  inflating: elasticsearch-6.2.3/modules/lang-mustache/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/lang-mustache/compiler-0.9.3.jar  
  inflating: elasticsearch-6.2.3/modules/lang-mustache/lang-mustache-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/lang-mustache/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/ingest-common/
  inflating: elasticsearch-6.2.3/modules/ingest-common/jcodings-1.0.12.jar  
  inflating: elasticsearch-6.2.3/modules/ingest-common/ingest-common-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/ingest-common/joni-2.1.6.jar  
  inflating: elasticsearch-6.2.3/modules/ingest-common/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/modules/repository-url/
  inflating: elasticsearch-6.2.3/modules/repository-url/plugin-security.policy  
  inflating: elasticsearch-6.2.3/modules/repository-url/repository-url-6.2.3.jar  
  inflating: elasticsearch-6.2.3/modules/repository-url/plugin-descriptor.properties  
   creating: elasticsearch-6.2.3/logs/
   creating: elasticsearch-6.2.3/plugins/
~~~
~~~
[esadmin@dn01 ~]$ cp -R elasticsearch-6.2.3 node1
[esadmin@dn01 ~]$ cp -R elasticsearch-6.2.3 node2
[esadmin@dn01 ~]$ cp -R elasticsearch-6.2.3 node3
[esadmin@dn01 ~]$ ls -al
total 28436
drwx------  9 esadmin esadmin     4096 Apr 15 04:42 .
drwxr-xr-x. 6 root    root          62 Apr 14 09:41 ..
-rw-------  1 esadmin esadmin      191 Apr 15 04:27 .bash_history
-rw-r--r--  1 esadmin esadmin       18 Jun 10  2014 .bash_logout
-rw-r--r--  1 esadmin esadmin      193 Jun 10  2014 .bash_profile
-rw-r--r--  1 esadmin esadmin      231 Jun 10  2014 .bashrc
drwxrwxr-x  3 esadmin esadmin       17 Apr 14 09:43 .cache
drwxrwxr-x  3 esadmin esadmin       17 Apr 14 09:43 .config
drwxr-xr-x  8 esadmin esadmin      134 Mar 13 10:08 elasticsearch-6.2.3
-rw-rw-r--  1 esadmin esadmin 29091467 Mar 20 10:31 elasticsearch-6.2.3.zip
drwxr-xr-x  4 esadmin esadmin       37 Feb 26  2017 .mozilla
drwxr-xr-x  8 esadmin esadmin      134 Apr 15 04:42 node1
drwxr-xr-x  8 esadmin esadmin      134 Apr 15 04:42 node2
drwxr-xr-x  8 esadmin esadmin      134 Apr 15 04:42 node3
-rw-------  1 esadmin esadmin      742 Apr 15 04:42 .viminfo
~~~
