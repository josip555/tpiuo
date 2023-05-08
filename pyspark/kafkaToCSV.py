from os import system
import findspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col

findspark.init()

spark = SparkSession.builder.master("local[*]").appName("KafkaToCSVDemo").getOrCreate()

# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("startingOffsets","earliest") \
  .option("subscribe", "ethereum") \
  .load()

# Save dataframe stream to CSV file
stream = df.selectExpr("CAST(value AS STRING)").withColumns({"time": F.split('value', ',')[0], "priceUsd": F.split('value', ',')[1]}) \
  .selectExpr("CAST(time AS LONG)", "CAST(priceUsd AS DOUBLE)") \
  .writeStream \
  .outputMode("append") \
  .format("csv") \
  .option("checkpointLocation", "checkpoint/") \
  .option("path", "output/") \
  .start() \
  .awaitTermination()
