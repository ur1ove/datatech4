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
warning: /var/cache/yum/x86_64/7/cassandra/packages/cassandra-3.11.2-1.noarch.rpm: Header V4 RSA/SHA256 Signature, key ID fe4b2bda: NOKEY
Public key for cassandra-3.11.2-1.noarch.rpm is not installed
cassandra-3.11.2-1.noarch.rpm                              |  28 MB   02:25
Retrieving key from https://www.apache.org/dist/cassandra/KEYS
Importing GPG key 0xF2833C93:
 Userid     : "Eric Evans <eevans@sym-link.com>"
 Fingerprint: cec8 6bb4 a0ba 9d0f 9039 7cae f835 8fa2 f283 3c93
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
Importing GPG key 0x8D77295D:
 Userid     : "Eric Evans <eevans@sym-link.com>"
 Fingerprint: c496 5ee9 e301 5d19 2ccc f2b6 f758 ce31 8d77 295d
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
Importing GPG key 0x2B5C1B00:
 Userid     : "Sylvain Lebresne (pcmanus) <sylvain@datastax.com>"
 Fingerprint: 5aed 1bf3 78e9 a19d ade1 bcb3 4bd7 36a8 2b5c 1b00
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
Importing GPG key 0x0353B12C:
 Userid     : "T Jake Luciani <jake@apache.org>"
 Fingerprint: 514a 2ad6 31a5 7a16 dd00 47ec 749d 6eec 0353 b12c
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
Importing GPG key 0xFE4B2BDA:
 Userid     : "Michael Shuler <michael@pbandjelly.org>"
 Fingerprint: a26e 528b 271f 19b9 e5d8 e19e a278 b781 fe4b 2bda
 From       : https://www.apache.org/dist/cassandra/KEYS
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : cassandra-3.11.2-1.noarch                                    1/1
  Verifying  : cassandra-3.11.2-1.noarch                                    1/1

Installed:
  cassandra.noarch 0:3.11.2-1

Complete!
[root@localhost yum.repos.d]#
~~~
  
~~~
[root@localhost yum.repos.d]# service cassandra start
Reloading systemd:                                         [  OK  ]
Starting cassandra (via systemctl):                        [  OK  ]
[root@localhost yum.repos.d]# chkconfig cassandra on
[root@localhost yum.repos.d]#
~~~
