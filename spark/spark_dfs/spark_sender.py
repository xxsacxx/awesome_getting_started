from pyspark.sql import SparkSession 
from pyspark.sql.functions import explode 
from pyspark.sql.functions import split 
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import re
spark = SparkSession.builder.appName("DataExtraction").getOrCreate()
df = spark.read.json("file:///Users/onion7/Documents/BankingRegex1.json",multiLine=True)
df.printSchema()                                                            
x = df.select("messages.sender_id")
x.printSchema()
path = "/Users/onion7/Documents/sms_Develop/sms3/sms/"
f = open(path+"bankSendersMap1.json","r")
se1 = f.read()
se1 = se1.split("\n")
se = {}
for i in range(0,len(se1)-1):
        line = re.sub('[!@#$-]', '', se1[i].split(":")[0])
        se[line[2:].lower()] = se1[i].split(":")[1]


def TagSender(send):
        line = re.sub('[!@#$-]', '', send)
        if(line[2:].lower() in se.keys()):
             if(se[line[2:].lower()] != "Others"):
               return str(se[line[2:].lower()])
        else:
            return str('Others')



TagSender1 = udf(lambda z: TagSender(z),StringType())
x = x.withColumn("sender_id", explode(x.sender_id))
x = x.withColumn("sender_id", TagSender1(x.sender_id))
x.select("sender_id").show()

#df123 = df.withColumn("messages", explode(df.messages))
#df123 = df123.withColumn("sender_id", TagSender1(df123.mesaages.sender_id))
banksmap = {"DBS":0,"Allahabad":1,"Andhra":2, "HSBC":3, "Kotak":4, "Citi":5, "SBI":6, "HDFC":7, "ICICI":8, "Axis":9 ,"Federal":10, "IOB":11, "Standard Chartered":12, "Bank of Maharastra":13, "AMEX":14, "RBL":15,"PAYTM":16,"PHONEPE":17}
def dataExtract(a,b):
     if('pnr' in a.lower()):
         return "Travel"
 
extract = udf(dataExtract,StringType())
#df1231 = df123.withColumn("message", extract(df123.messages.message_body,df123.messages.sender_id))
#df1231.show()

hdfs_path ="hdfs://172.20.20.91:9000/anisha"
x = spark.read.format("json").load(hdfs_path,multiLine=True)
x = x.withColumn("messages", explode(x.messages))
x.show()
x = x.withColumn("sender_id", TagSender1(x.messages.sender_id))
x.select("user_id","sender_id","messages.message_body").write.json("hdfs://172.20.20.91:9000/anisha/process_sender_id1")


