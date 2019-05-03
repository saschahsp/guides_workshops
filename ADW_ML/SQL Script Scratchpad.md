# SQL Script Scratchpad

SQL Scratchpad is a **low-overhead** tool that **simplifies** SQL and PL/SQL development. SQL Scratchpad uses a direct JDBC connection to a database.

Features include: 
* Full SQL editing capabilities, including color coding of SQL 
* Tabular formatted results window 
* Execution Plan access- graphical and tabular explain plan 
* Access to history of all SQL commands ran 
* Execution time and rows returned 
* Option to cancel a long running query

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/11.PNG)

A SQL script is a set of SQL statements. You can create SQL scripts in Oracle Machine Learning, save it as a .json file in your system, and share the SQL script with other users. 

Here a quick example:

You can simply insert your script and click run or press Shift+Enter 

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/12.PNG)

Tabular format.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/13.PNG)

Graph.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/14.PNG)

SQL script can be exported and imported. It will be exported and imported as .json file.

A connection group, also known as a Zeppelin interpreter set, is a collection of database connections. 

**Connection Groups** 

In the Connection Group page, you can manage your connections that constitute the connection group. 

You can Edit, and Stop one or more connections that are listed under a connection group. 

**Global Connection Group **

The Global Connection Group is created automatically when a new database is provisioned. The Global Connection Group comprises the following: 
* Compute Resource definition 
* Connection Group definition 

**Editing Oracle Database Interpreter Connection:** 

When defining an Oracle Database interpreter connection, a reference to a compute resource is created. This reference contains all connection-related information about the interpreter.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/15.PNG)

