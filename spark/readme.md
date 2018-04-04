scala> val inputRDD = sc.textFile("file:///C:/opt/spark-2.2.1-bin-hadoop2.7/README.md")
~~~
inputRDD: org.apache.spark.rdd.RDD[String] = file:///C:/opt/spark-2.2.1-bin-hadoop2.7/README.md MapPartitionsRDD[17] at textFile at <console>:24
~~~
scala> val sparkRDD = inputRDD.filter(line => line.contains("spark"))
~~~
sparkRDD: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[18] at filter at <console>:25
~~~
scala> val apacheRDD = inputRDD.filter(line=>line.contains("apache"))
~~~
apacheRDD: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[19] at filter at <console>:25
~~~
scala> val unionRDD = sparkRDD.union(apacheRDD)
~~~
unionRDD: org.apache.spark.rdd.RDD[String] = UnionRDD[20] at union at <console>:27
~~~
scala> sparkRDD.count()
~~~
res11: Long = 13
~~~
scala> apacheRDD.count()
~~~
res12: Long = 10
~~~
scala> unionRDD.count()
~~~
res13: Long = 23
~~~
