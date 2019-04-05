
./zkServer.sh start ### (for starting zookeeper)
bin/kafka-server-start.sh config/server.properties ### (for starting kafka)
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic spark_streaming ### (for creating topic 'spark_streaming')
bin/kafka-topics.sh --list --zookeeper localhost:2181 ### (list topics)
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic spark_streaming  ### (creates producers)
bin/kafka-console-consumer.sh --bootstrap-server  localhost:2181 --from-beginning --topic spark_streaming ### (creates consumers)
bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.0 ~/Downloads/utilities/spark/kafka_wordcount.py localhost:2181 spark_streaming 
### (deploys with spark streaming)


bin/kafka-console-consumer.sh --bootstrap-server  localhost:2181 --from-beginning --topic sparking
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic sparking
Hello