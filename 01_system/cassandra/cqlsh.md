~~~
[root@localhost cassandra]# cqlsh localhost
Connected to Test Cluster at localhost:9042.
[cqlsh 5.0.1 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh> use demo ;
cqlsh:demo> select * from users ;

 id | email           | name
----+-----------------+------
  1 | naver@naver.com |  Kim

(1 rows)
cqlsh:demo> create table  test_table_ex_1 (id  text primary key, name text, descript text) ;
cqlsh:demo> INSERT INTO demo.test_table_ex_1 (id, name , descript ) VALUES ( 'id_1', 'name_1', 'test_data_1') ;
cqlsh:demo> INSERT INTO demo.test_table_ex_1 (id, name , descript ) VALUES ( 'id_2', 'name_2', 'test_data_2') ;
cqlsh:demo> INSERT INTO demo.test_table_ex_1 (id, name , descript ) VALUES ( 'id_1', 'name_1', 'test_data_3') ;
cqlsh:demo> select * from demo.test_table_ex_1;

 id   | descript    | name
------+-------------+--------
 id_2 | test_data_2 | name_2
 id_1 | test_data_3 | name_1

(2 rows)
cqlsh:demo> INSERT INTO demo.test_table_ex_1 (id, name , descript ) VALUES ( 'id_1', 'name_1', 'test_data_3') IF NOT EXISTS ;

 [applied] | id   | descript    | name
-----------+------+-------------+--------
     False | id_1 | test_data_3 | name_1

cqlsh:demo> select * from demo.test_table_ex_1 ;

 id   | descript    | name
------+-------------+--------
 id_2 | test_data_2 | name_2
 id_1 | test_data_3 | name_1

(2 rows)
cqlsh:demo> UPDATE demo.test_table_ex_1 SET descript='test_data_3' WHERE id = 'id_1' IF name = 'name_1' ;

 [applied]
-----------
      True

cqlsh:demo> select * from demo.test_table_ex_1 ;                                      
 id   | descript    | name
------+-------------+--------
 id_2 | test_data_2 | name_2
 id_1 | test_data_3 | name_1

(2 rows)
cqlsh:demo> SELECT * FROM  demo.test_table_ex_1 WHERE name='name_1';
InvalidRequest: Error from server: code=2200 [Invalid query] message="Cannot execute this query as it might involve data filtering and thus may have unpredictable performance. If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING"
cqlsh:demo> CREATE INDEX name_idx ON demo.test_table_ex_1 (name);
cqlsh:demo> SELECT * FROM  demo.test_table_ex_1 WHERE name='name_1';

 id   | descript    | name
------+-------------+--------
 id_1 | test_data_3 | name_1

(1 rows)
cqlsh:demo> CREATE TABLE emp(
        ...    emp_id int PRIMARY KEY,
        ...    emp_name text,
        ...    emp_city text,
        ...    emp_sal varint,
        ...    emp_phone varint
        ...    );

cqlsh:demo>
cqlsh:demo> BEGIN BATCH
        ... INSERT INTO emp (emp_id, emp_city, emp_name, emp_phone, emp_sal) values(  4,'Pune','rajeev',9848022331, 30000);
        ... UPDATE emp SET emp_sal = 50000 WHERE emp_id =3;
        ... DELETE emp_city FROM emp WHERE emp_id = 2;
        ... APPLY BATCH;
cqlsh:demo> select * from emp ;

 emp_id | emp_city | emp_name | emp_phone  | emp_sal
--------+----------+----------+------------+---------
      4 |     Pune |   rajeev | 9848022331 |   30000
      3 |     null |     null |       null |   50000

(2 rows)
cqlsh:demo>
~~~
