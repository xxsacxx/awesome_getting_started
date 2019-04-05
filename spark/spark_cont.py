from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.functions import explode
from pyspark.sql.functions import col
from pyspark.sql import functions as F
import json


sc.stop()
sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 1)


directKafkaStream = KafkaUtils.createDirectStream(ssc, ['spark_process'], {"metadata.broker.list": 'localhost:9092'})


dstream =directKafkaStream.map(lambda x: json.loads(x[1]))
dstream.pprint()
print(type(dstream))



ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminat