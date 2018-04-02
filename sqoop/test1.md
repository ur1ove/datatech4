[vagrant@dn02 ~]$ mysql -u root -p
~~~
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 5.5.56-MariaDB MariaDB Server

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use sqoopdemo;
ERROR 1049 (42000): Unknown database 'sqoopdemo'
MariaDB [(none)]> create database sqoopdemo;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> use sqoopdemo;
Database changed
MariaDB [sqoopdemo]> CREATE TABLE departments (
    ->   department_id  INT(11) unsigned NOT NULL,
    ->   department_name VARCHAR(32) NOT NULL,
    ->   PRIMARY KEY (department_id)
    -> );
Query OK, 0 rows affected (0.01 sec)

MariaDB [sqoopdemo]> insert into departments (department_id, department_name) VALUES
    -> (1, 'Fitness'),
    -> (2, 'Footwear'),
    -> (3, 'Apparel'),
    -> (4, 'Golf'),
    -> (5, 'Outdoors'),
    -> (6, 'Fan Shop');
Query OK, 6 rows affected (0.00 sec)
Records: 6  Duplicates: 0  Warnings: 0

MariaDB [sqoopdemo]> select * from departments;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             1 | Fitness         |
|             2 | Footwear        |
|             3 | Apparel         |
|             4 | Golf            |
|             5 | Outdoors        |
|             6 | Fan Shop        |
+---------------+-----------------+
6 rows in set (0.00 sec)

MariaDB [sqoopdemo]> exit
Bye
[vagrant@dn02 ~]$ sqoop-version
Warning: /opt/sqoop/current/../hbase does not exist! HBase imports will fail.
Please set $HBASE_HOME to the root of your HBase installation.
Warning: /opt/sqoop/current/../hcatalog does not exist! HCatalog jobs will fail.
Please set $HCAT_HOME to the root of your HCatalog installation.
Warning: /opt/sqoop/current/../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
Warning: /opt/sqoop/current/../zookeeper does not exist! Accumulo imports will fail.
Please set $ZOOKEEPER_HOME to the root of your Zookeeper installation.
18/04/02 06:28:28 INFO sqoop.Sqoop: Running Sqoop version: 1.4.7
Sqoop 1.4.7
git commit id 2328971411f57f0cb683dfb79d19d4d19d185dd8
Compiled by maugli on Thu Dec 21 15:59:58 STD 2017
[vagrant@dn02 ~]$ 
~~~
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
dn01: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn01.out
dn02: starting nodemanager, logging to /opt/hadoop/2.8.3/logs/yarn-vagrant-nodemanager-dn02.out
[vagrant@nn01 ~]$ jps
2918 NameNode
3272 ResourceManager
3119 SecondaryNameNode
3535 Jps
[vagrant@nn01 ~]$ ssh dn01
[vagrant@dn01 ~]$ jps
3029 Jps
2872 NodeManager
[vagrant@dn01 ~]$ exit
logout
Connection to dn01 closed.
[vagrant@nn01 ~]$ 

~~~
[vagrant@dn02 ~]$ cd /opt/hadoop/  
[vagrant@dn02 hadoop]$ ls  
2.8.3  current
~~~
[vagrant@dn02 hadoop]$ ls -al
total 0
drwxr-xr-x.  3 vagrant root  34 Apr  2 01:19 .
drwxr-xr-x.  8 root    root  80 Apr  2 01:25 ..
drwxr-xr-x. 10 vagrant root 161 Apr  2 01:38 2.8.3
lrwxrwxrwx.  1 vagrant root  17 Apr  2 01:19 current -> /opt/hadoop/2.8.3
[vagrant@dn02 hadoop]$ cd current/
[vagrant@dn02 current]$ ls
bin  include  libexec      logs        README.txt  share
etc  lib      LICENSE.txt  NOTICE.txt  sbin
[vagrant@dn02 current]$ cd logs
[vagrant@dn02 logs]$ ls -al
total 124
drwxrwxr-x.  3 vagrant vagrant  4096 Apr  2 06:31 .
drwxr-xr-x. 10 vagrant root      161 Apr  2 01:38 ..
-rw-rw-r--.  1 vagrant vagrant 38904 Apr  2 06:30 hadoop-vagrant-datanode-dn02.log
-rw-rw-r--.  1 vagrant vagrant   718 Apr  2 06:30 hadoop-vagrant-datanode-dn02.out
-rw-rw-r--.  1 vagrant vagrant   718 Apr  2 01:38 hadoop-vagrant-datanode-dn02.out.1
-rw-rw-r--.  1 vagrant vagrant     0 Apr  2 01:39 SecurityAuth-vagrant.audit
drwxr-xr-x.  2 vagrant vagrant     6 Apr  2 06:33 userlogs
-rw-rw-r--.  1 vagrant vagrant 64856 Apr  2 06:34 yarn-vagrant-nodemanager-dn02.log
-rw-rw-r--.  1 vagrant vagrant  1508 Apr  2 06:31 yarn-vagrant-nodemanager-dn02.out
-rw-rw-r--.  1 vagrant vagrant  1508 Apr  2 01:41 yarn-vagrant-nodemanager-dn02.out.1
[vagrant@dn02 logs]$ 
~~~
