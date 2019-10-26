# 01_Basics

The Oracle Big Data Cloud has a built in Zeppelin Notebook, which is based on Apache Zeppelin. The notebook enables you to work with cells and a variety of interpreters. 

## About Interpreters

The Zeppelin notebook is powered by Interpreters, which allow various technologies to be combined into a single, easily documented environment. The concept of Zeppelin interpreter allows any language/data-processing-backend to be plugged into Zeppelin. Currently, Zeppelin supports many interpreters such as Scala ( with Apache Spark ), Python ( with Apache Spark   Spark SQL, JDBC, Markdown, Shell and so on.

## What is Zeppelin interpreter?

Zeppelin Interpreter is a plug-in which enables Zeppelin users to use a specific language/data-processing-backend. For example, to use Scala code in Zeppelin, you need %spark interpreter.

When you click the +Create button in the interpreter page, the interpreter drop-down list box will show all the available interpreters on your server.

![](img/1.png)

## What is interpreter setting?

Zeppelin interpreter setting is the configuration of a given interpreter on Zeppelin server. For example, the properties are required for hive JDBC interpreter to connect to the Hive server.

![](img/2.png)

Each notebook can be bound to multiple Interpreter Settings using setting icon on upper right corner of the notebook.

![](img/3.png)

The Interpreters currently offered with this version of BDCS-CE are, among others:

* Markdown (%md)
* Shell (%sh)
* Spark with Scala (%spark)
* Spark with Python (%pyspark)
* Spark SQL (%sql)
* Hive (%hive)
* JDBC (%jdbc)
* Angular

In this first tutorial, we will introduce you to the Markdown and Shell Interpreters.

## About the Markdown Interpreter (%md)

The Markdown interpreter is used to add documentation to your notebooks. To create a paragraph using the Markdown interpreter, use %md for the first line in the code editor.

Some simple examples…
Add Emphasis using one or more *

Create a list using +

* item
* item
* item

For more, check out the Markdown cheatsheet at https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

Hint: View the editor for this section to see the actual Markdown code used

# About the Shell Interpreter (%sh)

The shell interpreter runs linux shell commands as the zeppelin user on the BDCS-CE server running zepellin. It can be handy way to check zeppelin log files, pull files into BDCS-CE, interact with HDFS, or change/install software. SSH can also be used, but running shell commands via the notebook can be more natural and self-documenting.

By default, the zeppelin user does not have sudo privileges. But in the next Tutorial, we will show how you can add zeppelin to the authorized sudo users list.

The following paragraph has some sample shell command examples.

```bash
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

