
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
