
# Don’t Worry! How to Build a Data Lake in Oracle Big Data Service - BYOL [HOL2225]

## Abstract

Data volume worldwide is increasing by the second every day. Efficient methods are needed to handle this immense data growth and complexity. Having a data lake is an easy and fast way to store structured and unstructured data in a central repository. The data can be used for different purposes such as dashboards, big data processing, real-time analyses, or machine learning. 

This hands-on lab uses open source NYC bike rental data to build a data lake and load and stream the data from object storage in real time to get some quick insights and even build an interactive map. The session uses technologies such as Hive, Spark, Kafka, Python, Zeppelin, and object storage. 

## Introduction

Oracle offers a set of Big Data Journeys to help users get started using Oracle Cloud services with a purpose. This particular journey is designed to show you techniques you can use to build your own New Data Lake.

You will learn how to populate and analyze your data lake from a variety of file and streaming sources. You will learn how to execute real-time and batch processing with Oracle’s managed Hive, Spark, Kafka and Object Storage services in the cloud.

## Agenda

1. Introduction
2. Workshop Components
    1. Zeppelin
    2. Object Storage
    3. Hadoop
    4. Hive
    5. Kafka
    6. Spark
2. Notebook Basics
    1. Interpreter
    2. Shell, Markdown
3. Hive
    1. citibike dataset
    2. oci hdfs connector
    3. (create hive table from hdfs / object storage)
    4. scala read csv from object storage
    5. scala write csv to object storage
    6. pyspark read csv from object storage
    7. pyspark write csv to object storage
    8. show split
    9. write singel file to object storage
4. Kafka wip
    1. 

5. Poly & ADW
    1. Wallet & TNS ADMIN info
    2. cx_oracle cursor
    3. cx_oracle pandas 
    4. scala sql 
    5. create temp / global temp view
    6. pyspark sql / spark sql df 
    7. arrow enabled
    8. toPandas()
    9. back to pypark DF
    10. create hive table from tmp view
    11. query the table