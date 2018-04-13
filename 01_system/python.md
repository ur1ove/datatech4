  
  
[eduuser@dn01 ~]$ sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
~~~
Loaded plugins: fastestmirror, langpacks
ius-release.rpm                                                                     | 8.1 kB  00:00:00     
Examining /var/tmp/yum-root-wqv3bX/ius-release.rpm: ius-release-1.0-15.ius.centos7.noarch
Marking /var/tmp/yum-root-wqv3bX/ius-release.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package ius-release.noarch 0:1.0-15.ius.centos7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===========================================================================================================
 Package                 Arch               Version                         Repository                Size
===========================================================================================================
Installing:
 ius-release             noarch             1.0-15.ius.centos7              /ius-release             8.5 k

Transaction Summary
===========================================================================================================
Install  1 Package

Total size: 8.5 k
Installed size: 8.5 k
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : ius-release-1.0-15.ius.centos7.noarch                                                   1/1 
  Verifying  : ius-release-1.0-15.ius.centos7.noarch                                                   1/1 

Installed:
  ius-release.noarch 0:1.0-15.ius.centos7                                                                  

Complete!
[eduuser@dn01 ~]$ 
~~~
  
  
[eduuser@dn01 ~]$ sudo yum search python36  
~~~
Loaded plugins: fastestmirror, langpacks
ius                                                                                 | 2.3 kB  00:00:00     
ius/x86_64/primary_db                                                               | 251 kB  00:00:01     
Loading mirror speeds from cached hostfile
 * epel: mirror01.idc.hinet.net
 * ius: mirrors.tuna.tsinghua.edu.cn
========================================== N/S matched: python36 ==========================================
python36u-debuginfo.x86_64 : Debug information for package python36u
python36u-lxml-debuginfo.x86_64 : Debug information for package python36u-lxml
python36u-mod_wsgi-debuginfo.x86_64 : Debug information for package python36u-mod_wsgi
python36u-psycopg2-debuginfo.x86_64 : Debug information for package python36u-psycopg2
python36u-setproctitle-debuginfo.x86_64 : Debug information for package python36u-setproctitle
python36u-test.x86_64 : The self-test suite for the main python36u package
uwsgi-plugin-python36u-debuginfo.x86_64 : Debug information for package uwsgi-plugin-python36u
python36.x86_64 : Interpreter of the Python programming language
python36-debug.x86_64 : Debug version of the Python runtime
python36-devel.x86_64 : Libraries and header files needed for Python development
python36-libs.x86_64 : Python runtime libraries
python36-test.x86_64 : The self-test suite for the main python3 package
python36-tkinter.x86_64 : A GUI toolkit for Python
python36-tools.x86_64 : A collection of tools included with Python including 2to3 and idle
python36u.x86_64 : Interpreter of the Python programming language
python36u-debug.x86_64 : Debug version of the Python runtime
python36u-devel.x86_64 : Libraries and header files needed for Python development
python36u-gunicorn.noarch : Python WSGI application server
python36u-libs.x86_64 : Python runtime libraries
python36u-lxml.x86_64 : XML processing library combining libxml2/libxslt with the ElementTree API
python36u-mod_wsgi.x86_64 : A WSGI interface for Python web applications in Apache
python36u-pip.noarch : A tool for installing and managing Python packages
python36u-psycopg2.x86_64 : A PostgreSQL database adapter for Python
python36u-redis.noarch : Python interface to the Redis key-value store
python36u-setproctitle.x86_64 : Python module to customize a process title
python36u-setuptools.noarch : Easily build and distribute Python packages
python36u-tkinter.x86_64 : A GUI toolkit for Python
python36u-tools.x86_64 : A collection of tools included with Python including 2to3 and idle
uwsgi-plugin-python36u.x86_64 : uWSGI - Plugin for Python support

  Name and summary matches only, use "search all" for everything.
~~~
[eduuser@dn01 ~]$ sudo yum search python35  
~~~
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: mirror01.idc.hinet.net
 * ius: hkg.mirror.rackspace.com
========================================== N/S matched: python35 ==========================================
python35u-debuginfo.x86_64 : Debug information for package python35u
python35u-hiredis-debuginfo.x86_64 : Debug information for package python35u-hiredis
python35u-lxml-debuginfo.x86_64 : Debug information for package python35u-lxml
python35u-mod_wsgi-debuginfo.x86_64 : Debug information for package python35u-mod_wsgi
python35u-postgresql-debuginfo.x86_64 : Debug information for package python35u-postgresql
uwsgi-plugin-python35u-debuginfo.x86_64 : Debug information for package uwsgi-plugin-python35u
python35u.x86_64 : Version 3.5 of the Python programming language
python35u-debug.x86_64 : Debug version of the Python 3 runtime
python35u-devel.x86_64 : Libraries and header files needed for Python 3 development
python35u-hiredis.x86_64 : Python wrapper for hiredis
python35u-libs.x86_64 : Python 3 runtime libraries
python35u-lxml.x86_64 : XML processing library combining libxml2/libxslt with the ElementTree API
python35u-mod_wsgi.x86_64 : A WSGI interface for Python web applications in Apache
python35u-pip.noarch : A tool for installing and managing Python packages
python35u-postgresql.x86_64 : Connect to PostgreSQL with Python 3
python35u-redis.noarch : Python 3 interface to the Redis key-value store
python35u-setuptools.noarch : Easily build and distribute Python packages
python35u-test.x86_64 : The test modules from the main python 3 package
python35u-tkinter.x86_64 : A GUI toolkit for Python 3
python35u-tools.x86_64 : A collection of tools included with Python 3
uwsgi-plugin-python35u.x86_64 : uWSGI - Plugin for Python support

  Name and summary matches only, use "search all" for everything.
[eduuser@dn01 ~]$ 
~~~

~~~
[eduuser@dn01 ~]$ sudo yum install -y python36u python36u-libs python36u-devel python36u-pip
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: mirror01.idc.hinet.net
 * ius: hkg.mirror.rackspace.com
Resolving Dependencies
--> Running transaction check
---> Package python36u.x86_64 0:3.6.4-1.ius.centos7 will be installed
---> Package python36u-devel.x86_64 0:3.6.4-1.ius.centos7 will be installed
---> Package python36u-libs.x86_64 0:3.6.4-1.ius.centos7 will be installed
--> Processing Dependency: libcrypto.so.10(OPENSSL_1.0.2)(64bit) for package: python36u-libs-3.6.4-1.ius.centos7.x86_64
---> Package python36u-pip.noarch 0:9.0.1-1.ius.centos7 will be installed
--> Processing Dependency: python36u-setuptools for package: python36u-pip-9.0.1-1.ius.centos7.noarch
--> Running transaction check
---> Package openssl-libs.x86_64 1:1.0.1e-34.el7 will be updated
--> Processing Dependency: openssl-libs(x86-64) = 1:1.0.1e-34.el7 for package: 1:openssl-1.0.1e-34.el7.x86_64
---> Package openssl-libs.x86_64 1:1.0.2k-8.el7 will be an update
---> Package python36u-setuptools.noarch 0:39.0.1-1.ius.centos7 will be installed
--> Running transaction check
---> Package openssl.x86_64 1:1.0.1e-34.el7 will be updated
---> Package openssl.x86_64 1:1.0.2k-8.el7 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

===========================================================================================================
 Package                         Arch              Version                           Repository       Size
===========================================================================================================
Installing:
 python36u                       x86_64            3.6.4-1.ius.centos7               ius              56 k
 python36u-devel                 x86_64            3.6.4-1.ius.centos7               ius             839 k
 python36u-libs                  x86_64            3.6.4-1.ius.centos7               ius             8.7 M
 python36u-pip                   noarch            9.0.1-1.ius.centos7               ius             1.8 M
Installing for dependencies:
 python36u-setuptools            noarch            39.0.1-1.ius.centos7              ius             642 k
Updating for dependencies:
 openssl                         x86_64            1:1.0.2k-8.el7                    base            492 k
 openssl-libs                    x86_64            1:1.0.2k-8.el7                    base            1.2 M

Transaction Summary
===========================================================================================================
Install  4 Packages (+1 Dependent package)
Upgrade             ( 2 Dependent packages)

Total download size: 14 M
Downloading packages:
No Presto metadata available for base
(1/7): openssl-1.0.2k-8.el7.x86_64.rpm                                              | 492 kB  00:00:00     
(2/7): openssl-libs-1.0.2k-8.el7.x86_64.rpm                                         | 1.2 MB  00:00:00     
warning: /var/cache/yum/x86_64/7/ius/packages/python36u-3.6.4-1.ius.centos7.x86_64.rpm: Header V4 DSA/SHA1 Signature, key ID 9cd4953f: NOKEY
Public key for python36u-3.6.4-1.ius.centos7.x86_64.rpm is not installed
(3/7): python36u-3.6.4-1.ius.centos7.x86_64.rpm                                     |  56 kB  00:00:00     
(4/7): python36u-devel-3.6.4-1.ius.centos7.x86_64.rpm                               | 839 kB  00:00:02     
(5/7): python36u-setuptools-39.0.1-1.ius.centos7.noarch.rpm                         | 642 kB  00:00:02     
(6/7): python36u-pip-9.0.1-1.ius.centos7.noarch.rpm                                 | 1.8 MB  00:00:03     
(7/7): python36u-libs-3.6.4-1.ius.centos7.x86_64.rpm                                | 8.7 MB  00:00:05     
-----------------------------------------------------------------------------------------------------------
Total                                                                      2.5 MB/s |  14 MB  00:00:05     
Retrieving key from file:///etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY
Importing GPG key 0x9CD4953F:
 Userid     : "IUS Community Project <coredev@iuscommunity.org>"
 Fingerprint: 8b84 6e3a b3fe 6462 74e8 670f da22 1cdf 9cd4 953f
 Package    : ius-release-1.0-15.ius.centos7.noarch (@/ius-release)
 From       : /etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Updating   : 1:openssl-libs-1.0.2k-8.el7.x86_64                                                      1/9 
  Installing : python36u-3.6.4-1.ius.centos7.x86_64                                                    2/9 
  Installing : python36u-libs-3.6.4-1.ius.centos7.x86_64                                               3/9 
  Installing : python36u-setuptools-39.0.1-1.ius.centos7.noarch                                        4/9 
  Installing : python36u-pip-9.0.1-1.ius.centos7.noarch                                                5/9 
  Installing : python36u-devel-3.6.4-1.ius.centos7.x86_64                                              6/9 
  Updating   : 1:openssl-1.0.2k-8.el7.x86_64                                                           7/9 
  Cleanup    : 1:openssl-1.0.1e-34.el7.x86_64                                                          8/9 
  Cleanup    : 1:openssl-libs-1.0.1e-34.el7.x86_64                                                     9/9 
  Verifying  : 1:openssl-1.0.2k-8.el7.x86_64                                                           1/9 
  Verifying  : python36u-devel-3.6.4-1.ius.centos7.x86_64                                              2/9 
  Verifying  : python36u-setuptools-39.0.1-1.ius.centos7.noarch                                        3/9 
  Verifying  : 1:openssl-libs-1.0.2k-8.el7.x86_64                                                      4/9 
  Verifying  : python36u-pip-9.0.1-1.ius.centos7.noarch                                                5/9 
  Verifying  : python36u-3.6.4-1.ius.centos7.x86_64                                                    6/9 
  Verifying  : python36u-libs-3.6.4-1.ius.centos7.x86_64                                               7/9 
  Verifying  : 1:openssl-1.0.1e-34.el7.x86_64                                                          8/9 
  Verifying  : 1:openssl-libs-1.0.1e-34.el7.x86_64                                                     9/9 

Installed:
  python36u.x86_64 0:3.6.4-1.ius.centos7              python36u-devel.x86_64 0:3.6.4-1.ius.centos7        
  python36u-libs.x86_64 0:3.6.4-1.ius.centos7         python36u-pip.noarch 0:9.0.1-1.ius.centos7          

Dependency Installed:
  python36u-setuptools.noarch 0:39.0.1-1.ius.centos7                                                       

Dependency Updated:
  openssl.x86_64 1:1.0.2k-8.el7                     openssl-libs.x86_64 1:1.0.2k-8.el7                    

Complete!
[eduuser@dn01 ~]$ python3.6 -V
Python 3.6.0 :: Anaconda 4.3.0 (64-bit)
[eduuser@dn01 ~]$ 

~~~
