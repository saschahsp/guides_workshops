# Oracle’s Machine Learning and Advanced Analytics

## Oracle Machine Learning

[Link](https://www.oracle.com/technetwork/database/options/oml/overview/index.html)

Apache Zeppelin based Machine Learning SQL Notebook for Data Scientists to Collaborate in the Oracle Autonomous Data Warehouse

* Collaborative SQL notebook UI for data scientists  
* Packaged with Oracle Autonomous Data Warehouse
* Easy access to shared notebooks, templates, permissions, scheduler, etc.
* Access to 30+ parallel, scalable in-database implementations of machine learning algorithms
* SQL and PL/SQL scripting language supported
* Enables and Supports Deployments of Enterprise Machine Learning Methodologies in ADW

* [Github oracle/oracle-db-examples](https://github.com/oracle/oracle-db-examples/tree/master/machine-learning) 
* [ADW + OAC Predicting Demand with Oracle Machine Learning & Autonomous Data Warehouse Cloud Service](https://github.com/oracle/learning-library/tree/master/workshops/bike-share-prediction)
* [ADW ML Bonus Lab - Lab 9: Simple Introduction to Machine Learning Algorithms](https://github.com/oracle/learning-library/blob/master/workshops/journey4-adwc/LabGuide9.md)
     * [IO Link](https://oracle.github.io/learning-library/workshops/bike-share-prediction/?page=README.md)

## Oracle Advanced Analytics Database Option 

_included in Oracle Database Cloud High and Extreme Editions_

[Link](https://www.oracle.com/technetwork/database/options/advanced-analytics/overview/index.html)

[Public Customer Reference](https://www.oracle.com/technetwork/database/options/advanced-analytics/odm/odm-customers-086483.html)

### Oracle Data Mining (SQL API Machine Learning functions)

**There are no plans to make it available for ADW-ATP**

[Link](https://www.oracle.com/technetwork/database/options/advanced-analytics/odm/overview/index.html)

Oracle Data Mining (ODM) is a component of the Oracle Advanced Analytics Database Option and provides a Oracle Data Miner GUI, which is an extensions of the SQL Developer.

### Oracle Data Miner "workflow" UI (for Citizen Data Scientists) SQL Developer extension

[Link](https://www.oracle.com/technetwork/database/options/advanced-analytics/odm/dataminerworkflow-168677.html)

The Oracle Data Miner is an extension to Oracle SQL Developer that enables data analysts to view their data built and evaluate multiple machine learning/data mining models and accelerate model deployment.

### Oracle R Enterprise (R API to ODM SQL ML functions, R to SQL "push down" and R integration)

[Link](https://www.oracle.com/technetwork/database/database-technologies/r/r-enterprise/overview/index.html)

Oracle R Enterprise, a component of the Oracle Advanced Analytics Option, makes the open source R statistical programming language and environment ready for the enterprise and big data.

* R language SQL “push down”
    * Transparency layer for “push down” to equivalent SQL for parallelized in-DB processing
* Direct access to DB data
    * ROracle pkg for OCI connectivity
    * “Embedded R” call outs to R packages

## Oracle R Advanced Analytics for Hadoop (ORAAH) 

_(part of the Big Data Connectors)_

* Manipulate data stored in a local File System, HDFS,HIVE, Impala or JDBC sources
* General computation framework where users invoke parallel, distributed MapReduce jobs from R, writing custom mappers and reducers in R while also leveraging open source CRAN packages
* Leverage Hadoop nodes and Spark for cluster scalable, high performance
* Functions use the expressive R formula object for Spark parallel execution
    * ORAAH's custom LM/GLM/MLP NN algorithms scale better and run faster than the opensource Spark Mllib. Also Expose Mllib algorithms

[Link](http://www.oracle.com/technetwork/database/database-technologies/bdc/r-advanalytics-for-hadoop/overview/index.html)

## Oracle Machine Learning for Python

_Oracle Advanced Analytics Option to 18c+_

* Similar architecture to OAA’s Oracle R Enterprise
    * OML4Py Transparency Layer
    * Use Oracle Database as High Performance Computing environment
* OML4Py OAA Model Build and Apply
    * Use OAA parallel and distributed ML algorithms
    * Manage Python scripts and Python objects in Oracle Database
* OML4Py Embedded Python
    * Make callout to Python packages
    * Integrate Python results into applications via SQL
* cx_Oracle library

* Automated Machine Learning (AutoML) Components
    * Auto Feature Selection >50% reduction in features
    * Auto Model Selection 4x faster than exhaustive search
    * Auto Tuning of Hyperparameters Up to 24% accuracy improvement

* [Oracle Machine Learning for Python - Introduction](https://stbeehive.oracle.com/content/dav/st/Oracle%20Machine%20Learning%20&%20Advanced%20Analytics%20PM%20Workspace/Public%20Documents/OML4Py/1%20-%20OML4Py%20Introduction.html)
* [Oracle Machine Learning for Python - Automatic Machine Learning](https://stbeehive.oracle.com/content/dav/st/Oracle%20Machine%20Learning%20&%20Advanced%20Analytics%20PM%20Workspace/Public%20Documents/OML4Py/5%20-%20OML4Py%20Automatic%20Machine%20Learning.html)
* [Oracle Machine Learning for Python - Data Selection and Manipulation](https://stbeehive.oracle.com/content/dav/st/Oracle%20Machine%20Learning%20&%20Advanced%20Analytics%20PM%20Workspace/Public%20Documents/OML4Py/2%20-%20OML4Py%20Data%20Selection%20and%20Manipulation.html)
* [Oracle Machine Learning for Python - Embedded Python Execution](https://stbeehive.oracle.com/content/dav/st/Oracle%20Machine%20Learning%20&%20Advanced%20Analytics%20PM%20Workspace/Public%20Documents/OML4Py/4%20-%20OML4Py%20Embedded%20Python%20Execution.html)

* [Oracle Machine Learning for Python - Datastore and Script Repository](https://stbeehive.oracle.com/content/dav/st/Oracle%20Machine%20Learning%20&%20Advanced%20Analytics%20PM%20Workspace/Public%20Documents/OML4Py/3%20-%20OML4Py%20Datastore%20and%20Script%20Repository.html)


## (New Oracle Machine Learning Microservices)
### (OML Image Microservices)
### (OML Text Microservices)