# !apt-get install openjdk-8-jdk-headless -qq > /dev/null
# !wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz
# !tar xf spark-3.0.0-bin-hadoop3.2.tgz
# !pip install -q findspark

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"

# !pip install findspark
# !pip3 uninstall pyspark
# !pip3 install pyspark==3.0.2

import findspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
findspark.init()

products_table = spark.createDataFrame([
    ('milk', '0'),
    ('chocolate', '1'),
    ('car', '2'),
    ('cheese', '3')
]).toDF("name", "id")
products_table.show()

product_and_category = spark.createDataFrame([
    ('0', '0'),
    ('1', '1'),
    ('1', '2'),
    ('2', None),
    ('3', '0'),
    ('3', '3')
]).toDF("name_id", "category_id")
product_and_category.show()

categories_table = spark.createDataFrame([
    ('dairy', '0'),
    ('sweets', '1'),
    ('confectionery', '2'),
    ('cheeses', '3')
]).toDF("category", "id")
categories_table.show()

df_rez = product_and_category.join(categories_table, categories_table.id == product_and_category.category_id, how="inner").join(products_table, products_table.id == product_and_category.name_id, how="full_outer")
df_rez.select(df_rez.category,df_rez.name).show()
