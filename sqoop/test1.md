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
~~~
2.8.3  current
~~~
[vagrant@dn02 hadoop]$ ls -al
~~~
total 0
drwxr-xr-x.  3 vagrant root  34 Apr  2 01:19 .
drwxr-xr-x.  8 root    root  80 Apr  2 01:25 ..
drwxr-xr-x. 10 vagrant root 161 Apr  2 01:38 2.8.3
lrwxrwxrwx.  1 vagrant root  17 Apr  2 01:19 current -> /opt/hadoop/2.8.3
~~~
[vagrant@dn02 hadoop]$ cd current/  
[vagrant@dn02 current]$ ls  
~~~
bin  include  libexec      logs        README.txt  share
etc  lib      LICENSE.txt  NOTICE.txt  sbin
~~~
[vagrant@dn02 current]$ cd logs  
[vagrant@dn02 logs]$ ls -al  
~~~
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
[vagrant@nn01 ~]$ 
~~~
[vagrant@nn01 ~]$ vi /opt/hadoop/current/etc/hadoop/hdfs-site.xml
~~~
......
        <property>
                <name>dfs.namenode.name.dir</name>
                <value>file:/var/hadoop/hadoop-namenode</value>
        </property>
        <property>
                <name>dfs.datanode.data.dir</name>
                <value>file:/var/hadoop/hadoop-datanode</value>
        </property>
......
~~~
[vagrant@nn01 ~]$ vi /opt/hadoop/current/etc/hadoop/hdfs-site.xml  
[vagrant@nn01 ~]$ scp /opt/hadoop/current/etc/hadoop/hdfs-site.xml vagrant@dn02:/opt/hadoop/current/etc/hadoop/hdfs-site.xml  
hdfs-site.xml                                        100% 1577     2.3MB/s   00:00    
[vagrant@nn01 ~]$ scp /opt/hadoop/current/etc/hadoop/hdfs-site.xml vagrant@dn01:/opt/hadoop/current/etc/hadoop/hdfs-site.xml   
hdfs-site.xml                                        100% 1577     2.1MB/s   00:00    
[vagrant@nn01 ~]$ 

C:\Users\user\vagrant\hadoop>vagrant halt
~~~
==> dn02: Attempting graceful shutdown of VM...
==> dn01: Attempting graceful shutdown of VM...
==> nn01: Attempting graceful shutdown of VM...
~~~
C:\Users\user\vagrant\hadoop>vagrant snapshot push
~~~
==> nn01: Snapshotting the machine as 'push_1522651496_7937'...
==> nn01: Snapshot saved! You can restore the snapshot at any time by
==> nn01: using `vagrant snapshot restore`. You can delete it using
==> nn01: `vagrant snapshot delete`.
==> dn01: Snapshotting the machine as 'push_1522651498_6704'...
==> dn01: Snapshot saved! You can restore the snapshot at any time by
==> dn01: using `vagrant snapshot restore`. You can delete it using
==> dn01: `vagrant snapshot delete`.
==> dn02: Snapshotting the machine as 'push_1522651498_6495'...
==> dn02: Snapshot saved! You can restore the snapshot at any time by
==> dn02: using `vagrant snapshot restore`. You can delete it using
==> dn02: `vagrant snapshot delete`.
~~~
C:\Users\user\vagrant\hadoop>vagrant up dn01 dn02 nn01
~~~
Bringing machine 'dn01' up with 'virtualbox' provider...
Bringing machine 'dn02' up with 'virtualbox' provider...
Bringing machine 'nn01' up with 'virtualbox' provider...
==> dn01: Clearing any previously set forwarded ports...
==> dn01: Clearing any previously set network interfaces...
==> dn01: Preparing network interfaces based on configuration...
    dn01: Adapter 1: nat
    dn01: Adapter 2: hostonly
==> dn01: Forwarding ports...
    dn01: 22 (guest) => 2222 (host) (adapter 1)
==> dn01: Running 'pre-boot' VM customizations...
==> dn01: Booting VM...
==> dn01: Waiting for machine to boot. This may take a few minutes...
    dn01: SSH address: 127.0.0.1:2222
    dn01: SSH username: vagrant
    dn01: SSH auth method: private key
==> dn01: Machine booted and ready!
==> dn01: Checking for guest additions in VM...
    dn01: No guest additions were detected on the base box for this VM! Guest
    dn01: additions are required for forwarded ports, shared folders, host only
    dn01: networking, and more. If SSH fails on this machine, please install
    dn01: the guest additions and repackage the box to continue.
    dn01:
    dn01: This is not an error message; everything may continue to work properly
,
    dn01: in which case you may ignore this message.
==> dn01: Setting hostname...
==> dn01: Configuring and enabling network interfaces...
    dn01: SSH address: 127.0.0.1:2222
    dn01: SSH username: vagrant
    dn01: SSH auth method: private key
==> dn01: Rsyncing folder: /cygdrive/c/Users/user/vagrant/hadoop/ => /vagrant
==> dn01: Machine already provisioned. Run `vagrant provision` or use the `--pro
vision`
==> dn01: flag to force provisioning. Provisioners marked to run always will sti
ll run.
==> dn02: Clearing any previously set forwarded ports...
==> dn02: Fixed port collision for 22 => 2222. Now on port 2200.
==> dn02: Clearing any previously set network interfaces...
==> dn02: Preparing network interfaces based on configuration...
    dn02: Adapter 1: nat
    dn02: Adapter 2: hostonly
==> dn02: Forwarding ports...
    dn02: 22 (guest) => 2200 (host) (adapter 1)
==> dn02: Running 'pre-boot' VM customizations...
==> dn02: Booting VM...
==> dn02: Waiting for machine to boot. This may take a few minutes...
    dn02: SSH address: 127.0.0.1:2200
    dn02: SSH username: vagrant
    dn02: SSH auth method: private key
==> dn02: Machine booted and ready!
==> dn02: Checking for guest additions in VM...
    dn02: No guest additions were detected on the base box for this VM! Guest
    dn02: additions are required for forwarded ports, shared folders, host only
    dn02: networking, and more. If SSH fails on this machine, please install
    dn02: the guest additions and repackage the box to continue.
    dn02:
    dn02: This is not an error message; everything may continue to work properly
,
    dn02: in which case you may ignore this message.
==> dn02: Setting hostname...
==> dn02: Configuring and enabling network interfaces...
    dn02: SSH address: 127.0.0.1:2200
    dn02: SSH username: vagrant
    dn02: SSH auth method: private key
==> dn02: Rsyncing folder: /cygdrive/c/Users/user/vagrant/hadoop/ => /vagrant
==> dn02: Machine already provisioned. Run `vagrant provision` or use the `--pro
vision`
==> dn02: flag to force provisioning. Provisioners marked to run always will sti
ll run.
==> nn01: Clearing any previously set forwarded ports...
==> nn01: Fixed port collision for 22 => 2222. Now on port 2201.
==> nn01: Clearing any previously set network interfaces...
==> nn01: Preparing network interfaces based on configuration...
    nn01: Adapter 1: nat
    nn01: Adapter 2: hostonly
==> nn01: Forwarding ports...
    nn01: 22 (guest) => 2201 (host) (adapter 1)
==> nn01: Running 'pre-boot' VM customizations...
==> nn01: Booting VM...
==> nn01: Waiting for machine to boot. This may take a few minutes...
    nn01: SSH address: 127.0.0.1:2201
    nn01: SSH username: vagrant
    nn01: SSH auth method: private key
==> nn01: Machine booted and ready!
==> nn01: Checking for guest additions in VM...
    nn01: No guest additions were detected on the base box for this VM! Guest
    nn01: additions are required for forwarded ports, shared folders, host only
    nn01: networking, and more. If SSH fails on this machine, please install
    nn01: the guest additions and repackage the box to continue.
    nn01:
    nn01: This is not an error message; everything may continue to work properly
,
    nn01: in which case you may ignore this message.
==> nn01: Setting hostname...
==> nn01: Configuring and enabling network interfaces...
    nn01: SSH address: 127.0.0.1:2201
    nn01: SSH username: vagrant
    nn01: SSH auth method: private key
==> nn01: Rsyncing folder: /cygdrive/c/Users/user/vagrant/hadoop/ => /vagrant
==> nn01: Machine already provisioned. Run `vagrant provision` or use the `--pro
vision`
==> nn01: flag to force provisioning. Provisioners marked to run always will sti
ll run.

C:\Users\user\vagrant\hadoop>
~~~
