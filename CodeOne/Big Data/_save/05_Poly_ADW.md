# Poly & ADW

If desired and add a Data Warehouse to the Data Lake, you can use, among others, the Python library cx_Oracle.

**cx_Oracle**

Python package enabling scalable and performant connectivity to Oracle Database.

* Open source, publicly available on PyPI, OTN, and Github
* Oracle is maintainer
* Oracle Database Interface for Python conforming to Python DB API 2*.0 specification
* Optimized driver based on OCI
* Execute SQL statements from Python
* Enables transactional behavior for insert, update, and delete

**Configurations (already done)**

ADW has a wallet file that is needed to connect to the database. This has to be unzipped and be located in a TNS_ADMIN folder. 

```sh
sudo mkdir /opt/oracle/dbconnector/tns_admin
sudo chown zeppelin /opt/oracle/dbconnector/tns_admin
cd /opt/oracle/dbconnector/tns_admin
rm *
hadoop fs -ls /tmp
hadoop fs -get "/tmp/wallet_ADWOCO.zip" wallet.zip
unzip -u wallet.zip

#update the wallet directory path in the sqlnet.ora
cp sqlnet.ora sqlnet.ora.save
cat <<EOF > sqlnet.ora
WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="/opt/oracle/dbconnector/tns_admin")))
SSL_SERVER_DN_MATCH=yes
EOF

ls
echo "done"
```
Make sure your environmental variables are set correctly. 

```sh
export TNS_ADMIN=/opt/oracle/dbconnector/tns_admin
export LD_LIBRARY_PATH=/opt/oracle/dbconnector/instantclient:$LD_LIBRARY_PATH
export PATH=/opt/oracle/dbconnector/instantclient:$PATH

sqlplus 'TESTUSER/WElcome_123#@ADWTest_high'
#sqlplus 'ADMIN/CrEakY@6EsCape@ADWTest_high'

echo "select 1 from dual;" | sqlplus 'TESTUSER/WElcome_123#@ADWTest_high'
```
Check the environmental variables in Python. 

```python
%pyspark
import os
print(os.environ['TNS_ADMIN'])
print(os.environ['LD_LIBRARY_PATH'])
print(os.environ['PATH'])
```

A cursor example with cx_Oracle

```python
%pyspark

import os
import cx_Oracle

connection = cx_Oracle.connect('admin', 'WElcome_123#', 'ADWoco_high')

cursor = connection.cursor()
rs = cursor.execute("select * from sh.customers where rownum < 1000")
rs.fetchall()
```

Get the SQL query result as Pandas Data Frame. 

```python
%pyspark
import cx_Oracle 
import pandas as pd

connection = cx_Oracle.connect('admin', 'WElcome_123#', 'ADWoco_high')

# Write records stored in a DataFrame to a oracle database
df = pd.read_sql('select * from sh.customers where rownum < 1000', connection) # the error shows here

df
```

## Spark SQL

Let's run a Spark SQL query against a Hive table. 

```sql
%jdbc(hive)

show tables;
```

```scala
%spark

val sqlDF = spark.sql("SELECT startstationname, avg(tripduration) / 60 as AverageTripduration FROM bike_trips_objectstore group by startstationname")

z.show(sqlDF)
```
We can create temporary or global views based on the Spark SQL Data Frame.

```scala
%spark

df.createOrReplaceTempView("aggregation_tmp")

df.createGlobalTempView("global_temp.aggregation_glb")
```
We can query this view also with pyspark, of cours.

```python
%pyspark

sqlDF = spark.sql("SELECT * FROM global_temp.aggregation_glb")
z.show(sqlDF)
```

However, those are no persistent hive tables.

```sql
%jdbc(hive)

show tables;
```

Temporary views in Spark SQL are session-scoped and will disappear if the session that creates it terminates. If you want to have a temporary view that is shared among all sessions and keep alive until the Spark application terminates, you can create a global temporary view. Global temporary view is tied to a system preserved database global_temp, and we must use the qualified name to refer it.

```scala
%spark

val sqlDF = spark.sql("SELECT * FROM global_temp.aggregation_glb")
```

Of course, the same can be done with pyspark.

```python
%pyspark


sqlDF = spark.sql("SELECT * FROM global_temp.aggregation_glb")

type(sqlDF)
```
You can convert the Spark SQL Data Frame.  

```python
%pyspark

#spark.conf.set("spark.sql.execution.arrow.enabled", "true")
sqlDF_pd = sqlDF.toPandas()

type(sqlDF_pd)
```

```python
%pyspark

sqlDF_pd.head()
```
Of course, you can convert it back to Spark SQL Data Frame

```python
%pyspark

#spark.conf.set("spark.sql.execution.arrow.enabled", "true")
spark_df = spark.createDataFrame(sqlDF_pd)

print(type(spark_df))
```

We can also create a hive table from the Spark Data Frame.

```scala
%spark

spark.sql("drop table if exists my_new_table");
spark.sql("create table my_new_table as select * from aggregation_tmp");
```

Let's see if it works. 

```sql
%jdbc(hive)
show tables;
```

```sql
%jdbc(hive)

select * from my_new_table;
```