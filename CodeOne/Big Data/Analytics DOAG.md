# Analytics DOAG

“Don’t worry ! How to Build and Populate a Data Lake in the Oracle Cloud”

This workshop will be held in the course of the Knowledge Transfer Session (10 – 12 o'clock, 26th of March, 2019) at the DOAG Oracle DATA ANALYTICS 2019 in Bruehl, Germany.

## Abstract

Der weltweite Datenbestand wächst stetig. Aberdeen Research schätzt, dass der Datenbestand der Unternehmen im Schnitt mit einer jährlichen Wachstumrate von über 50% wächst. Dabei werden Daten auf unterschiedliche Art und Weise erzeugt, um dann im Anschluss weiter verarbeitet, ausgetauscht und abgespeichert zu werden. Darüber hinaus werden Daten und ihre Beziehungen zueinander immer komplexer. Es bedarf daher effizienter Methoden, um die steigenden Datenvolumina und die zunehmende Datenkomplexität zu managen. 

Ein ‘Data Lake’ erlaubt hierbei ein unkompliziertes und schnelles Speichern von strukturierten und unstrukturierten Daten in einem zentralen Repository. Die Daten können dann für verschiedene Zwecke wie Dashboards, Big Data Processing, Echtzeitanalyse oder Machine Learning weiter verwendet werden. Dieser Workshop zeigt anhand von Open Source Daten des NYC-Bike-Verleihsystem, wie man mit der Oracle Big Data Cloud einen Data Lake erstellen kann, um im Anschluss wertvolle Insights aus den Daten zu gewinnen. Dabei wird auf Open-Source Technologien wie Hadoop, Hive, Spark, Kafka und R eingegangen.

## Big Data Cloud Service - Compute Edition

Oracle Big Data Cloud combines open source technologies such as Apache Spark and Apache Hadoop with unique innovations from Oracle to deliver a complete Big Data platform for running and managing Big Data Analytics applications. Big Data Cloud leverages Oracle’s Infrastructure Cloud Services to deliver a secure, elastic, integrated platform for all Big Data workloads. 

You can:

* Spin up multiple Hadoop or Spark clusters in minutes
* Use built-in tools such as Apache Zeppelin to understand your data, or use the jobs API to run non-interactive jobs
* Use open interfaces to integrate third-party tools to analyze your data
* Launch multiple clusters against a centralized data lake to achieve data sharing without compromising on job isolation
* Create small clusters or extremely large ones based on workload and use-cases
* Elastically scale the compute and storage tiers independently of one another, either manually or in an automated fashion
* Pause a cluster when not in use
* Use REST APIs to monitor, manage, and utilize the service

### Big Data Journey: New Data Lake Workshop

Oracle offers a set of Big Data Journeys to help users get started using Oracle Cloud services with a purpose. This particular journey is designed to show you techniques you can use to build your own New Data Lake.

![1548755367000](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548755367000.png)

* Real-time and Batch
* Data Science Friendly
* Scalable
* Agile
* Economical

You will learn how to populate and analyze your data lake from a variety of file and streaming sources. You will learn how to execute real-time and batch processing with Oracle’s managed Hive, Spark, Kafka and Object Storage services in the cloud.

The New Data Lake workshop will use a series of tutorials running in Zeppelin Notebook. The tutorials will leverage the New York City CitiBike data to illustrate how the New Data Lake can work easily with both batch and real-time data.

![1548755427131](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548755427131.png)

#### Provisioning Oracle Big Data Cloud

The Oracle Big Data Cloud (BDC) enables you to rapidly, securely, and cost-effectively leverage the power of an elastic, integrated Big Data Infrastructure to unlock the value in Big Data. In this lab, we will walk you through the steps to quickly configure and create a Big Data Cloud instance. When done you will see how to view the configuration and layout of your instance using the Oracle Big Data Console.

We will create a container in the Storage Cloud to hold the files and data used by this workshop. This container will be the "default" container used by the BDC instance we will create. And we will upload to this container a special "bootstrap.sh" file that will be used to customize our BDC instance as it is provisioned.

![1548756069603](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548756069603.png)

Fill in the name journeyC and leave the storage tier as standard. 


![1548756129110](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548756129110.png)

Download the bootstrap.zip file from here: https://github.com/millerhoo/journey2-new-data-lake/raw/master/workshops/journey2-new-data-lake/files/100/bootstrap.zip

Be sure to unzip the bootstrap.zip file to extract/save the bootstrap.sh file to a directory on your local computer.

Click on your journeyC bucket to open it. Click on Upload Objects. Select the bootstrap.sh file. Make sure to name the file bdcsce/bootstrap/bootstrap.sh, which will create the folder logic that we want.

![1548756264087](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548756264087.png)

Now, lets provision a Big Data instance. Fill in the necessary information. 

| Name                | Comment                                                      |
| ------------------- | ------------------------------------------------------------ |
| Instance Name       | Choose a name that is unique within the tenant domain that will be used to identify this new instance. Instance name cannot have more than 50 characters. It must start with a letter, and contain only letters and numbers; no special characters. |
| Description         | You may add an optional description that can be used to help identify this new service. The description is only used during service list display and is not used internally by Service Manager |
| Notification Email  | Provisioning status update(s) will be sent to the specified e-mail. |
| Region              | Name of the Compute Region.                                  |
| Availability Domain | Name of the Availability Domain within the Compute Region.   |
| Subnet              | Select a subnet for your Instance. Subnets can be created using [OCI Console](https://console.eu-frankfurt-1.oraclecloud.com/) and appropriate access must be granted for PaaS Service Manager. Refer to [details](http://www.oracle.com/pls/topic/lookup?ctx=cloud&id=oci_general_paasprereqs)
If you want the subnet to be assigned automatically, then select **No Preference**. |
| Tags                | Select available tags for assignment, or define new tags and assign to the service instance.You can use tags to search for and categorize your instances. |

![1548758330250](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548758330250.png)

|                                       |                                                              |
| ------------------------------------- | ------------------------------------------------------------ |
| Deployment Profile                    | Deployment Profile determines the component makeup and tuning of the instance, to optimize it for specific workloads. "Full" - Comes with Spark, MapReduce, Zeppelin, Hive, Spark Thrift, Big Data File System. "Basic" - Comes with Spark, MapReduce and Zeppelin. "Snap" - Comes with Snap, Spark and Zeppelin. |
| Number of Nodes                       | Choosing 3 or more nodes provides high availability (HA) with multiple master nodes. If fewer than 3 nodes, critical services will run on a single master node without HA. Enter a value between 1 and 100 |
| Compute Shape                         | Select a compute shape for BDC cluster. For Clusters with 4 or more nodes, the NameNodes always get provisioned as OC2M. Oracle recommends OC3M or higher shapes for the remaining nodes. Customers are recommended to not choose the High I/O and Dense I/O shapes appearing in the drop-down as these have been enabled for specific beta use-cases. |
| Queue Profile                         | Queue profile defines job queues appropriate for different types of workloads. Each queue has minimum guaranteed capacity and maximum allowed capacity. "Preemption On" option provides three queues with preemption - api(min:50, max:100), interactive(min:40, max:100) and default (min:10, max:100). "Preemption Off" option provides two queues without preemption - dedicated(min:80, max:80) and default(min:20, max:20). Queue configuration can be customized on Cluster Manager UI |
| Spark Version                         |                                                              |
| SSH Public Key                        | You can choose to enter a public key name, the public key text or have the service generate the key to use for service host access. SSH Access is disabled by default. To enable it, edit the Access Rules. |
| User Name                             | User name for the Big Data Cloud Console and REST APIs for job submission. User name admin is not allowed. |
| Password & Confirm Password           | Password for the Cluster user. Password must be at least 8 characters long with at least one lower case letter, one upper case letter, one number and one special character. For example, Ach1z0#d |
| OCI Cloud Storage URL                 | OCI Cloud Storage URL. E.g., https://objectstorage.us-phoenix-1.oraclecloud.com/ . For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| OCI Cloud Storage Bucket URL          | OCI Cloud Storage Bucket URL. E.g., oci://bucket1@tenant1/ where bucket1 is the default bucket where application binaries and application logs are stored. tenant1 is your Tenancy. For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| OCI Cloud Storage User OCID           | OCI Cloud Storage User OCID. Refer to Required Keys and OCIDs in Developer Tools documentation of Oracle Cloud Infrastructure. For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| OCI Cloud Storage PEM Private Key     | OCI Cloud Storage PEM Private Key. This is the private PEM key file which has to be generated without a passphrase. Refer to How to Generate an API Signing Key section in Oracle Cloud Infrastructure documentation. For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| OCI Cloud Storage PEM Key Fingerprint | OCI Cloud Storage PEM Key Fingerprint. This has to be generated. Refer to How to Generate an API Signing Key section in Oracle Cloud Infrastructure documentation. For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| OCI Cloud Storage PEM Key Fingerprint | OCI Cloud Storage PEM Key Fingerprint. This has to be generated. Refer to How to Generate an API Signing Key section in Oracle Cloud Infrastructure documentation. For more details, refer to the tutorial at https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:24147 showing how to create an Oracle Big Data Cloud instance on Oracle Cloud Infrastructure. |
| Use High Performance Storage          | Use High Performance Storage for HDFS (Not available on Oracle Cloud at Customer or Oracle Cloud Infrastructure)
Select this to use high performance storage for HDFS. With this option the storage attached to nodes uses SSDs (solid state drives) instead of HDDs (hard disk drives). Use this option for performance-critical workloads. An additional cost is associated with this type of storage. |
| Usable HDFS Storage (GB)              | Usable HDFS Storage, value in GB. Actual allocated physical storage will be twice the value specified for HDFS replication plus additional 5% for intermediate logs |
| Usable BDFS Cache (GB)                | Usable Cache, value in GB. Actual allocated physical storage will be the value specified for BDFS plus additional 5% for intermediate logs. Oracle block storage has an inbuilt replication of 2x. Enter a value between 50 and 74000 |
| Total Allocated Storage (GB)          |                                                              |
| Association                           | On the Service Details page, complete the Associations section by selecting the services you’d like to associate with this cluster. You can associate a Big Data Cloud cluster with other Oracle Cloud services you've already provisioned. When you associate a cluster with another service, networking between the service instances is reconfigured so the instances can communicate with one another. This is helpful if you have Apache Spark jobs that require interaction between services or have some dependency. To associate a cluster with a service, you must already have an active subscription for that service |
|                                       | ![1548760369650](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548760369650.png) |
|                                       |                                                              |

#### Getting to know Big Data Cloud

You will use the Notebook feature of BDC to run a series of tutorials that show you different aspects of functionality. In this lab, you will learn how to work with the Zeppelin Notebook. You will also be introduced to the New York City Citi Bike dataset that we will use for experimentation. You will see how we can download some sample data and upload it to the Oracle Cloud Storage Object Store. And finally, another tutorial will show you how to interact with Hive.

Notebooks are used to explore and visualize data in an iterative and easily documented fashion. Oracle Big Data Cloud Service - Compute Edition uses Apache Zeppelin as its notebook interface and coding environment. Information about Zeppelin can be found here: https://zeppelin.apache.org/ .

Launch the Big Data Cluster Console for your BDC cluster. If this is your first time, you will likely need to allow your browser to accept the self-signed certificate for the web console application. You will be asked to provide a username/password. Use the username and password you defined earlier when you created the BDC instance (the username defaults to bdcsce_admin). 

Click on the Notebook tab. Expand the Journeys folder. Then expand the New Data Lake folder. Then click on the title of the "Tutorial 1 Notebook Basics" note.

*If you do not see the "Journeys" folder or the "Extras" folder, then the bootstrap.sh script did not work correctly. If this happened, most likely there was a problem with how you uploaded the bootstrap.sh and/or the exact syntax you specified for the Storage Cloud location when you provisioned your BDC instance. Sorry, but you will want to delete your instance and re-follow the Lab 100 instructions again paying close attention to the instructions around bootstrap and Storage Cloud.*

##### Notebook Basic

BDCS-CE includes a built-in Zeppelin notebook. Currently, BDCS-CE is using Zeppelin version 0.7.0(?). 

###### **About Interpreters**

The Zeppelin notebook is powered by Interpreters, which allow various technologies to be combined into a single, easily documented environment. The concept of Zeppelin interpreter allows any language/data-processing-backend to be plugged into Zeppelin. Currently, Zeppelin supports many interpreters such as Scala ( with Apache Spark ), Python ( with Apache Spark ), Spark SQL, JDBC, Markdown, Shell and so on. 

###### What is Zeppelin interpreter?

Zeppelin Interpreter is a plug-in which enables Zeppelin users to use a specific language/data-processing-backend. For example, to use Scala code in Zeppelin, you need %spark interpreter.

When you click the +Create button in the interpreter page, the interpreter drop-down list box will show all the available interpreters on your server.

![alt text](https://zeppelin.apache.org/docs/0.8.0/assets/themes/zeppelin/img/screenshots/interpreter_create.png "Logo Title Text 1")

###### **What is interpreter setting?**

Zeppelin interpreter setting is the configuration of a given interpreter on Zeppelin server. For example, the properties are required for hive JDBC interpreter to connect to the Hive server.

![alt text](https://zeppelin.apache.org/docs/0.8.0/assets/themes/zeppelin/img/screenshots/interpreter_setting.png)

Each notebook can be bound to multiple Interpreter Settings using setting icon on upper right corner of the notebook.

![int settings](https://zeppelin.apache.org/docs/0.8.0/assets/themes/zeppelin/img/screenshots/interpreter_binding.png)

The Interpreters currently offered with this version of BDCS-CE are, among others:

+ Markdown (%md)
+ Shell (%sh)
+ Spark with Scala (%spark)
+ Spark with Python (%pyspark)
+ Spark SQL (%sql)
+ Hive (%hive)
+ JDBC (%jdbc)
+ Angular

In this first tutorial, we will introduce you to the Markdown and Shell Interpreters.

###### **About the Markdown Interpreter (%md)**

The Markdown interpreter is used to add documentation to your notebooks.  To create a paragraph using the Markdown interpreter, use %md for the first line in the code editor.

Details about the markdown interpreter can be found here: <https://zeppelin.apache.org/docs/0.7.0/interpreter/markdown.html>

**Some simple examples...**

**Add Emphasis** using one or more \*

Create a list using \+

+ item
+ item
+ item



For more, check out the Markdown cheatsheet at <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>

_Hint: View the editor for this section to see the actual Markdown code used_

**###### About the Shell Interpreter (%sh)**

The shell interpreter runs linux shell commands as the zeppelin user on the BDCS-CE server running zepellin.  It can be handy way to check zeppelin log files, pull files into BDCS-CE, interact with HDFS, or change/install software.  SSH can also be used, but running shell commands via the notebook can be more natural and self-documenting.

By default, the zeppelin user does not have sudo privileges.  But in the next Tutorial, we will show how you can add zeppelin to the authorized sudo users list.

The following paragraph has some sample shell command examples.

```sh
%sh
echo "running whoami"
whoami
echo ".."
echo "running pwd"
pwd
echo ".."
echo "running a hadoop command"
hadoop fs -ls /user
echo ".."
echo "done"
```

##### Hive

###### About Citi Bike New York City

This user journey uses bike ride data available from the New York City bike share program known as Citi Bike NYC.  Citi Bike consists of a fleet of bikes and a network of docking stations.  Bikes can be unlocked from one station and returned to any other.  Details about Citi Bike can be found here: <a href="https://www.citibikenyc.com/" target="_blank">https ://www.citibikenyc.com/</a>.

We will use Citi Bike bike trip data to illustrate some of the capabilities of BDCS-CE and its sister cloud services throughout this journey.

Parts of the journey are inspired by this analysis: <a href="http://toddwschneider.com/posts/a-tale-of-twenty-two-million-citi-bikes-analyzing-the-nyc-bike-share-system/" target="_blank">http ://toddwschneider.com/posts/a-tale-of-twenty-two-million-citi-bikes-analyzing-the-nyc-bike-share-system/</a>

![NYC](https://d21xlh2maitm24.cloudfront.net/nyc/CitiBike_Logo_p.svg?mtime=20160427183115)

The data includes:

* Trip Duration (seconds)
* Start Time and Date
* Stop Time and Date
* Start Station Name
* End Station Name
* Station ID
* Station Lat/Long
* Bike ID
* User Type (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member)
* Gender (Zero=unknown; 1=male; 2=female)
* Year of Birth

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure).

Data notes:

Trip count and milage estimates include trips with a duration of greater than one minute.
Milage estimates are calculated using an assumed speed of 7.456 miles per hour, up to two hours. Trips over two hours max-out at 14.9 miles. Once you opt into Ride Insights, the Citi Bike app will use your phone's location to record the route you take between your starting and ending Citi Bike station to give exact mileage.
We only include trips that begin at publicly available stations (thereby excluding trips that originate at our depots for rebalancing or maintenance purposes).

###### **Downloading Citi Bike data and Storing in the Object Store**

The first st ep will be to download a month of data.  We will get our data from <a href="https://www.citibikenyc.com/system-data" target="_blank">https: //www.citibikenyc.com/system-data</a>.  We will grab data for December 2016.

Once the data is downloaded, we will unzip it.  Finally, we will store the unzipped data into a container in Object Store.  The container does not need to exist-- the code will create it if needed.  By default, the container will be named "journeyC".  We will put our data into a "citibike" directory within the "journeyC" container.

Here is a logical diagram of the architecture we will use in these tutorials:
![Architecture](https://raw.githubusercontent.com/oracle/learning-library/master/workshops/journey2-new-data-lake/images/snap0012028.jpg)

In this step, we are illustrating how to move files into the Object Storage.  We will store the original data file into a directory within our container called "citibike/raw".  We will create a modified version of the data file (that has the header row removed) and store that into a directory called "citibike/modified".

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



###### **About Apache Hive**

The Apache Hive ™ data warehouse software facilitates reading, writing, and managing large datasets residing in distributed storage using SQL. Structure can be projected onto data already in storage. A command line tool and JDBC driver are provided to connect users to Hive.

In this tutorial, we will use Hive to enable SQL queries against our Citi Bike .csv dataset.

Learn more about Hive <a href="https://hive.apache.org/" target="_blank">here</a>

###### **Create a Hive Table**

Our first step will be to define a Hive table on top of our CSV file.  We will show (x?) variations.  The first example leverages a "managed" table where Hive manages the storage details (internally Hive will leverage HDFS storage).  The second example leverages an "external" table where Hive will read the data directly from the Object Store.

We will use the hive command line running in the shell interpreter to create our tables.

###### **Create an Hive table from local file**

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

###### **Create an Hive table from a file in the object storage** 

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

###### Show the hive tables.

```
%jdbc(hive)

show tables;
```
```sh
%sh

hive  <<EOF
show tables;
EOF
```

```sh
%sh

hive  <<EOF
select 
 case when a.gender=1 then 'Male' when a.gender=2 then 'Female' else 'unknown' end gender ,
        a.trip_count 
from (select gender, count(*) trip_count from bike_trips
group by gender) a;
EOF
```

###### **Working with the JDBC(Hive) interpreter**

Zeppelin includes a JDBC interpreter that allows you run a query as a paragraph and do some nice formating of the results.  In BDCS-CE, the JDBC interpreter has been pre-configured to connect to Hive.


You can work with the JDBC interpreter and connect to Hive like this:

    %jdbc(hive)
    select * from my_table;
```sql
%jdbc(hive)
describe bike_trips
```

```sql
%jdbc(hive)
show create table bike_trips
```

```sql
%jdbc(hive)

select 
 case when a.gender=1 then 'Male' when a.gender=2 then 'Female' else 'Unknown' end gender,  a.trip_count 
from (select gender, count(*) trip_count from bike_trips
group by gender) a
```

```sql
%jdbc(hive)

select * from bike_trips
```

```sql
%jdbc(hive)

select gender, dayofweek, count(*)
from (    select date_format(`StartTime`,"E") dayofweek,
          case when gender=1 then 'Male' when gender=2 then 'Female' else 'Unknown' end gender 
from bike_trips) bike_times 
group by gender, dayofweek
```

```sql
%jdbc(hive)

select (2016 - a.birthyear) age, count(*) number_trips from bike_trips as a
where birthyear is not null
group by birthyear
```

##### Maps

###### About Displaying Maps in Zeppelin

This example will plot our top bike pickup/dropoff stations on a map.  To do so, 

 + We'll use Spark code to gather the data that we will use to define specific markers to add to our map.  We will bind this marker data to a named angular variable.  Angular is the framework that Zeppelin uses for its UI. <a href="https://angularjs.org" target="_blank">here</a>
 + Then we will create a %angular paragraph to hold some custom HTML/javascript code.  This is the paragraph that will display the map.  Our code will use the javascript Leaflet project (<a href="http://leafletjs.com/examples/quick-start/" target="_blank">here</a>) to create an html/javascript map object.  As part of our javascript, we'll instruct it to listen for changes to our named angular variable that we are populating in our spark paragraph.  When the angular variable changes, our code will re-draw the markers on the map.

This approach is derived from examples on the internet, such as <a href="https://gist.github.com/granturing/a09aed4a302a7367be92" target="_blank">here</a> or <a href="https://community.hortonworks.com/articles/90320/add-leaflet-map-to-zeppelin-notebook.html" target="_blank">here</a>, that are all based on a similar approach.  

###### Our First Map - Top 10 Pickup Stations

To get started, we will plot the 10 top pickup stations on a map.  We will have 1 paragraph which will use Spark and Spark SQL to query our bike_trips table and save the results into an angular variable.  And we will have 1 paragraph that contains the html/javascript to display our map. 

+ Run the "Spark code for our first map" to gather the data for our map,
+ Then run the "HTML/Javascript for our first map" to display the map with the selected data

```scala
%spark


//a previous tutorial placed the csv file into your Object Store citibike container
//notice the use of the swift://CONTAINER.default/ syntax
//define container and directory as variable
val Container = "journeyC"
val Directory = "citibike"

//initate df variable
var df: org.apache.spark.sql.DataFrame = null

//load data from object storage into df
if( "oci://journeyC@interactivetech".contains("swift")  ){
         println("Running on OCI-C");
   //We will use the bdfs (alluxio) cached file system to access our object store data...
   df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema","true").load("bdfs://localhost:19998/"+Directory+"/raw/201612-citibike-tripdata.csv")
} else {
         println("Running on OCI");
   df = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").load("oci://journeyC@interactivetech/"+Directory+"/raw/201612-citibike-tripdata.csv")
}


// If you get this error message:
// java.lang.IllegalStateException: Cannot call methods on a stopped SparkContext.
// Then go to the Settings tab, then click on Notebook.  Then restart the Notebook.  This will restart your SparkContext

//create temporay view
df.createOrReplaceTempView("bike_trips_temp")

//Define a class for the structure of the data we will be passing to the map javascript code
case class Stations(ridetype: String, station: String, trips: String, lat: Double, lon: Double)

//Unbind angular variable in case it already exists from previous run
z.angularUnbind("topstations") 

//Define a new dataframe based off a query
val topstationsDF = sqlContext.sql(s"""select "Start" ridetype, `Start Station Name` station,`Start Station Latitude` lat,`Start Station Longitude` lon, count(*) trips from bike_trips_temp 
group by `Start Station Name`,`Start Station Latitude`,`Start Station Longitude`
order by count(*) desc limit 10""")


//Map the DF into an Array of Stations
var items = topstationsDF.map(b => Stations(b(0).toString, b(1).toString, "Pickups:"+b(4).toString, b(2).toString.toDouble, b(3).toString.toDouble)).collect

//Bind the TopStations (as an Array) to an Angular variable named topstations
z.angularBind("topstations", items) 

println("..")
println("done")

```

Some comments for the Map below

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.css" />
```
Leaflet is the leading open-source JavaScript library for mobile-friendly interactive maps.

Leaflet is designed with simplicity, performance and usability in mind. It works efficiently across all major desktop and mobile platforms, can be extended with lots of plugins, has a beautiful, easy to use and well-documented API and a simple, readable source code that is a joy to contribute to.

```html
<div id="firstmap" style="height: 600px; width: 100%"></div>
```
Dimensions

```javascript
function initMap()
```

The Maps JavaScript API lets you customize maps with your own content and imagery for display on web pages and mobile devices. The Maps JavaScript API features four basic map types (roadmap, satellite, hybrid, and terrain) which you can modify using layers and styles, controls and events, and various services and libraries.

```html
%angular
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.css" />
<div id="firstmap" style="height: 600px; width: 100%"></div>

<script type="text/javascript">

//based on https://gist.github.com/granturing/a09aed4a302a7367be92, https://community.hortonworks.com/articles/90320/add-leaflet-map-to-zeppelin-notebook.html, etc

function initMap() {
    //open up a map around NYC at zoom level 13
    var map = L.map('firstmap', {preferCanvas: true}).setView([40.75, -73.99], 13);

    //define the background tile layer using OpenStreet maps.  Leaflet can work with other providers, too
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 16,
        minZoom: 11
    }).addTo(map);

    var geoMarkers = L.layerGroup().addTo(map);
    
    // setup a custom icon for markers. See https://github.com/pointhi/leaflet-color-markers
    var greenIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });
    
    var redIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });

    var el = angular.element($('#firstmap').parent('.ng-scope'));
    angular.element(el).ready(function() {
        
        //listen for changes to the angular variable called stations
        window.locationWatcher = el.scope().compiledScope.$watch('topstations', function(newValue, oldValue) {

            //loop through each entry in our stations variable and add it as a marker
            angular.forEach(newValue, function(station) {
                var marker = L.marker([station.lat, station.lon])
                marker.addTo(geoMarkers);  

            });
        })
    });
}

if (window.locationWatcher) {
    // clear existing watcher otherwise we'll have duplicates
    window.locationWatcher();
}

// ensure we only load the script once, seems to cause issues otherwise
if (window.L) {
    initMap();
} else {
    console.log('Loading Leaflet library');
    var sc = document.createElement('script');
    sc.type = 'text/javascript';
    sc.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.js';
    sc.onload = initMap;
    sc.onerror = function(err) { alert(err); }
    document.getElementsByTagName('head')[0].appendChild(sc);
}
</script>


```
###### A more complex example - Top Pickup and Dropoff locations for certain times of day

Now that we have shown a simple example of a map, we will show a more complex example using a parameter-driven query with multiple map markers and layers.

To run this example:

- Use the Query Parameters paragraph to choose the time frame for the query as well as how many of the Top pickup and dropoff stations to show on the map.
- Then run the Query Parameters paragraph.  This will query the desired data (by automatically running the "Spark code for the more complex map" paragraph)
- Once the data has been queried (takes about 20 seconds), the "More Complex Map" will be updated.  If the map is not showing, then play the "More Complex Map" paragraph to make it visible.
  -- Pickups are drawn in green.  Dropoffs are in red.
  -- Use the layers control in the upper right of the map to show/hide pickup and dropoff stations.
  -- The size of the circle on the map represents the number of pickups/dropoffs for that station during the selected time frame.

```scala
%spark
z.angularBind("BIND_topN", z.select("Top N","10",Seq(("5","5"),("10","10"),("20","20"),("50","50"),("100","100"))))
z.angularBind("BIND_dayOfWeek", z.select("dayOfWeek", "All", Seq(("All", "All"),
                         ("MonFri", "Mon-Fri"), ("SatSun","Weekend")))  )
z.angularBind("BIND_hourOfDay", z.select("hourOfDay", "All", Seq(("All", "All"),
                         ("Morning", "7am to 10am"), ("Midday","11am to 3pm"),("Afternoon","4pm to 7pm"),
                         ("Evening","8pm to 11pm"),("LateNite","12am to 6am")))  )
                         
z.run("20170417-105408_1898939870")   
						 
```

```scala
%spark

//Define a class for the structure of the data we will be passing to the map javascript code
case class Stations(ridetype: String, station: String, trips: String, lat: Double, lon: Double, radius: Double)

z.angularUnbind("stations")

{
//Be sure to have run Part 1 prior to running this as this assumes that the bike_trips table is part of your current session

//Define some UI widgets for data selection parameters
// Learn more here: https://zeppelin.apache.org/docs/0.6.1/interpreter/spark.html#form-creation


//Use our UI values to define custom SQL
var limitString = " limit "+z.angular("BIND_topN")
var whereString = " where 1=1 "

if (z.angular("BIND_dayOfWeek")=="MonFri") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"E") in ("Mon","Tue","Wed","Thu","Fri") """
} else if (z.angular("BIND_dayOfWeek")=="SatSun") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"E") in ("Sat","Sun") """
}

if (z.angular("BIND_hourOfDay")=="Morning") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("7","8","9","10") """
} else if (z.angular("BIND_hourOfDay")=="Midday") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("11","12","13","14","15") """
} else if (z.angular("BIND_hourOfDay")=="Afternoon") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("16","17","18","19") """
} else if (z.angular("BIND_hourOfDay")=="Evening") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("20","21","22","23") """
} else if (z.angular("BIND_hourOfDay")=="LateNite") {
    whereString = whereString+ s""" AND date_format(`Start Time`,"H") in ("0","1","2","3","4","5","6") """
}

println("WHERE STRING: "+whereString)

//Define a new dataframe based off a query
var stations = sqlContext.sql(s"""select "Start" ridetype, `Start Station Name` station,`Start Station Latitude` lat,`Start Station Longitude` lon, count(*) trips from bike_trips_temp """ +
whereString + s"""
group by `Start Station Name`,`Start Station Latitude`,`Start Station Longitude`
order by count(*) desc """ + limitString)


//Map the DF into an Array of Stations
var items1 = stations.map(b => Stations(b(0).toString, b(1).toString, "Pickups:"+b(4).toString, b(2).toString.toDouble, b(3).toString.toDouble,  b(4).toString.toDouble/8 )).collect



//now do the same for top ending stations
stations = sqlContext.sql(s"""select "End" ridetype, `End Station Name` station,`End Station Latitude` lat,`End Station Longitude` lon, count(*) trips from bike_trips_temp """ +
whereString + s"""
group by `End Station Name`,`End Station Latitude`,`End Station Longitude`
order by count(*) desc """ + limitString)
	
//Map the DF into an Array of Stations.  Offset the lat,lon by a bit so you see both Start and End markers
var items2 = stations.map(b => Stations(b(0).toString, b(1).toString, "Dropoffs:"+b(4).toString, b(2).toString.toDouble+0.0001, b(3).toString.toDouble+0.0001, b(4).toString.toDouble/8)).collect

//combine the two arrays
val combined=items1 ++ items2

//Bind the Stations to an Angular variable named stations
z.angularBind("stations", combined) 

println("done")
}

```

```html
%angular
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.css" />
<div id="map" style="height: 600px; width: 100%"></div>

<script type="text/javascript">

//based on https://gist.github.com/granturing/a09aed4a302a7367be92, https://community.hortonworks.com/articles/90320/add-leaflet-map-to-zeppelin-notebook.html, etc

function initMap() {
    //open up a map around NYC at zoom level 13
    var map = L.map('map', {preferCanvas: true}).setView([40.75, -73.99], 13);

    //define the background tile layer using OpenStreet maps.  Leaflet can work with other providers, too
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        maxZoom: 16,
        minZoom: 11
    }).addTo(map);

    //define a new LayerGroup which will hold our markers
    var startMarkers = L.layerGroup().addTo(map);
    var endMarkers = L.layerGroup().addTo(map);

    var overlayMaps = {
    "Top Pickup Stations": startMarkers,
    "Top Dropoff Stations": endMarkers
    };
    
    //add a Control to the map to let the user click the Marker layer off and on
    L.control.layers(null, overlayMaps).addTo(map);
    
    // keep track of our markers, so we can remove them later
    var markers = new Array();
    
    // setup a custom icon for markers. See https://github.com/pointhi/leaflet-color-markers
    var greenIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-green.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });
    
    var redIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [12, 20],
      iconAnchor: [6, 20],
      popupAnchor: [1, -17],
      shadowSize: [20, 20]
    });

    var el = angular.element($('#map').parent('.ng-scope'));
    angular.element(el).ready(function() {
        
        //listen for changes to the angular variable called stations
        window.locationWatcher = el.scope().compiledScope.$watch('stations', function(newValue, oldValue) {
             //startMarkers.clearLayers(); -- this did not work for me, so I use the for loop below to delete old markers
            for(i=0;i<markers.length;i++) {
               startMarkers.removeLayer(markers[i]);
               endMarkers.removeLayer(markers[i]);
               map.removeLayer(markers[i]);
            }  
            //now empty our array and start again
            markers = new Array();
            
            //loop through each entry in our stations variable and add it as a marker
            angular.forEach(newValue, function(bikes) {
                var marker = L.marker([bikes.lat, bikes.lon], {icon: greenIcon})
                    .bindPopup("<b>" + bikes.station + "</b><br>" + bikes.trips)
                var circle = L.circle([bikes.lat, bikes.lon], bikes.radius,{
                       color: 'green',
                       fillColor: '#5f0',
                       fillOpacity: 0.5 })
                   
                if (bikes.ridetype=="End") {
                    marker.setIcon(redIcon)
                    marker.addTo(endMarkers)
                    circle.setStyle({
                       color: 'red',
                       fillColor: '#f03',
                       fillOpacity: 0.5 })
                    circle.addTo(endMarkers)
                } else {
                    marker.addTo(startMarkers);  
                    circle.addTo(startMarkers);  
                }
                markers.push(circle);   
                markers.push(marker);   

            });
        })
    });
}

if (window.locationWatcher) {
    // clear existing watcher otherwise we'll have duplicates
    window.locationWatcher();
}

// ensure we only load the script once, seems to cause issues otherwise
if (window.L) {
    initMap();
} else {
    console.log('Loading Leaflet library');
    var sc = document.createElement('script');
    sc.type = 'text/javascript';
    sc.src = 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.3/leaflet.js';
    sc.onload = initMap;
    sc.onerror = function(err) { alert(err); }
    document.getElementsByTagName('head')[0].appendChild(sc);
}
</script>

```

#### Oracle Event Hub Cloud Service / Kafka

###### About OEHCS (Oracle Event Hub Cloud Service)


Oracle Event Hub Cloud Service combines the open source technology Apache Kafka with unique innovations from Oracle to deliver a complete platform for working with streaming data.

The Oracle Event Hub Cloud Service is a managed Platform as a Service (PaaS) cloud-based offering that provides a highly available and scalable messaging platform for loading and analyzing streaming data. You can:

 + Spin up multiple clusters and create topics in seconds, on demand, and then use it.
 + Scale Out or Scale In clusters or Add/Remove partitions to elastically react to varying demands of your streaming data.
 + Choose different cluster configurations depending on your needs.
 + Use open REST APIs and CLIs to manage, use, and extend the service.


Documentation for OEHCS can be found: <a href="http://docs.oracle.com/cloud/latest/event-hub-cloud/index.html" target="_new">here</a>.  General info about Apache Kafka can be found: <a href="https://kafka.apache.org/" target="_new">here</a>.

###### About Spark Streaming

The integration between OEHCS and BDCS-CE leverages Spark Streaming to easily process the live streams of data from OEHCS.  In particular, while Spark Streaming can work with multiple types of sources, we will be using Spark Streaming's support for Kafka as OEHCS leverages Kafka internally.

Documentation about Spark Streaming can be found: <a href="http://spark.apache.org/docs/2.1.0/streaming-programming-guide.html" target="_blank">here</a>.  And the integration with Kafka:  <a href="https://spark.apache.org/docs/2.1.0/streaming-kafka-integration.html" target="_blank">here</a>.

###### Configuring Spark for Kafka

Add a dependency to the Spark interpreter in Zeppelin

+ Go to Settings
+ Click on Notebook
+ Scroll down to the Spark Interpreter settings area
+ Click on Edit
+ Add the below dependency
+ Click on Save
+ Click to Restart the Spark Interpreter

Hint: Copy the below dependency string into your clipboard for easy pasting into the edit setting screen:

    org.apache.spark:spark-streaming-kafka-0-8_2.11:2.1.0 

To connect your OEHCS instance with your BDC instance, we need to lookup a few settings for use later.

Follow these steps (hint: you might want to open up a second browser window so that you can refer back to these instructions as you follow the steps):

First, lookup the Public IP address of your BDCS-CE server. You will find it on the My Services - BDCSCE Service Overview page as show here:

![1548763811225](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548763811225.png)

###### Setting up your OEHCS for Access from BDC (if using OCI)

**This step can be skipped when the OEHCS is already associated with the BDCS CE (option when provisioning BDCS CE)**

If running in OCI: To connect your OEHCS instance with your BDC instance, we need to setup the appropriate Security List for your OCI Network VCN.


Follow these steps (hint: you might want to open up a second browser window so that you can refer back to these instructions as you follow the steps):

 + Navigate to the OCI Compute Console.
 + Click on the Networking tab
 + Set the Compartment filter to Demo
 + Click on the listed VCN
 + Under the Resources list, click on Security Lists
 + Click on the Default Security List
 + Click Edit All Rules
 + Add a new ingress rule for: publicIP/32 . TCP . source port is null . destination port is 6667
 + Click Save Security List Rules

###### Creating a topic in OEHCS

Now, we will create a new Kafka topic in OEHCS for this tutorial.  Before we do so, a quick comment about OEHCS terminology.  The "OEHCS Platform" is the terminology for the cluster itself.  A cluster will manage multiple topics.  We refer to individual topics as instances of "OEHCS".  Thus, to create a new topic you will create a new instance of "OEHCS" to run on the "OEHCS Platform" (cluster) you already created.

Open the OEHCS console and stay in the topics tab.

![1548764031411](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548764031411.png)

Click on New Topic and fill out the Topic Name

![1548764083555](C:\Users\shagedor\AppData\Roaming\Typora\typora-user-images\1548764083555.png)

|                          |                                                              |
| ------------------------ | ------------------------------------------------------------ |
| Topic Name               | Specify a name for the Topic. Choose a name that is unique within the tenant domain that will be used to identify the new Topic. |
| Partitions               | Number of partitions to be created in the topic. Minimum 1 and Maximum 256. |
| Replication Factor       | Number of replications that should created for the Topic     |
| Log Cleanup Policy       | Specify the cleanup policy for logs. You can choose between Delete and Compact. Delete policy deletes the log after retention period. Compact policy ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition. Use Compact only with messages that specify keys |
| Retention Period (Hours) | The duration (in hours) for which logs in the topic should be retained. Minimum 1 and Maximum 336 hours i.e. 14 days |

```scala
%spark
z.angularBind("BIND_ObjectStorage_Container", "journeyC")
z.angularBind("BIND_OEHCS_ConnectionDescriptor", z.input("OEHCS_ConnectionDescriptor","interactiveeventhub-kafka-zk-1.svcsubnetad1.svcvcn.oraclevcn.com:6667"))
z.angularBind("BIND_OEHCS_Topic", z.input("OEHCS_Topic","BDCSCE"))

//save these for pyspark
z.put("BIND_OEHCS_Topic", z.angular("BIND_OEHCS_Topic"))
z.put("BIND_OEHCS_ConnectionDescriptor", z.angular("BIND_OEHCS_ConnectionDescriptor"))

//save these for shell
scala.tools.nsc.io.File("/var/lib/zeppelin/oehcs.sh").writeAll(
  "export ObjectStorage_Container=\""+z.angular("BIND_ObjectStorage_Container")+"\"\n" +
  "export OEHCS_ConnectionDescriptor=\""+z.angular("BIND_OEHCS_ConnectionDescriptor")+"\"\n" +
  "export OEHCS_Topic=\""+z.angular("BIND_OEHCS_Topic")+"\"\n"
)
println("done")

```

###### Writing a Producer to stream data to OEHCS

This tutorial will use a small python program to stream our bike data to OEHCS.  This program will read the bike data and play it back, either in "real-time" or in an accelerated fashion.  Our Python program will use the "kafka-python" library, as described <a href="https://github.com/dpkp/kafka-python" target="_blank">here</a>.  

Our first step is to download the kafka-python library using pip as seen in the next paragraph.  Then we will write our python program and save as a file.

Run the next 2 paragraphs to continue.

By the way, you might want to review the "Understanding Python with BDC" notebook in the Extras folder to learn about the Python setup on BDC environments.

```sh
%sh

echo "Please run this paragraph to do some additional setup for our journey"

sudo whoami
#the sudo whoami output should say root.  If not, your bootstrap.sh script did not work.  The easiest fix is to start over and recreate your instance as per the New Data Lake journey instructions.
#Or you can follow the Reference document on manually running bootstrap.

# If you get a SIGTERM error before this finishes, it is another sign your bootstrap.sh script did not work.

echo "may take a few minutes."

case "oci://journeyC@interactivetech" in
    *oci*) 
      #echo "running easy_install"
      #sudo /u01/bdcsce/usr/local/bin/easy_install --upgrade --index-url https://pypi.python.org/simple/ pip 
      #echo "after easy_install"
      echo "No need to run easy_install with OCI builds"
    ;;
    *)
    echo "No need to run easy_install with OCIC builds"
    ;;	
esac

echo "use pip to upgrade setuptools"
sudo /u01/bdcsce/usr/local/bin/pip install --upgrade setuptools 
echo "after upgrade setuptools"
echo ".."
echo ".."

#do this at least once.  
echo "appdirs==1.4.3
kafka-python==1.3.3
packaging==16.8
pyparsing==2.2.0
python-dateutil==2.6.0
six==1.10.0
" > requirements.txt

sudo /u01/bdcsce/usr/local/bin/pip install -r requirements.txt 
echo "done"

```

```python
%sh

. oehcs.sh

echo "
#!/usr/bin/env python

# standard libraries
import os
import sys
import csv
import json
from time import sleep
import datetime as dt

# Quality of Life Utils
import dateutil.parser

# kafka-python libraries
from kafka import KafkaProducer
from kafka.errors import KafkaError

if len(sys.argv) < 6:
	print 'usage: tutorial_kafka.py [inputfile:/path/to/file.csv] [acceleration-factor:integer] [recordcount:int-0 is infinite] [starttime:YYYY-MM-DD hh:mm:ss]'
	sys.exit(1)

inputfile = sys.argv[1]
accelerator = float(sys.argv[2])
recordcount = int(sys.argv[3])
inputstarttime = dateutil.parser.parse(' '.join(sys.argv[4:]))

scriptstarttime = dt.datetime.now()
relativestarttimedelta = inputstarttime - scriptstarttime

def timedelta_total_seconds(timedelta):
    return (
        timedelta.microseconds + 0.0 +
        (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6


# When this baby hits 88mph, you're going to see some serious stuff.
def delorean(accelerator, scriptstarttime):
	nowtime = dt.datetime.now()
	return scriptstarttime + dt.timedelta(seconds=accelerator*timedelta_total_seconds(nowtime - scriptstarttime))


# Kafka Stuff
# put your broker hostname:port in single quotes inside those bracketse
mykafkaservers = ['$OEHCS_ConnectionDescriptor']
producer = KafkaProducer(bootstrap_servers=mykafkaservers, value_serializer=lambda m: json.dumps(m).encode('utf-8'))


i = 0
# Reader Loop
with open(inputfile) as csvfile:
	reader = csv.DictReader(csvfile)
	for rec in reader:
		eventtime = dateutil.parser.parse(rec['Start Time'])
		if eventtime < inputstarttime:
			continue
		relativenowtime = delorean(accelerator, scriptstarttime) + relativestarttimedelta
		while (relativenowtime < eventtime):
			relativenowtime = delorean(accelerator, scriptstarttime) + relativestarttimedelta
			# print relativenowtime, eventtime
			sleep(0.1)
		print str(i)+'/'+str(recordcount)+' sending: ', rec
		producer.send('$OEHCS_Topic', rec)
		i += 1
		if i >= recordcount and recordcount != 0:
			break
" > tutorial_kafka.py

ls -l tutorial_kafka.py
echo "done"
```

###### Example: Consuming streaming data from OEHCS

Now that we have downloaded data and written our python producer, we are ready for our first example.  To run our example, **you will need to run 2 things**: the python producer script and a Spark Streaming consumer script.

First, we will start with the Spark Streaming script.  **Run the next paragraph**.  **Scroll down and observe the output**, even though it says it is still running.  You will notice that it begins to report new information every 5 seconds.  After 90 seconds, it will shut itself down.

**Before the Spark Streaming code shuts itself down**, move to the paragraph that invokes our python producer in a shell interpreter (it is the one right after the spark streaming script).  **Run this python producer paragraph**.  At this point, both the producer and the consumer should be running.  Observe the output of both.  

After sending 10 records, the python producer will quit.  After 90 seconds, the Spark Streaming consumer will quit.

```scala
%spark

{
    

import _root_.kafka.serializer.StringDecoder //http://stackoverflow.com/questions/36397688/sbt-cannot-import-kafka-encoder-decoder-classes
import org.apache.spark.streaming._
import org.apache.spark.streaming.kafka._


 println("Creating new Streaming Context")
 val ssc = new StreamingContext(sc, Seconds(5))
 
 val topic = z.angular("BIND_OEHCS_Topic").toString
 println("topic:"+topic)
 val topicsSet = topic.split(",").toSet
 
 val brokers=z.angular("BIND_OEHCS_ConnectionDescriptor").toString
 println("brokers:"+brokers)
 val kafkaParams = Map[String, String]("metadata.broker.list" -> brokers)
 
 println("Creating Kafka DStream")
 //https://spark.apache.org/docs/1.6.1/streaming-kafka-integration.html
 val messages = KafkaUtils.createDirectStream[String, String, StringDecoder, StringDecoder](
      ssc, kafkaParams, topicsSet)
      

 println("Setting up operations on DStream")    
 
 //for debugging, you can print the full contents of the first 10 rows of each batch of messages by uncommenting the following
 //messages.print()
 
 messages.foreachRDD(rdd => {
     //our Kafka data comes in Key,Value format.  we only care about the value, so use a map to extract just the 2nd element
     var values=rdd.map(kv => kv._2)
     
     //for this example, the value is a JSON string.  Let's make a DataFrame out of the JSON strings
     var df=sqlContext.read.json(values)
     
     var reccount = df.count()
     //let's print out the count
     printf("count = %s \n",reccount)
     
     //check to see if we have any rows...
     if (reccount >0)  {
        //let's print the first row
        println("first row ",df.first())

     } 
     
 })
 
 println("Starting Streaming Context")
 ssc.start()

 println("Will now sleep for a few minutes, before stopping the StreamingContext.  At this point, you should start the producer.")

 //now sleep for 1.5 minutes.  Parameter is milliseconds
 Thread.sleep(90000)

 //stop any active streamingcontexts.  Parameters are boolean stopSparkContext, boolean stopGracefully
 println("Stopping Active StreamingContext")
 StreamingContext.getActive().map(_.stop(false,true))

 println("done")

}

```

```sh
%sh
#The arguments are datafile TimeSpeedupFactor RecordsToProduce StartDate StartTime  
/u01/bdcsce/usr/local/bin/python ./tutorial_kafka.py citibike/201612-citibike-tripdata.csv 1 10 2016-12-01 06:00:00 2>&1

```

###### More complex example: Spark SQL and Writing to Object Store

In this example, we will demonstrate defining a Spark SQL table with our real-time data as well as writing data to the Object Store. 

To run the more complex example, **you will need to**

+ run the Spark paragraph below to start the consumer.  *Note: this consumer will not stop by itself but we provide commands later to stop it when needed.*
+ run the producer paragraph below to start the producer.
+ Observe the output of the consumer and run and re-run the SQL paragraphs to query the realtime_bike_trips table.  The consumer is using a window of 30 secods, so you should see different data approximately every 30 seconds as you run the SQL queries.
+ run the Spark paragraph further below to stop the running StreamingContext
+ check the ObjectStore to confirm that the streaming data was written to it

```scala
%spark

{
    

 import _root_.kafka.serializer.StringDecoder //http://stackoverflow.com/questions/36397688/sbt-cannot-import-kafka-encoder-decoder-classes
 import org.apache.spark.streaming._
 import org.apache.spark.streaming.kafka._

 val filebase = "oci://journeyC@interactivetech/citibike/streaming"


 println("Defining a placeholder empty dataframe for our SQL table structure when we don't have any realtime data")

 //use a sample record to capture the column names and types
 val dummyrec="{'Birth Year': '1981', 'Stop Time': '2016-12-01 06:03:36', 'End Station Longitude': '-73.99061728', 'Trip Duration': '214', 'Start Station ID': '447', 'Start Station Longitude': '-73.9851615', 'End Station Latitude': '40.76669671', 'End Station Name': 'W 53 St & 10 Ave', 'Start Time': '2016-12-01 06:00:01', 'Start Station Latitude': '40.76370739', 'End Station ID': '480', 'Bike ID': '16669', 'User Type': 'Subscriber', 'Gender': '1', 'Start Station Name': '8 Ave & W 52 St'}"
 val dummyRDD = sc.parallelize(dummyrec :: Nil)
 var dummyDf=sqlContext.read.json(dummyRDD)
 //df.printSchema()
 //create a new DF with zero records (but with same column names/types)
 var emptyDF=dummyDf.filter("Gender = 'xxx'")
 //emptyDF.printSchema()
  
  
 println("Creating new Streaming Context")
 val ssc = new StreamingContext(sc, Seconds(30))
 

 val topic = z.angular("BIND_OEHCS_Topic").toString
 println("topic:"+topic)
 val topicsSet = topic.split(",").toSet
 
 val brokers=z.angular("BIND_OEHCS_ConnectionDescriptor").toString
 println("brokers:"+brokers)
 val kafkaParams = Map[String, String]("metadata.broker.list" -> brokers)


 println("Creating Kafka DStream")
 //https://spark.apache.org/docs/1.6.1/streaming-kafka-integration.html
 val messages = KafkaUtils.createDirectStream[String, String, StringDecoder, StringDecoder](
      ssc, kafkaParams, topicsSet)
      

 println("Setting up operations on DStream")    
 
 //for debugging, you can print the full contents of the first 10 rows of each batch of messages by uncommenting the following
 //messages.print()
 
 messages.foreachRDD(rdd => {
     //our Kafka data comes in Key,Value format.  we only care about the value, so use a map to extract just the 2nd element
     var values=rdd.map(kv => kv._2)
     
     //for this example, the value is a JSON string.  Let's make a DataFrame out of the JSON strings
     var df=sqlContext.read.json(values)
     
     var reccount = df.count()
     //let's print out the count
     //printf("count = %s \n",reccount)  This will get printed to the Spark log files, not zeppelin
     
     //check to see if we have any rows...
     if (reccount >0) {
        //let's print the first row
        //println("first row ",df.first()) This will get printed to the Spark log files, not zeppelin
        
        //let's define a temptable
        df.createOrReplaceTempView("realtime_bike_trips")
        
        //let's also write this DF to Object Store...

        // save in json format.  the repartition(1) ensures that we write a single output file, which makes sense since we know the output is small
        df.repartition(1).write.format("json").mode("append").save(filebase)


     } else {
         //no records.
         //let's register a df with no data
         emptyDF.createOrReplaceTempView("realtime_bike_trips")
     }
     
     
 })
 
 println("Starting Streaming Context")
 ssc.start()

 println("Note: you will need to manually stop this StreamingContext or it will continue forever.  To do so, run: StreamingContext.getActive().map(_.stop(false,true))")
 println("      There is a sample paragraph below that shows you how to do this.")

 println("Start of the Consumer done. Go ahead and start the producer if you have not already. With both the Consumer and Producer running, run the Spark SQL queries below and you should see different data every 30 seconds ")

}
```

```sh
%sh
#The arguments are datafile TimeSpeedupFactor RecordsToProduce StartDate StartTime  

# for the more complex example, we are running a timespeedup factor of 10 to push data faster through the system

/u01/bdcsce/usr/local/bin/python ./tutorial_kafka.py citibike/201612-citibike-tripdata.csv 10 300 2016-12-01 06:00:00 2>&1

```

```sql
%sql
select * from realtime_bike_trips
```

```sh
%sh

export HADOOP_ROOT_LOGGER=WARN

echo "Observe the timestamps of the files.  You should see files with today's timestamps added by the more complex streaming example"

hadoop fs -ls oci://journeyC@interactivetech/citibike/streaming
```

```scala
%spark
{
    import org.apache.spark.streaming._
    println("Stopping any active StreamingContext.  May take a minute.")
    StreamingContext.getActive().map(_.stop(false,true))
    println("done")
}
```

