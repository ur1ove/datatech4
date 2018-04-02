[vagrant@nn01 ~]$ start-all.sh
~~~
This script is Deprecated. Instead use start-dfs.sh and start-yarn.sh
Starting namenodes on [nn01]
nn01: starting namenode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-namenode-nn01.out
dn02: starting datanode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-datanode-dn02.out
dn01: starting datanode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-datanode-dn01.out
Starting secondary namenodes [nn01]
nn01: starting secondarynamenode, logging to /opt/hadoop/2.8.3/logs/hadoop-vagrant-secondarynamenode-nn01.out
starting yarn daemons
starting resourcemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-resourcemanager-nn01.out
dn02: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn02.out
dn01: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn01.out
[vagrant@nn01 ~]$ 
~~~
[vagrant@nn01 ~]$ jps
~~~
3251 ResourceManager
2902 NameNode
3098 SecondaryNameNode
3515 Jps
~~~
[vagrant@nn01 ~]$ ssh vagrant@dn01
~~~
Last login: Mon Apr  2 06:48:18 2018
~~~
[vagrant@dn01 ~]$ jps
~~~
2864 NodeManager
3021 Jps
~~~
[vagrant@dn01 ~]$ exit
~~~
logout
Connection to dn01 closed.
~~~
[vagrant@nn01 ~]$ ssh vagrant@dn02
~~~
Last login: Mon Apr  2 06:48:35 2018
~~~
[vagrant@dn02 ~]$ jps
~~~
3300 Jps
3143 NodeManager
~~~
[vagrant@nn01 ~]$ stop-all.sh
~~~
This script is Deprecated. Instead use stop-dfs.sh and stop-yarn.sh
Stopping namenodes on [nn01]
nn01: stopping namenode
dn02: no datanode to stop
dn01: no datanode to stop
Stopping secondary namenodes [nn01]
nn01: stopping secondarynamenode
stopping yarn daemons
stopping resourcemanager
dn02: stopping nodemanager
dn01: stopping nodemanager
dn02: nodemanager did not stop gracefully after 5 seconds: killing with kill -9
dn01: nodemanager did not stop gracefully after 5 seconds: killing with kill -9
no proxyserver to stop
~~~
