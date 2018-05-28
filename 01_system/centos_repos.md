  
~~~
[root@localhost ~]# bzip2 /etc/yum.repos.d/CentOS-*.repo
[root@localhost ~]# yum repolist
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: ftp.riken.jp
repo id            repo name                                              status
epel/x86_64        Extra Packages for Enterprise Linux 7 - x86_64         12,575
repolist: 12,575
[root@localhost ~]# ll /etc/yum.repos.d/
total 36
-rw-r--r--  1 root root  648 Aug 31  2017 CentOS-Base.repo.bz2
-rw-r--r--  1 root root  774 Aug 31  2017 CentOS-CR.repo.bz2
-rw-r--r--  1 root root  441 Aug 31  2017 CentOS-Debuginfo.repo.bz2
-rw-r--r--  1 root root  239 Aug 31  2017 CentOS-fasttrack.repo.bz2
-rw-r--r--  1 root root  407 Aug 31  2017 CentOS-Media.repo.bz2
-rw-r--r--  1 root root  597 Aug 31  2017 CentOS-Sources.repo.bz2
-rw-r--r--  1 root root  534 Aug 31  2017 CentOS-Vault.repo.bz2
-rw-r--r--. 1 root root  951 Oct  3  2017 epel.repo
-rw-r--r--. 1 root root 1050 Oct  3  2017 epel-testing.repo
~~~
  
~~~
[root@localhost ~]# echo '[base]
> name=CentOS-$releasever - Base
> baseurl=http://ftp.daumkakao.com/centos/$releasever/os/$basearch/
> gpgcheck=0
> [updates]
> name=CentOS-$releasever - Updates
> baseurl=http://ftp.daumkakao.com/centos/$releasever/updates/$basearch/
> gpgcheck=0
> [extras]
> name=CentOS-$releasever - Extras
> baseurl=http://ftp.daumkakao.com/centos/$releasever/extras/$basearch/
> gpgcheck=0' > /etc/yum.repos.d/Daum.repo
[root@localhost ~]# yum repolist
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: ftp.riken.jp
repo id               repo name                                           status
base/7/x86_64         CentOS-7 - Base                                      9,911
epel/x86_64           Extra Packages for Enterprise Linux 7 - x86_64      12,575
extras/7/x86_64       CentOS-7 - Extras                                      303
updates/7/x86_64      CentOS-7 - Updates                                     632
repolist: 23,421
~~~
