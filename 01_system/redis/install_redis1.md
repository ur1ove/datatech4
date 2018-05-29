
~~~
[root@localhost yum.repos.d]# yum -y install --enablerepo=remi redis                  Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi: mirror.oxilion.nl
 * remi-safe: mirror.oxilion.nl
 * webtatic: sp.repo.webtatic.com
Resolving Dependencies
--> Running transaction check
---> Package redis.x86_64 0:4.0.9-1.el7.remi will be installed
--> Processing Dependency: libjemalloc.so.1()(64bit) for package: redis-4.0.9-1.el7.remi.x86_64
--> Finished Dependency Resolution
Error: Package: redis-4.0.9-1.el7.remi.x86_64 (remi)
           Requires: libjemalloc.so.1()(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
~~~

~~~
[root@localhost yum.repos.d]# yum --enablerepo=remi,remi-test install redis
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi: repo1.sea.innoscale.net
 * remi-safe: repo1.sea.innoscale.net
 * remi-test: repo1.sea.innoscale.net
 * webtatic: sp.repo.webtatic.com
remi-test                                                      | 2.9 kB  00:00:00
remi-test/primary_db                                           | 580 kB  00:00:09
Resolving Dependencies
--> Running transaction check
---> Package redis.x86_64 0:4.0.9-1.el7.remi will be installed
--> Processing Dependency: libjemalloc.so.1()(64bit) for package: redis-4.0.9-1.el7.remi.x86_64
--> Finished Dependency Resolution
Error: Package: redis-4.0.9-1.el7.remi.x86_64 (remi)
           Requires: libjemalloc.so.1()(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
~~~

~~~
[root@localhost yum.repos.d]# rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
Retrieving https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
Preparing...                          ################################# [100%]
        package epel-release-7-11.noarch is already installed
[root@localhost yum.repos.d]# rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
Retrieving http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
warning: /var/tmp/rpm-tmp.pYR6JZ: Header V4 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
Preparing...                          ################################# [100%]
        package remi-release-7.4-2.el7.remi.noarch is already installed
~~~

~~~
[root@localhost yum.repos.d]# yum --enablerepo=remi,remi-test install redis           
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi: remi.mirror.ate.info
 * remi-safe: remi.mirror.ate.info
 * remi-test: remi.mirror.ate.info
 * webtatic: sp.repo.webtatic.com
Resolving Dependencies
--> Running transaction check
---> Package redis.x86_64 0:4.0.9-1.el7.remi will be installed
--> Processing Dependency: libjemalloc.so.1()(64bit) for package: redis-4.0.9-1.el7.remi.x86_64
--> Finished Dependency Resolution
Error: Package: redis-4.0.9-1.el7.remi.x86_64 (remi)
           Requires: libjemalloc.so.1()(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
[root@localhost yum.repos.d]# wget https://www.rpmfind.net/linux/epel/7/x86_64/Packages/j/jemalloc-3.6.0-1.el7.x86_64.rpm
--2018-05-30 13:47:08--  https://www.rpmfind.net/linux/epel/7/x86_64/Packages/j/jemalloc-3.6.0-1.el7.x86_64.rpm
Resolving www.rpmfind.net (www.rpmfind.net)... 195.220.108.108
Connecting to www.rpmfind.net (www.rpmfind.net)|195.220.108.108|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 107040 (105K) [application/x-rpm]
Saving to: ‘jemalloc-3.6.0-1.el7.x86_64.rpm’

100%[============================================>] 107,040      112KB/s   in 0.9s

2018-05-30 13:47:11 (112 KB/s) - ‘jemalloc-3.6.0-1.el7.x86_64.rpm’ saved [107040/107040]

[root@localhost yum.repos.d]# rpm -Uvh jemalloc-3.6.0-1.el7.x86_64.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:jemalloc-3.6.0-1.el7             ################################# [100%]
~~~

~~~
[root@localhost yum.repos.d]# yum --enablerepo=remi,remi-test install redis           Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi: remi.mirror.ate.info
 * remi-safe: remi.mirror.ate.info
 * remi-test: remi.mirror.ate.info
 * webtatic: sp.repo.webtatic.com
Resolving Dependencies
--> Running transaction check
---> Package redis.x86_64 0:4.0.9-1.el7.remi will be installed
--> Processing Dependency: libjemalloc.so.1()(64bit) for package: redis-4.0.9-1.el7.remi.x86_64
--> Finished Dependency Resolution
Error: Package: redis-4.0.9-1.el7.remi.x86_64 (remi)
           Requires: libjemalloc.so.1()(64bit)
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
[root@localhost yum.repos.d]# Requires: libjemalloc.so.1()(64bit)^C
[root@localhost yum.repos.d]# yum install jemalloc
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi-safe: mirrors.thzhost.com
 * webtatic: sp.repo.webtatic.com
No package jemalloc available.
Error: Nothing to do
[root@localhost yum.repos.d]# wget https://www.rpmfind.net/linux/epel/7/x86_64/Packages/j/jemalloc-3.6.0-1.el7.x86_64.rpm
--2018-05-30 13:47:08--  https://www.rpmfind.net/linux/epel/7/x86_64/Packages/j/jemalloc-3.6.0-1.el7.x86_64.rpm
Resolving www.rpmfind.net (www.rpmfind.net)... 195.220.108.108
Connecting to www.rpmfind.net (www.rpmfind.net)|195.220.108.108|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 107040 (105K) [application/x-rpm]
Saving to: ‘jemalloc-3.6.0-1.el7.x86_64.rpm’

100%[============================================>] 107,040      112KB/s   in 0.9s

2018-05-30 13:47:11 (112 KB/s) - ‘jemalloc-3.6.0-1.el7.x86_64.rpm’ saved [107040/107040]

[root@localhost yum.repos.d]# rpm -Uvh jemalloc-3.6.0-1.el7.x86_64.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:jemalloc-3.6.0-1.el7             ################################# [100%]
[root@localhost yum.repos.d]# yum --enablerepo=remi,remi-test install redis           Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * remi: remi.mirror.wearetriple.com
 * remi-safe: remi.mirror.wearetriple.com
 * remi-test: remi.mirror.wearetriple.com
 * webtatic: sp.repo.webtatic.com
Resolving Dependencies
--> Running transaction check
---> Package redis.x86_64 0:4.0.9-1.el7.remi will be installed
--> Finished Dependency Resolution

Dependencies Resolved

======================================================================================
 Package          Arch              Version                     Repository       Size
======================================================================================
Installing:
 redis            x86_64            4.0.9-1.el7.remi            remi            578 k

Transaction Summary
======================================================================================
Install  1 Package

Total download size: 578 k
Installed size: 1.4 M
Is this ok [y/d/N]: y
Downloading packages:
warning: /var/cache/yum/x86_64/7/remi/packages/redis-4.0.9-1.el7.remi.x86_64.rpm: Header V4 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
Public key for redis-4.0.9-1.el7.remi.x86_64.rpm is not installed
redis-4.0.9-1.el7.remi.x86_64.rpm                              | 578 kB  00:00:07
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-remi
Importing GPG key 0x00F97F56:
 Userid     : "Remi Collet <RPMS@FamilleCollet.com>"
 Fingerprint: 1ee0 4cce 88a4 ae4a a29a 5df5 004e 6f47 00f9 7f56
 Package    : remi-release-7.4-2.el7.remi.noarch (installed)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-remi
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : redis-4.0.9-1.el7.remi.x86_64                                      1/1
  Verifying  : redis-4.0.9-1.el7.remi.x86_64                                      1/1

Installed:
  redis.x86_64 0:4.0.9-1.el7.remi

Complete!
~~~
