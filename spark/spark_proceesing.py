from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.functions import explode
from pyspark.sql.functions import col
from pyspark.sql import functions as F
import json
from pyspark.sql import SparkSession
from pyspark.sql import Row, DataFrame, SQLContext


def getSqlContextInstance(sparkContext):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(sparkContext)
    return globals()['sqlContextSingletonInstance']


# Convert RDDs of the words DStream to DataFrame and run SQL query
def process(time, rdd):
    	print("========= %s =========" % str(time))
        # Get the singleton instance of SparkSession
        sqlContext = getSqlContextInstance(rdd.context)

        # Convert RDD[String] to RDD[Row] to DataFrame
        #rowRdd = rdd.map(lambda w: Row(word=w))
        rowRdd = rdd.map(lambda w: Row(word=w[0], cnt=w[1]))
        #rowRdd.pprint()
        wordsDataFrame = sqlContext.createDataFrame(rowRdd, schema=['Name', 'Age'])
        wordsDataFrame.show()
        wordsDataFrame.printSchema()
        print(type(wordsDataFrame))
        wordsDataFrame.write.csv("hdfs://localhost:9000/sachin/d")

        # Creates a temporary view using the DataFrame.
        wordsDataFrame.createOrReplaceTempView("words")

        # Do word count on table using SQL and print it
        wordCountsDataFrame = \
             spark.sql("select SUM(cnt) as total from words")
        print(type(wordCountsDataFrame))
        wordCountsDataFrame.show()

       



sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")
spark=SparkSession.builder.appName('PythonSparkStreamingKafka_RM_01').getOrCreate()

ssc = StreamingContext(sc, 1)


directKafkaStream = KafkaUtils.createDirectStream(ssc, ['sparkss'], {"metadata.broker.list": 'localhost:9092'})


dstream =directKafkaStream.map(lambda x: (x[1]))

counts = dstream.flatMap(lambda line: line.split(" ")) \
     .map(lambda word: (word, 1)) \
     .reduceByKey(lambda a, b: a+b)

counts.foreachRDD(process)
dstream.pprint()


sample_list = [('Mona',20), ('Jennifer',34), ('John',20), ('Jim',26)]

# # Create a RDD from the list
rdd = sc.parallelize(sample_list)

# # Create a PySpark DataFrame
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])
names_df.printSchema()
print(type(names_df))
#names_df.write.csv("hdfs://localhost:9000/sachin/b")
# dstream.pprint()
# print(type(dstream))
    
# dstream.pprint()
#print(str(dstream))
# rdd=sc.parallelize(str(dstream))
# rdd.collect()
# # resultDF=spark.createDataFrame(rdd)
# resultDF = spark.read.json(rdd)
# resultDF.show()
#counts.pprint()
#dstream.saveAsTextFile("hdfs://localhost:9000/sachin/res_raw.txt")


# def sendRecord(record):
# 	print(record)
# 	record.pprint()
# 	record.saveAsTextFile("hdfs://localhost:9000/sachin/res_raw.txt")

# #names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])

# # df=dstream.foreachRDD(lambda rdd: (spark.createDataFrame(rdd)).show())
# #df.show()
# #dstream.foreachRDD(lambda rdd: rdd.foreach(sendRecord))

# def sendRecord(iter):

# 	for record in iter:
# 		print(record)

# 		#record.saveAsTextFile("hdfs://localhost:9000/sachin/")

      
#     #rdd.map(lambda record: record.saveAsTextFile("hdfs://localhost:9000/sachin/"))
    

# # dstream.foreachRDD(lambda rdd: rdd.foreachPartition(sendRecord))









ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminat