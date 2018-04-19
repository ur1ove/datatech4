## 깃(Git) 설치하기^^  
  
1) 어라? 코드 좀 볼라니 깃이 없네.  
~~~
[b3nn9@dn01 ~]$ git clone https://github.com/guriguri/cauca
bash: git: command not found...
~~~
2) 깃 좀 깔아볼까?  
~~~
[b3nn9@dn01 ~]$ sudo yum install git
Loaded plugins: fastestmirror, langpacks
Loading mirror speeds from cached hostfile
 * epel: mirror01.idc.hinet.net
 * ius: mirrors.tuna.tsinghua.edu.cn
Resolving Dependencies
--> Running transaction check
---> Package git.x86_64 0:1.8.3.1-12.el7_4 will be installed
--> Processing Dependency: perl-Git = 1.8.3.1-12.el7_4 for package: git-1.8.3.1-12.el7_4.x86_64
--> Processing Dependency: perl(Term::ReadKey) for package: git-1.8.3.1-12.el7_4.x86_64
--> Processing Dependency: perl(Git) for package: git-1.8.3.1-12.el7_4.x86_64
--> Processing Dependency: perl(Error) for package: git-1.8.3.1-12.el7_4.x86_64
--> Running transaction check
---> Package perl-Error.noarch 1:0.17020-2.el7 will be installed
---> Package perl-Git.noarch 0:1.8.3.1-12.el7_4 will be installed
---> Package perl-TermReadKey.x86_64 0:2.30-20.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===========================================================================================================
 Package                      Arch               Version                         Repository           Size
===========================================================================================================
Installing:
 git                          x86_64             1.8.3.1-12.el7_4                updates             4.4 M
Installing for dependencies:
 perl-Error                   noarch             1:0.17020-2.el7                 base                 32 k
 perl-Git                     noarch             1.8.3.1-12.el7_4                updates              53 k
 perl-TermReadKey             x86_64             2.30-20.el7                     base                 31 k

Transaction Summary
===========================================================================================================
Install  1 Package (+3 Dependent packages)

Total download size: 4.5 M
Installed size: 22 M
Is this ok [y/d/N]: y
Downloading packages:
(1/4): perl-Error-0.17020-2.el7.noarch.rpm                                          |  32 kB  00:00:00     
(2/4): perl-Git-1.8.3.1-12.el7_4.noarch.rpm                                         |  53 kB  00:00:00     
(3/4): perl-TermReadKey-2.30-20.el7.x86_64.rpm                                      |  31 kB  00:00:00     
(4/4): git-1.8.3.1-12.el7_4.x86_64.rpm                                              | 4.4 MB  00:00:00     
-----------------------------------------------------------------------------------------------------------
Total                                                                      7.8 MB/s | 4.5 MB  00:00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : 1:perl-Error-0.17020-2.el7.noarch                                                       1/4 
  Installing : perl-TermReadKey-2.30-20.el7.x86_64                                                     2/4 
  Installing : perl-Git-1.8.3.1-12.el7_4.noarch                                                        3/4 
  Installing : git-1.8.3.1-12.el7_4.x86_64                                                             4/4 
  Verifying  : git-1.8.3.1-12.el7_4.x86_64                                                             1/4 
  Verifying  : 1:perl-Error-0.17020-2.el7.noarch                                                       2/4 
  Verifying  : perl-Git-1.8.3.1-12.el7_4.noarch                                                        3/4 
  Verifying  : perl-TermReadKey-2.30-20.el7.x86_64                                                     4/4 

Installed:
  git.x86_64 0:1.8.3.1-12.el7_4                                                                            

Dependency Installed:
  perl-Error.noarch 1:0.17020-2.el7                     perl-Git.noarch 0:1.8.3.1-12.el7_4                
  perl-TermReadKey.x86_64 0:2.30-20.el7                

Complete!
~~~
3) What the..... 뭐냐?
~~~
[b3nn9@dn01 ~]$ git clone https://github.com/guriguri/cauca
Cloning into 'cauca'...
fatal: unable to access 'https://github.com/guriguri/cauca/': Peer reports incompatible or unsupported protocol version. 
~~~
