[vagrant@dn02 ~]$ mysql -u root -p
~~~
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 5.5.56-MariaDB MariaDB Server

Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use sqoopdemo;
ERROR 1049 (42000): Unknown database 'sqoopdemo'
MariaDB [(none)]> create database sqoopdemo;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> use sqoopdemo;
Database changed
MariaDB [sqoopdemo]> CREATE TABLE departments (
    ->   department_id  INT(11) unsigned NOT NULL,
    ->   department_name VARCHAR(32) NOT NULL,
    ->   PRIMARY KEY (department_id)
    -> );
Query OK, 0 rows affected (0.01 sec)

MariaDB [sqoopdemo]> insert into departments (department_id, department_name) VALUES
    -> (1, 'Fitness'),
    -> (2, 'Footwear'),
    -> (3, 'Apparel'),
    -> (4, 'Golf'),
    -> (5, 'Outdoors'),
    -> (6, 'Fan Shop');
Query OK, 6 rows affected (0.00 sec)
Records: 6  Duplicates: 0  Warnings: 0

MariaDB [sqoopdemo]> select * from departments;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             1 | Fitness         |
|             2 | Footwear        |
|             3 | Apparel         |
|             4 | Golf            |
|             5 | Outdoors        |
|             6 | Fan Shop        |
+---------------+-----------------+
6 rows in set (0.00 sec)

MariaDB [sqoopdemo]> exit
Bye
[vagrant@dn02 ~]$ sqoop-version
Warning: /opt/sqoop/current/../hbase does not exist! HBase imports will fail.
Please set $HBASE_HOME to the root of your HBase installation.
Warning: /opt/sqoop/current/../hcatalog does not exist! HCatalog jobs will fail.
Please set $HCAT_HOME to the root of your HCatalog installation.
Warning: /opt/sqoop/current/../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
Warning: /opt/sqoop/current/../zookeeper does not exist! Accumulo imports will fail.
Please set $ZOOKEEPER_HOME to the root of your Zookeeper installation.
18/04/02 06:28:28 INFO sqoop.Sqoop: Running Sqoop version: 1.4.7
Sqoop 1.4.7
git commit id 2328971411f57f0cb683dfb79d19d4d19d185dd8
Compiled by maugli on Thu Dec 21 15:59:58 STD 2017
[vagrant@dn02 ~]$ 
