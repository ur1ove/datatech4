참고 : http://cassandra.apache.org/download/  
  
  
~~~
[root@localhost yum.repos.d]# vi /etc/yum.repos.d/cassandra.repo
[cassandra]
name=Apache Cassandra
baseurl=https://www.apache.org/dist/cassandra/redhat/311x/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://www.apache.org/dist/cassandra/KEYS
~~~
  
~~~
[root@localhost yum.repos.d]# yum install cassandra
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
cassandra/signature                                      |  819 B     00:00
Retrieving key from https://www.apache.org/dist/cassandra/KEYS
Importing GPG key 0xF2833C93:
 Userid     : "Eric Evans <eevans@sym-link.com>"
 Fingerprint: cec8 6bb4 a0ba 9d0f 9039 7cae f835 8fa2 f283 3c93
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
cassandra/signature                                      | 2.9 kB     00:06 !!!
cassandra/primary_db                                       | 8.0 kB   00:11
Resolving Dependencies
--> Running transaction check
---> Package cassandra.noarch 0:3.11.2-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package            Arch            Version            Repository          Size
================================================================================
Installing:
 cassandra          noarch          3.11.2-1           cassandra           28 M

Transaction Summary
================================================================================
Install  1 Package

Total download size: 28 M
Installed size: 37 M
Is this ok [y/d/N]: y
Downloading packages:

~~~
