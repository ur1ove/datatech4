## Kibana 좀 설치해볼까요?  
  
1) 사용할 계정을 만들고 sudo 권한을 줍니다.  
~~~
Last login: Thu Apr 19 09:59:46 on ttys004
Benjaminui-MacBook-Pro:~ bEnnY$ ssh eduuser@210.114.91.91 -p 19540
eduuser@210.114.91.91's password: 
Last login: Thu Apr 19 03:38:23 2018 from dn01
[eduuser@dn02 ~]$ sudo adduser esadmin
[eduuser@dn02 ~]$ sudo vi /etc/group

[eduuser@dn02 ~]$ sudo passwd esadmin
Changing password for user esadmin.
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.
[eduuser@dn02 ~]$ exit
logout
Connection to 210.114.91.91 closed.
~~~
2) Kibana를 다운로드하고 압축을 풉니다.
~~~
Benjaminui-MacBook-Pro:~ bEnnY$ ssh esadmin@210.114.91.91 -p 19540
esadmin@210.114.91.91's password: 
[esadmin@dn02 ~]$ wget https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz
--2018-04-19 03:40:53--  https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz
Resolving artifacts.elastic.co (artifacts.elastic.co)... 23.21.67.46, 184.73.245.233, 23.23.109.100, ...
Connecting to artifacts.elastic.co (artifacts.elastic.co)|23.21.67.46|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 85348919 (81M) [application/x-gzip]
Saving to: ‘kibana-6.2.4-linux-x86_64.tar.gz’

100%[=============================================================>] 85,348,919  7.59MB/s   in 15s    

2018-04-19 03:41:11 (5.53 MB/s) - ‘kibana-6.2.4-linux-x86_64.tar.gz’ saved [85348919/85348919]

[esadmin@dn02 ~]$ tar zxvf kibana-6.2.4-linux-x86_64.tar.gz 
~~~
