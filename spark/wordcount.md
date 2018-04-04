(base) C:\Users\user>spark-shell
~~~
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
2018-04-04 13:27:48 WARN  Utils:66 - Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
Spark context Web UI available at http://192.168.3.105:4041
Spark context available as 'sc' (master = local[*], app id = local-1522816068942).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.3.0
      /_/

Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_161)
Type in expressions to have them evaluated.
Type :help for more information.

scala> sc
res0: org.apache.spark.SparkContext = org.apache.spark.SparkContext@3eb9c575
~~~
scala> val textFile = sc.textFile("file:///C:/opt/spark-2.2.1-bin-hadoop2.7/README.md")  
~~~
textFile: org.apache.spark.rdd.RDD[String] = file:///C:/opt/spark-2.2.1-bin-hadoop2.7/README.md MapPartitionsRDD[3] at textFile at <console>:24
~~~
scala> textFile.first
~~~
res2: String = # Apache Spark
~~~
scala> val tokenizedFileData = textFile.flatMap(line=>line.split(" "))
~~~
tokenizedFileData: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[4] at flatMap at <console>:25
~~~
scala> tokenizedFileData.first
~~~
res3: String = #
~~~
scala> tokenizedFileData.take(5)
~~~
res4: Array[String] = Array(#, Apache, Spark, "", Spark)
~~~
scala> val countPrep = tokenizedFileData.map(word=>(word,1))
~~~
countPrep: org.apache.spark.rdd.RDD[(String, Int)] = MapPartitionsRDD[5] at map at <console>:25
~~~
scala> countPrep.first
~~~
res5: (String, Int) = (#,1)
~~~
scala> countPrep.take(5)
~~~
res6: Array[(String, Int)] = Array((#,1), (Apache,1), (Spark,1), ("",1), (Spark,1))
~~~
scala> val counts = countPrep.reduceByKey((accumValue, newValue)=>accumValue + newValue)
~~~
counts: org.apache.spark.rdd.RDD[(String, Int)] = ShuffledRDD[6] at reduceByKey at <console>:25
~~~
scala> counts.first
~~~
res7: (String, Int) = (package,1)
~~~
scala> counts.take(5)
~~~
res8: Array[(String, Int)] = Array((package,1), (this,1), (Version"](http://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version),1),
(Because,1), (Python,2))
~~~
scala> val sortedCounts = counts.sortBy(kvPair=>kvPair._2, false)
~~~
sortedCounts: org.apache.spark.rdd.RDD[(String, Int)] = MapPartitionsRDD[11] at sortBy at <console>:25
~~~
scala> sortedCounts.saveAsTextFile("file:///c:/WordCount.txt")  
  
scala> tokenizedFileData.countByValue
~~~
res10: scala.collection.Map[String,Long] = Map(site, -> 1, Please -> 4, Contributing -> 1, GraphX -> 1, project. -> 1, "" -> 71, for -> 12, find -> 1, Apache ->
 1, package -> 1, Hadoop, -> 2, review -> 1, Once -> 1, For -> 3, name -> 1, this -> 1, protocols -> 1, Hive -> 2, in -> 6, "local[N]" -> 1, MASTER=spark://host
:7077 -> 1, have -> 1, your -> 1, are -> 1, is -> 6, HDFS -> 1, Data. -> 1, built -> 1, thread, -> 1, examples -> 2, developing -> 1, using -> 5, system -> 1, t
han -> 1, Shell -> 2, mesos:// -> 1, 3"](https://cwiki.apache.org/confluence/display/MAVEN/Parallel+builds+in+Maven+3). -> 1, easiest -> 1, This -> 2, -T -> 1,
[Apache -> 1, N -> 1, <class> -> 1, different -> 1, "local" -> 1, README -> 1, online -> 1, spark:// -> 1, return -> 2, Note -> 1, if -> 4, project -> 1, Sca...

scala>
~~~
