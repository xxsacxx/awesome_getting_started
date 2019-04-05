from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.functions import explode
from pyspark.sql.functions import col
from pyspark.sql import functions as F
import json,string,random,sys,time
from pyspark.sql import SparkSession
from time import sleep


def dataStream(broker,topic):
  sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
  sc.setLogLevel("WARN")
  spark = SparkSession.builder.appName("PythonSparkStreamingKafka_RM_01").getOrCreate()
  ssc = StreamingContext(sc, 1)
  kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})
  print("hello")
  def process(rdd):
    df = spark.read.json(rdd)
    df.printSchema()
    df.show()
    x = df.select('user_id').head()
    path = x.asDict()['user_id']
    t = "/"+str(int(time.time())) + '.json'
    df.write.mode('append').json("hdfs://172.20.20.91:9000/anisha/process_sender_id1/"+path+"/"+topic+t)
    df.show()
    
  kvs.pprint()
  if(kvs):
    dstream =kvs.map(lambda x: (x[1]))
    dstream.foreachRDD(lambda x:process(x))
  else: 
    sleep(10)
    ssc.start() 

  ssc.start()  
  ssc.stop(stopSparkContext=True, stopGraceFully=True)
  print("hi")

if __name__ == "__main__":
    dataStream(sys.argv[1],sys.argv[2])


