  
  
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
