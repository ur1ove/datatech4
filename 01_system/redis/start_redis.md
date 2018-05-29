
~~~
[root@localhost yum.repos.d]# vi /etc/redis.conf
......
#pidfile /var/run/redis_6379.pid
pidfile /var/run/redis.pid

dir /var/lib/redis

logfile /var/log/redis/redis.log

#bind 127.0.0.1
......
[root@localhost yum.repos.d]# systemctl start redis.service
[root@localhost yum.repos.d]# systemctl status redis.service
● redis.service - Redis persistent key-value database
   Loaded: loaded (/usr/lib/systemd/system/redis.service; disabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/redis.service.d
           └─limit.conf
   Active: active (running) since Wed 2018-05-30 13:54:50 KST; 16s ago
 Main PID: 87431 (redis-server)
   CGroup: /system.slice/redis.service
           └─87431 /usr/bin/redis-server *:6379

May 30 13:54:50 localhost.localdomain systemd[1]: Starting Redis persistent key-va....
May 30 13:54:50 localhost.localdomain systemd[1]: Started Redis persistent key-val....
Hint: Some lines were ellipsized, use -l to show in full.
~~~
  
~~~
[root@localhost yum.repos.d]# redis-cli ping
PONG
[root@localhost yum.repos.d]# ss -nlp | grep redis
tcp    LISTEN     0      128       *:6379                  *:*                   users:(("redis-server",pid=87431,fd=7))
tcp    LISTEN     0      128      :::6379                 :::*                   users:(("redis-server",pid=87431,fd=6))
~~~
  
~~~
[root@localhost yum.repos.d]# redis-cli -h localhost
localhost:6379> set data1 mydata1
OK
localhost:6379> set data2 mydata2
OK
localhost:6379> keys dat*
1) "data1"
2) "data2"
~~~
  
~~~
localhost:6379> get data1
"mydata1"
~~~
