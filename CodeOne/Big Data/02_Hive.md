# 02_Hive_Spark_ObjectStorage

In this notebook we will learn to utilize Hive, Spark and the Oracle Object Storage to store and interact with the data. But first look at our hands-on data. 

## About Citi Bike New York City

This user journey uses bike ride data available from the New York City bike share program known as Citi Bike NYC. Citi Bike consists of a fleet of bikes and a network of docking stations. Bikes can be unlocked from one station and returned to any other. Details about Citi Bike can be found here: https ://www.citibikenyc.com/.

We will use Citi Bike bike trip data to illustrate some of the capabilities of BDCS-CE and its sister cloud services throughout this journey.

Parts of the journey are inspired by this analysis: http ://toddwschneider.com/posts/a-tale-of-twenty-two-million-citi-bikes-analyzing-the-nyc-bike-share-system/

![](img/4.svg)

The data includes:

* Trip Duration (seconds)
* Start Time and Date
* Stop Time and Date
* Start Station Name
* End Station Name
* Station ID
* Station Lat/Long
* Bike ID
* User Type (Customer = 24-hour pass or 3-day pass user; 
* Subscriber = Annual Member)
* Gender (Zero=unknown; 1=male; 2=female)
* Year of Birth

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

Data notes:

Trip count and milage estimates include trips with a duration of greater than one minute. Milage estimates are calculated using an assumed speed of 7.456 miles per hour, up to two hours. Trips over two hours max-out at 14.9 miles. Once you opt into Ride Insights, the Citi Bike app will use your phone's location to record the route you take between your starting and ending Citi Bike station to give exact mileage. We only include trips that begin at publicly available stations (thereby excluding trips that originate at our depots for rebalancing or maintenance purposes).

## oci HDFS Connector

The Hadoop Distributed File System (HDFS) Connector lets your Apache Hadoop application read and write data to and from the Oracle Cloud Infrastructure Object Storage service.

This is an important component in the Oracle Data Lake architecture. 

We will use this throughout the hands-on to utilize the Oracle Object Storage. 

Let's see a simple command. 

```sh
%sh

hadoop fs -ls oci://bigdataprep@sehubpilot/citibike
```

## Get the New York Cite Bike Dataset

The first step will be to download a month of data. We will get our data from https: //www.citibikenyc.com/system-data. We will grab data for December 2016.

Once the data is downloaded, we will unzip it. Finally, we will store the unzipped data into a container in Object Store. The container does not need to exist-- the code will create it if needed. By default, the container will be named "journeyC". We will put our data into a "citibike" directory within the "journeyC" container.

In this step, we are illustrating how to move files into the Object Storage. We will store the original data file into a directory within our container called "citibike/raw". We will create a modified version of the data file (that has the header row removed) and store that into a directory called "citibike/modified".

This exercise shows how easy it is to push the data from hadoop to the Object Storage by using OCI HDFS connector. 

```sh
%sh

# the very first time you run a shell interpreter with zeppelin 0.70, the first few characters of output seem to get jumbled.
# since this paragraph is typically the first thing run, here is a silly workaround
echo "                                       "
sleep 5
echo "                                       "
# end silly workaround

export HADOOP_ROOT_LOGGER=WARN

CONTAINER=journeyC
DIRECTORY=citibike
FILENAME=201612-citibike-tripdata

echo "Object Storage Container Name        :" $CONTAINER
echo "Directory Name        :" $DIRECTORY
echo "Data Set name (remove .zip or .csv)  :" $FILENAME
echo "-----------------------------------------------------------------"

test -e $DIRECTORY || mkdir $DIRECTORY
cd $DIRECTORY
rm $FILENAME*

echo "Downloading $FILENAME.zip.  This may take a few minutes."
# https://www.citibikenyc.com/system-data links us to https://s3.amazonaws.com/tripdata/
wget -nv https://s3.amazonaws.com/tripdata/$FILENAME.zip 
echo "Extracting the csv from the zip file"
unzip $FILENAME.zip
#head -3 $FILENAME.csv
echo "Creating a new version of the file without header information named _nh.csv"
sed '1d' $FILENAME.csv > $FILENAME.nh.csv
ls -l

echo "Storing both versions of the csv files to Object Storage.  This may take a few minutes."
# we use the hadoop swift:// or oci:// driver to interact with the Object Store.

echo "List the directory. directory should be empty or missing"
hadoop fs -ls oci://journeyC@interactivetech/$DIRECTORY 
echo "Make the raw directory in Object Store"
hadoop fs -mkdir -p oci://journeyC@interactivetech/$DIRECTORY/raw 
echo "Copy First File to Object Store. May take a minute"
hadoop fs -put $FILENAME.csv oci://journeyC@interactivetech/$DIRECTORY/raw/$FILENAME.csv 
echo "Make the modified directory in Object Store"
hadoop fs -mkdir -p oci://journeyC@interactivetech/$DIRECTORY/modified 
echo "Copy Second File to Object Store.  May take a minute"
hadoop fs -put $FILENAME.nh.csv oci://journeyC@interactivetech/$DIRECTORY/modified/$FILENAME.nh.csv 
echo "Validate by listing the 2 csv files that got copied to Object Store (you should see 2 .csv files)"
hadoop fs -ls oci://journeyC@interactivetech/$DIRECTORY/raw 
hadoop fs -ls oci://journeyC@interactivetech/$DIRECTORY/modified
echo "done"
```

## About Apache Hive

The Apache Hive ™ data warehouse software facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. Structure can be projected onto data already in storage. A command line tool and JDBC driver are provided to connect users to Hive.

Hive is great, because it enables us to use SQL on top of HDFS and therefore use all the common and know SQL syntax that most people are familiar with. 

## Create a Hive Table

Our first step will be to define a Hive table on top of our CSV file.

The first example leverages a “managed” table where Hive manages the storage details (internally Hive will leverage HDFS storage). The second example leverages an “external” table where Hive will read the data directly from the Object Store.

We will use the hive command line running in the shell interpreter to create our tables.

**From HDFS File**

```sh
%sh 

DIRECTORY=citibike
FILENAME=201612-citibike-tripdata

echo "Data Set name (remove .zip or .csv)  :" $FILENAME
echo "-----------------------------------------------------------------"
echo ".."
echo "If this paragraph hangs on the SELECT count(*) FROM bike_trips, see the next paragraph for an explanation/resolution...."
echo ".."

cd $DIRECTORY

# run hive
hive <<EOF
DROP TABLE IF EXISTS bike_trips;

CREATE TABLE bike_trips ( 
TripDuration int,
StartTime timestamp,
StopTime timestamp,
StartStationID string,
StartStationName string,
StartStationLatitude string,
StartStationLongitude string,
EndStationID string,
EndStationName string,
EndStationLatitude string,
EndStationLongitude string,
BikeID int,
UserType string,
BirthYear int, 
Gender int
) 
ROW FORMAT delimited 
FIELDS TERMINATED BY ',' ;

LOAD DATA LOCAL INPATH '$FILENAME.nh.csv' into table bike_trips;

create table bike_trips_small as select * from bike_trips limit 50000;

SELECT count(*) FROM bike_trips;

exit;

EOF
```

**From Object Storage**

```sh
%sh

CONTAINER=journeyC
DIRECTORY=citibike
FILENAME=201612-citibike-tripdata

echo "Object Storage Container Name        :" $CONTAINER
echo "Data Set name (remove .zip or .csv)  :" $FILENAME
echo "-----------------------------------------------------------------"


# run hive
hive  <<EOF
DROP TABLE bike_trips_objectstore;

CREATE external TABLE bike_trips_objectstore ( 
TripDuration int,
StartTime timestamp,
StopTime timestamp,
StartStationID string,
StartStationName string,
StartStationLatitude string,
StartStationLongitude string,
EndStationID string,
EndStationName string,
EndStationLatitude string,
EndStationLongitude string,
BikeID int,
UserType string,
BirthYear int, 
Gender int
) 
ROW FORMAT delimited 
FIELDS TERMINATED BY ',' 
location 'oci://journeyC@interactivetech/citibike/modified/';


SELECT count(*) FROM bike_trips_objectstore;

exit;

EOF
```

**Show the hive tables.**

```sql
%jdbc(hive)

show tables;
```
### Working with the JDBC(Hive) interpreter

Zeppelin includes a JDBC interpreter that allows you run a query as a paragraph and do some nice formating of the results. In BDCS-CE, the JDBC interpreter has been pre-configured to connect to Hive.

You can work with the JDBC interpreter and connect to Hive like this:

```sql
%jdbc(hive)
describe bike_trips
```

```sql
%jdbc(hive)

select * from bike_trips
```

## Spark

Apache Spark™ is a unified analytics engine for large-scale data processing. 

Spark offers over 80 high-level operators that make it easy to build parallel apps. And you can use it interactively from the Scala, Python, R, and SQL shells.

We will use Spark to query data and utilize its in-memory power with Scala (Spark) and Pyspark (pyspark).

```scala
%spark

val df = spark.read.format("csv").option("header", "true").load("oci://bigdataprep@sehubpilot/citibike/raw/201612-citibike-tripdata.csv")


println(df.getClass)
z.show(df)
```

We read the CSV (or other formats; json, parquet, text and more) directly from the Object Storage by using SparkSQL and receive a Sark SQL Data Frame. 

```scala
%spark

df.write.format("csv").save("oci://bigdataprep@sehubpilot/citibike/raw/df_written_back.csv")
```

After some processing, we can also store a Spark Data Frame as CSV (or other formats) in the Oracle Object Storage. 

```sh
%sh

hadoop fs -ls oci://bigdataprep@sehubpilot/citibike/raw/df_written_back.csv
```
When we write the DF back, the CSV will be split into parts. Later, we will see how to prevent this. 

## Pyspark

We can also use the Python interpreter for Spark.

```python
%pyspark

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.load("oci://bigdataprep@sehubpilot/citibike/raw/201612-citibike-tripdata.csv", header="True" ,format="csv")

print(type(df))
z.show(df)
```

We can also read different formats directly from the Object Storage. The syntax is very similar to Scala, but we need to define a SparkSession. SparkSession provides a single point of entry to interact with underlying Spark functionality and allows programming Spark with DataFrame and Dataset APIs.

We receive a Pyspark SQL Data Frame. 

```python
%pyspark

df.write.option("header", "true").csv("oci://bigdataprep@sehubpilot/citibike/raw/write_back_with_python.csv")
```

Of course, we can also write it back into the Oracle Object Storage.

Also here, the csv is split into parts. However, when storing into Object Storage this is not necessary. We can prevent this by using `coalesce(1)`. 

```python
%pyspark

df.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("oci://bigdataprep@sehubpilot/citibike/raw/one_part.csv/")
```
Let's have a look. 

```sh
%sh

hadoop fs -ls oci://bigdataprep@sehubpilot/citibike/raw/test3.csv/
```