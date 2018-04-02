[vagrant@nn01 ~]$ sudo vi /etc/hosts
~~~
#127.0.0.1      dn01    dn01 <-삭제
#127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 <-주석풀기
#::1         localhost localhost.localdomain localhost6 localhost6.localdomain6 <-주석풀기
192.168.56.100 nn01
192.168.56.101 dn01
192.168.56.102 dn02
~~~
~~~
[vagrant@nn01 ~]$ ssh vagrant@dn01
Last login: Mon Apr  2 07:03:40 2018 from 192.168.56.100
[vagrant@dn01 ~]$ sudo vi /etc/hosts
[vagrant@dn01 ~]$ exit
logout
Connection to dn01 closed.
[vagrant@nn01 ~]$ ssh vagrant@dn02
Last login: Mon Apr  2 06:52:58 2018 from 192.168.56.100
[vagrant@dn02 ~]$ sudo vi /etc/hosts
[vagrant@dn02 ~]$ exit
logout
Connection to dn02 closed.
[vagrant@nn01 ~]$ 
~~~
[vagrant@nn01 ~]$ hdfs namenode -format
~~~
18/04/02 07:08:48 INFO namenode.NameNode: STARTUP_MSG: 
/************************************************************
STARTUP_MSG: Starting NameNode
STARTUP_MSG:   user = vagrant
STARTUP_MSG:   host = nn01/192.168.56.100
STARTUP_MSG:   args = [-format]
STARTUP_MSG:   version = 2.8.3
STARTUP_MSG:   classpath = /opt/hadoop/current/etc/hadoop:/opt/hadoop/2.8.3/share/hadoop/common/lib/activation-1.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/apacheds-i18n-2.0.0-M15.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/apacheds-kerberos-codec-2.0.0-M15.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/api-asn1-api-1.0.0-M20.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/api-util-1.0.0-M20.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/asm-3.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/avro-1.7.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-beanutils-1.7.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-beanutils-core-1.8.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-cli-1.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-codec-1.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-collections-3.2.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-compress-1.4.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-configuration-1.6.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-digester-1.8.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-io-2.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-lang-2.6.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-logging-1.1.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-math3-3.1.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/commons-net-3.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/curator-client-2.7.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/curator-framework-2.7.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/curator-recipes-2.7.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/gson-2.2.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/guava-11.0.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/hadoop-annotations-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/hadoop-auth-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/hamcrest-core-1.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/htrace-core4-4.0.1-incubating.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/httpclient-4.5.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/httpcore-4.4.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jackson-core-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jackson-jaxrs-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jackson-mapper-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jackson-xc-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/java-xmlbuilder-0.4.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jaxb-api-2.2.2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jaxb-impl-2.2.3-1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jcip-annotations-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jersey-core-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jersey-json-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jersey-server-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jets3t-0.9.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jettison-1.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jetty-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jetty-sslengine-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jetty-util-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jsch-0.1.54.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/json-smart-1.1.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jsp-api-2.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/jsr305-3.0.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/junit-4.11.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/log4j-1.2.17.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/mockito-all-1.8.5.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/netty-3.6.2.Final.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/nimbus-jose-jwt-3.9.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/paranamer-2.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/protobuf-java-2.5.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/servlet-api-2.5.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/slf4j-api-1.7.10.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/slf4j-log4j12-1.7.10.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/snappy-java-1.0.4.1.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/stax-api-1.0-2.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/xmlenc-0.52.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/xz-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/common/lib/zookeeper-3.4.6.jar:/opt/hadoop/2.8.3/share/hadoop/common/hadoop-common-2.8.3-tests.jar:/opt/hadoop/2.8.3/share/hadoop/common/hadoop-common-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/common/hadoop-nfs-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/asm-3.2.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-cli-1.2.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-codec-1.4.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-daemon-1.0.13.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-io-2.4.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-lang-2.6.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/commons-logging-1.1.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/guava-11.0.2.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/hadoop-hdfs-client-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/htrace-core4-4.0.1-incubating.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jackson-core-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jackson-mapper-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jersey-core-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jersey-server-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jetty-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jetty-util-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/jsr305-3.0.0.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/leveldbjni-all-1.8.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/log4j-1.2.17.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/netty-3.6.2.Final.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/netty-all-4.0.23.Final.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/okhttp-2.4.0.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/okio-1.4.0.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/protobuf-java-2.5.0.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/servlet-api-2.5.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/xercesImpl-2.9.1.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/xml-apis-1.3.04.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/lib/xmlenc-0.52.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-2.8.3-tests.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-client-2.8.3-tests.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-client-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-native-client-2.8.3-tests.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-native-client-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/hdfs/hadoop-hdfs-nfs-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/activation-1.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/aopalliance-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/asm-3.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-cli-1.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-codec-1.4.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-collections-3.2.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-compress-1.4.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-io-2.4.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-lang-2.6.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-logging-1.1.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/commons-math-2.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/curator-client-2.7.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/curator-test-2.7.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/fst-2.50.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/guava-11.0.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/guice-3.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/guice-servlet-3.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jackson-core-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jackson-jaxrs-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jackson-mapper-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jackson-xc-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/java-util-1.9.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/javassist-3.18.1-GA.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/javax.inject-1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jaxb-api-2.2.2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jaxb-impl-2.2.3-1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jersey-client-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jersey-core-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jersey-guice-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jersey-json-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jersey-server-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jettison-1.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jetty-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jetty-util-6.1.26.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/json-io-2.5.1.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/jsr305-3.0.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/leveldbjni-all-1.8.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/log4j-1.2.17.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/netty-3.6.2.Final.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/protobuf-java-2.5.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/servlet-api-2.5.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/stax-api-1.0-2.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/xz-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/zookeeper-3.4.6-tests.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/lib/zookeeper-3.4.6.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-api-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-applications-distributedshell-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-applications-unmanaged-am-launcher-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-client-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-common-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-registry-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-applicationhistoryservice-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-common-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-nodemanager-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-resourcemanager-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-sharedcachemanager-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-tests-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-timeline-pluginstorage-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/yarn/hadoop-yarn-server-web-proxy-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/aopalliance-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/asm-3.2.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/avro-1.7.4.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/commons-compress-1.4.1.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/commons-io-2.4.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/guice-3.0.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/guice-servlet-3.0.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/hadoop-annotations-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/hamcrest-core-1.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/jackson-core-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/jackson-mapper-asl-1.9.13.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/javax.inject-1.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/jersey-core-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/jersey-guice-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/jersey-server-1.9.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/junit-4.11.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/leveldbjni-all-1.8.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/log4j-1.2.17.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/netty-3.6.2.Final.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/paranamer-2.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/protobuf-java-2.5.0.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/snappy-java-1.0.4.1.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/lib/xz-1.0.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-app-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-common-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-hs-plugins-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.8.3-tests.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-jobclient-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-client-shuffle-2.8.3.jar:/opt/hadoop/2.8.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.3.jar:/opt/hive/current/lib/*.jar:/opt/hadoop/current/lib/*.jar:/opt/hadoop/current/share/hadoop/common/*.jar:/opt/hadoop/current/share/hadoop/hdfs/*.jar:/opt/hadoop/current/share/hadoop/mapreduce/*.jar:/opt/hadoop/current/share/hadoop/yarn/*.jar:/opt/jdk/current/lib/*.jar:/opt/sqoop/current/lib/*.jar:/opt/sqoop/current/*.jar:/opt/hadoop/current/share/hadoop/tools/lib/*.jar:/opt/hadoop/current/contrib/capacity-scheduler/*.jar
STARTUP_MSG:   build = https://git-wip-us.apache.org/repos/asf/hadoop.git -r b3fe56402d908019d99af1f1f4fc65cb1d1436a2; compiled by 'jdu' on 2017-12-05T03:43Z
STARTUP_MSG:   java = 1.8.0_161
************************************************************/
18/04/02 07:08:48 INFO namenode.NameNode: registered UNIX signal handlers for [TERM, HUP, INT]
18/04/02 07:08:48 INFO namenode.NameNode: createNameNode [-format]
Formatting using clusterid: CID-fc2fe079-0e3f-4c33-987a-7b2218e4ae11
18/04/02 07:08:49 INFO namenode.FSEditLog: Edit logging is async:true
18/04/02 07:08:49 INFO namenode.FSNamesystem: KeyProvider: null
18/04/02 07:08:49 INFO namenode.FSNamesystem: fsLock is fair: true
18/04/02 07:08:49 INFO namenode.FSNamesystem: Detailed lock hold time metrics enabled: false
18/04/02 07:08:49 INFO blockmanagement.DatanodeManager: dfs.block.invalidate.limit=1000
18/04/02 07:08:49 INFO blockmanagement.DatanodeManager: dfs.namenode.datanode.registration.ip-hostname-check=true
18/04/02 07:08:49 INFO blockmanagement.BlockManager: dfs.namenode.startup.delay.block.deletion.sec is set to 000:00:00:00.000
18/04/02 07:08:49 INFO blockmanagement.BlockManager: The block deletion will start around 2018 Apr 02 07:08:49
18/04/02 07:08:49 INFO util.GSet: Computing capacity for map BlocksMap
18/04/02 07:08:49 INFO util.GSet: VM type       = 64-bit
18/04/02 07:08:49 INFO util.GSet: 2.0% max memory 966.7 MB = 19.3 MB
18/04/02 07:08:49 INFO util.GSet: capacity      = 2^21 = 2097152 entries
18/04/02 07:08:49 INFO blockmanagement.BlockManager: dfs.block.access.token.enable=false
18/04/02 07:08:49 INFO blockmanagement.BlockManager: defaultReplication         = 1
18/04/02 07:08:49 INFO blockmanagement.BlockManager: maxReplication             = 512
18/04/02 07:08:49 INFO blockmanagement.BlockManager: minReplication             = 1
18/04/02 07:08:49 INFO blockmanagement.BlockManager: maxReplicationStreams      = 2
18/04/02 07:08:49 INFO blockmanagement.BlockManager: replicationRecheckInterval = 3000
18/04/02 07:08:49 INFO blockmanagement.BlockManager: encryptDataTransfer        = false
18/04/02 07:08:49 INFO blockmanagement.BlockManager: maxNumBlocksToLog          = 1000
18/04/02 07:08:49 INFO namenode.FSNamesystem: fsOwner             = vagrant (auth:SIMPLE)
18/04/02 07:08:49 INFO namenode.FSNamesystem: supergroup          = supergroup
18/04/02 07:08:49 INFO namenode.FSNamesystem: isPermissionEnabled = true
18/04/02 07:08:49 INFO namenode.FSNamesystem: HA Enabled: false
18/04/02 07:08:49 INFO namenode.FSNamesystem: Append Enabled: true
18/04/02 07:08:49 INFO util.GSet: Computing capacity for map INodeMap
18/04/02 07:08:49 INFO util.GSet: VM type       = 64-bit
18/04/02 07:08:49 INFO util.GSet: 1.0% max memory 966.7 MB = 9.7 MB
18/04/02 07:08:49 INFO util.GSet: capacity      = 2^20 = 1048576 entries
18/04/02 07:08:49 INFO namenode.FSDirectory: ACLs enabled? false
18/04/02 07:08:49 INFO namenode.FSDirectory: XAttrs enabled? true
18/04/02 07:08:49 INFO namenode.NameNode: Caching file names occurring more than 10 times
18/04/02 07:08:49 INFO util.GSet: Computing capacity for map cachedBlocks
18/04/02 07:08:49 INFO util.GSet: VM type       = 64-bit
18/04/02 07:08:49 INFO util.GSet: 0.25% max memory 966.7 MB = 2.4 MB
18/04/02 07:08:49 INFO util.GSet: capacity      = 2^18 = 262144 entries
18/04/02 07:08:49 INFO namenode.FSNamesystem: dfs.namenode.safemode.threshold-pct = 0.9990000128746033
18/04/02 07:08:49 INFO namenode.FSNamesystem: dfs.namenode.safemode.min.datanodes = 0
18/04/02 07:08:49 INFO namenode.FSNamesystem: dfs.namenode.safemode.extension     = 30000
18/04/02 07:08:49 INFO metrics.TopMetrics: NNTop conf: dfs.namenode.top.window.num.buckets = 10
18/04/02 07:08:49 INFO metrics.TopMetrics: NNTop conf: dfs.namenode.top.num.users = 10
18/04/02 07:08:49 INFO metrics.TopMetrics: NNTop conf: dfs.namenode.top.windows.minutes = 1,5,25
18/04/02 07:08:49 INFO namenode.FSNamesystem: Retry cache on namenode is enabled
18/04/02 07:08:49 INFO namenode.FSNamesystem: Retry cache will use 0.03 of total heap and retry cache entry expiry time is 600000 millis
18/04/02 07:08:49 INFO util.GSet: Computing capacity for map NameNodeRetryCache
18/04/02 07:08:49 INFO util.GSet: VM type       = 64-bit
18/04/02 07:08:49 INFO util.GSet: 0.029999999329447746% max memory 966.7 MB = 297.0 KB
18/04/02 07:08:49 INFO util.GSet: capacity      = 2^15 = 32768 entries
Re-format filesystem in Storage Directory /var/hadoop/hadoop-namenode ? (Y or N) Y
18/04/02 07:08:58 INFO namenode.FSImage: Allocated new BlockPoolId: BP-125821281-192.168.56.100-1522652938164
18/04/02 07:08:58 INFO common.Storage: Storage directory /var/hadoop/hadoop-namenode has been successfully formatted.
18/04/02 07:08:58 INFO namenode.FSImageFormatProtobuf: Saving image file /var/hadoop/hadoop-namenode/current/fsimage.ckpt_0000000000000000000 using no compression
18/04/02 07:08:58 INFO namenode.FSImageFormatProtobuf: Image file /var/hadoop/hadoop-namenode/current/fsimage.ckpt_0000000000000000000 of size 324 bytes saved in 0 seconds.
18/04/02 07:08:58 INFO namenode.NNStorageRetentionManager: Going to retain 1 images with txid >= 0
18/04/02 07:08:58 INFO util.ExitUtil: Exiting with status 0
18/04/02 07:08:58 INFO namenode.NameNode: SHUTDOWN_MSG: 
/************************************************************
SHUTDOWN_MSG: Shutting down NameNode at nn01/192.168.56.100
************************************************************/
~~~
[vagrant@nn01 ~]$ start-all.sh                                    
~~~
This script is Deprecated. Instead use start-dfs.sh and start-yarn.sh
Starting namenodes on [nn01]
nn01: starting namenode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-namenode-nn01.out
dn01: starting datanode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-datanode-dn01.out
dn02: starting datanode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-datanode-dn02.out
Starting secondary namenodes [nn01]
nn01: starting secondarynamenode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-secondarynamenode-nn01.out
starting yarn daemons
starting resourcemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-resourcemanager-nn01.out
dn01: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn01.out
dn02: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn02.out
[vagrant@nn01 ~]$ 
~~~
