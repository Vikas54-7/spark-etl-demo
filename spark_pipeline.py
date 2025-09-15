from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year

# Initialize Spark
spark = SparkSession.builder \
    .appName("ETL Pipeline - User Data") \
    .getOrCreate()

# Load raw CSV
df = spark.read.csv("data/input/users.csv", header=True, inferSchema=True)

# Transform: filter users older than 25 and add signup year
cleaned_df = df.filter(col("age") > 25) \
               .withColumn("signup_year", year(col("signup_date")))

# Save output to Parquet
cleaned_df.write.mode("overwrite").parquet("data/output/processed_users")

print("✅ ETL pipeline complete. Output saved in data/output/processed_users")

spark.stop()
