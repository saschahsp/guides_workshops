# Notebooks

* A notebook is a web-based interface for data analysis, data discovery, data visualization, and collaboration.
* Oracle Machine Learning SQL notebooks provide easy access to Oracle’s parallelized, scalable, in-database implementations of a library of Oracle Advanced Analytics’ machine learning algorithms (classification, regression, anomaly detection, clustering, associations, attribute importance, feature extraction, times series, and so on.)
* Oracle Machine Learning uses Zeppelin Notebook, a collaborative interface to write the code, equations, and text, create visualizations, and perform data analytics.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/16.PNG)

## Create a Notebook

Following Notebook features are accessible: 
* Edit
* Create
* Duplicate
* Save as Template
* Delete
* Import
* Version

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/18.PNG)

To create a notebook, OML has an interpreter settings specification. The notebook contains an internal list of bindings that determines the order of the interpreter bindings.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/17.PNG)

Dynamic forms such as the Text Input form, Select form, Check box form for easy selection of inputs and easy filtering of data in your notebook. 

Oracle Machine Learning supports the following Apache Zeppelin dynamic forms: 
* **Text Input form:** Allows you to create a simple form for text input 
* **Select form:** Allows you to create a form containing a range of values that the user can select 
* **Check Box form:** Allows you to insert check boxes for multiple selection of inputs

The **text input form** allows you to dynamically retrieve values 
as defined in the notebook.

To create a **text input form**:

In an SQL statement, define the text input form by using the syntax:

```sql
SELECT * FROM ALL_OBJECTS WHERE OBJECT_TYPE = '${OBJ}';
```

In the preceding example:

* The form name is **obj**
* The table name is **ALL_OBJECTS**
* The column name is **OBJECT_TYPE**
* Text form **obj** is created for the column `OBJECT_TYPE` in the table `ALL_OBJECTS`
* Enter different values in the form field **obj** and run the notebook to retrieve the corresponding values in the column `OBJECT_TYPE`.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/19.PNG)

To create a **check box form:**

In an SQL statement, define the check box form by using the syntax:

```sql
SELECT '${checkbox:whichcolumn=OWNER|OBJECT_TYPE, OWNER|OBJECT_NAME|OBJECT_TYPE|CREATED|STATUS}' FROM ALL_OBJECTS WHERE OBJECT_TYPE IN ('VIEW', 'TABLE', 'INDEX', 'SYNONYM');
```

In the preceding example:
* The check box form name is WhichColumn.
* The multiple selection options available in the check boxes are `OWNER`, `OBJECT_NAME`, `OBJECT_TYPE`, `CREATED`, and `STATUS`.
* The fields `OWNER` and `OBJECT_TYPE` are defined as default.
* The table name is `ALL_OBJECTS`.
* The columns that are configured for display are `OWNER,OBJECT_NAME, OBJECT_TYPE, CREATED,` and `STATUS`.

Run the notebook. The check box form called WhichForm is available in the notebook.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/20.PNG)

To create a **select input form:**

In an SQL statement, define the select input form by using the syntax:

```sql
SELECT * FROM ALL_OBJECTS WHERE OBJECT_TYPE = '${OBJ=INDEX,INDEXTABLE|VIEW|SYNONYM}';
```

In the preceding example :

* The form name is **obj**
* The list of available values are `INDEX, TABLE, VIEW, SYNONYM`.
* The table name is `ALL_OBJECTS`
* The column name is `OBJECT_TYPE`

Select any values from the drop-down list in the obj form. The selected value 
will be retrieved in the `OBJECT_TYPE` column in the `ALL_OBJECTS` table.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/21.PNG)

## Setting Up an Output Format

Oracle Machine Learning allows you to preformat query output in notebooks.

```sql
%script
SET SQLFORMAT format_option
```

For example, if you want the output in ansiconsole format, then type the command followed by the SQL query as:
```sql
SET SQLFORMAT ansiconsole;
SELECT * FROM HR.EMPLOYEES;
```

The output format is ansiconsole, and the table name is HR.EMPLOYEES.

Note: This formatting is available for the Script interpreter and you must add the prefix %script.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/22.PNG)

**Output Formats Supported by the `SET SQLFORMAT` Command**

**CSV** — The CSV format produces standard comma-separated variable output, with string values enclosed in double quotes
```sql
%script
SET SQLFORMAT CSV
```
**HTML** - The HTML format produces the HTML for a responsive table. The content of the table changes dynamically to match the search string entered in the text field
```sql
%script
SET SQLFORMAT HTML
```
**XML** — The XML format produces a tag based XML document. All data is presented as CDATA tags.
```sql
%script 
SET SQLFORMAT XML 
```
**JSON** - The JSON format produces a JSON document containing the definitions of the columns along with the data that it contains 
```sql
%script 
SET SQLFORMAT JSON
```
**ANSICONSOLE** — The ANSICONSOLE format resizes the columns to the width of the data to save space. It also underlines the columns, instead of separate line of output.  
```sql 
%script 
SET SQLFORMAT ANSICONSOLE
```
**INSERT** — The INSERT format produces the INSERT statements that could be used to recreate the rows in a table. 
```sql
%script 
SET SQLFORMAT INSERT
```
**LOADER** — The LOADER format produces pipe delimited output with string values enclosed in double quotes. The column names are not included in the output.  
```sql
%script 
SET SQLFORMAT LOADER
```
