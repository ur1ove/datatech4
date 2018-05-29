
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
  
~~~
[root@localhost yum.repos.d]# redis-cli -h localhost
localhost:6379> set counter 1000
OK
localhost:6379> INCR counter
(integer) 1001
localhost:6379> INCR counter
(integer) 1002
localhost:6379> INCRBY counter 50
(integer) 1052
localhost:6379> MSET key1 "Hello" key2 "world"
OK
localhost:6379> get key1
"Hello"
localhost:6379> get key2
"world"
localhost:6379> mget key1 key2
1) "Hello"
2) "world"
localhost:6379>
~~~
  
~~~
localhost:6379> rpush mylist A
(integer) 1
localhost:6379> rpush mylist B
(integer) 2
localhost:6379> lrange mylist 0 -1
1) "A"
2) "B"
localhost:6379> lpush mylist first
(integer) 3
localhost:6379> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
localhost:6379> rpush mylist 1 2 3 4 5 "foo bar"
(integer) 9
localhost:6379> lrange mylist 0 -1
1) "first"
2) "A"
3) "B"
4) "1"
5) "2"
6) "3"
7) "4"
8) "5"
9) "foo bar"
localhost:6379> rpush mylist a b c
(integer) 12
localhost:6379> rpop mylist
"c"
localhost:6379> rpop mylist
"b"
localhost:6379> rpop mylist
"a"
~~~
