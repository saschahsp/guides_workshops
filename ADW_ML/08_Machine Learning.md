# Machine Learning Example

## DBMS_DATA_MINING Overview

Oracle Data Mining supports both supervised and unsupervised data mining. 

* Supervised data mining predicts a target value based on historical data. 
* Unsupervised data mining discovers natural groupings and does not use a target. You can use Oracle Data Mining to mine structured data and unstructured text.

Supervised data mining functions include:
* Classification
* Regression
* Feature Selection (Attribute Importance)

Unsupervised data mining functions include:
* Clustering
* Association
* Feature Extraction
* Anomaly Detection

The steps you use to build and apply a mining model depend on the data mining function and the algorithm being used. The algorithms supported by Oracle Data

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/40.PNG)

Oracle Data Mining supports more than one algorithm for the classification, regression, clustering, and feature extraction mining functions. Each of these mining functions has a default algorithm.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/41.PNG)

## DBMS_DATA_MINING — Mining Functions

A data mining function refers to the methods for solving a given class of data mining problems.

The mining function must be specified when a model is created. ~~(See CREATE_MODEL Procedure.)~~

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/42.PNG)

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/43.PNG)

## DBMS_DATA_MINING — Model Settings

Oracle Data Mining uses settings to specify the algorithm and other characteristics of a model. Some settings are general, some are specific to a mining function, and some are specific to an algorithm.

All settings have default values. If you want to override one or more of the settings for a model, you must create a settings table. The settings table must have the column names and datatypes shown in the following table.

**Column Name Datatype**
```
SETTING_NAME    VARCHAR2(30)
SETTING_VALUE   VARCHAR2(4000)
```

The information you provide in the settings table is used by the model at build time.

You can find the settings used by a model by querying the data dictionary view `ALL_MINING_MODEL_SETTINGS`. This view lists the model settings used by the mining models to which you have access. All the setting values are included in the view,
whether default or user-specified.

## DBMS_DATA_MINING — Algorithm Names

The `ALGO_NAME setting` specifies the model algorithm.

The values for the `ALGO_NAME` setting are listed in the following table.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/44.PNG)

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/45.PNG)

## DBMS_DATA_MINING — Automatic Data Preparation

Oracle Data Mining supports fully Automatic Data Preparation (ADP, user-directed general data preparation, and user-specified embedded data preparation. The `PREP_*` settings enable the user to request fully automated or user-directed general data preparation. By default, fully Automatic Data Preparation (`PREP_AUTO_ON`) is enabled.

When you enable Automatic Data Preparation, the model uses heuristics to transform the build data according to the requirements of the algorithm. Instead of fully Automatic Data Preparation, the user can request that the data be shifted and/or scaled with the `PREP_SCALE*` and `PREP_SHIFT*` settings. The transformation instructions are stored with the model and reused whenever the model is applied. Refer to Model Detail Views, Oracle Data Mining User’s Guide.

You can choose to supplement Automatic Data Preparations by specifying additional transformations in the `xform_list` parameter when you build the model. ~~(See "CREATE_MODEL Procedure".)~~

If you do not use Automatic Data Preparation and do not specify transformations in the `xform_list` parameter to CREATE_MODEL, you must implement your own transformations separately in the build, test, and scoring data. You must take special care to implement the exact same transformations in each data set.

If you do not use Automatic Data Preparation, but you do specify transformations in the `xform_list` parameter to `CREATE_MODEL`, Oracle Data Mining embeds the transformation definitions in the model and prepares the test and scoring data to match the build data.

The values for the `PREP_*` setting are described in the following table.

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/46.PNG)

For more details see: 
* **DBMS_DATA_MINING — Mining Function Settings**
* **DBMS_DATA_MINING — Global Settings**
* **DBMS_DATA_MINING — Algorithm Settings (for each algorithm)**

## 43.6 DBMS_DATA_MINING Datatypes

The `DBMS_DATA_MINING` package defines object datatypes for mining transactional data. The package also defines a type for user-specified transformations. These types are called `DM_NESTED_n`, where `n` identifies the Oracle datatype of the nested attributes.

The Data Mining object datatypes are described in the following table:

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/47.PNG)

## 43.7.4 APPLY Procedure

The APPLY procedure applies a mining model to the data of interest, and generates the results in a table. The APPLY procedure is also referred to as scoring.

For predictive mining functions, the APPLY procedure generates predictions in a target column. For descriptive mining functions such as Clustering, the APPLY process assigns each case to a cluster with a probability.

In Oracle Data Mining, the APPLY procedure is not applicable to Association models and Attribute Importance models.

```sql
DBMS_DATA_MINING.APPLY (
      model_name           IN VARCHAR2,
      data_table_name      IN VARCHAR2,
      case_id_column_name  IN VARCHAR2,
      result_table_name    IN VARCHAR2,
      data_schema_name     IN VARCHAR2 DEFAULT NULL);
```
![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/48.PNG)

**Usage Notes**
1. The data provided for `APPLY` must undergo the same preprocessing as the data used to create and test the model. When you use Automatic Data Preparation, the preprocessing required by the algorithm is handled for you by the model: both at build time and apply time. (See "Automatic Data Preparation".)
2. `APPLY` creates a table in the user's schema to hold the results. The columns are algorithm-specific. The columns in the results table are listed in Table 43-41 through Table 43-45. The case ID column name in the results table will match the case ID column name provided by you. The type of the incoming case ID column is also preserved in APPLY output.
3. The datatype for the `PREDICTION, CLUSTER_ID, and FEATURE_ID` output columns is influenced by any reverse expression that is embedded in the model by the user. If the user does not provide a reverse expression that alters the scored value type, then the types will conform to the descriptions in the following tables. See "ALTER_REVERSE_EXPRESSION Procedure".
4. If the model is partitioned, the `result_table_name` can contain results from different partitions depending on the data from the input data table. An additional column called `PARTITION_NAME` is added to the result table indicating the partition name that is associated with each row.

For a non-partitioned model, the behavior does not change.

**Classification**

The results table for Classification has the columns described the table below. If the target of the model is categorical, the `PREDICTION` column will have a `VARCHAR2` datatype. If the target has a binary type, the `PREDICTION` column will have the binary type of the target.

---

**APPLY Results Table for Classification**

Column Name| Datatype | 
---------|----------|
 _Case ID column name_ | Type of the case ID | 
 `PREDICTION` | Type of the target | 
 `PROBABILITY` | `BINARY_DOUBLE` | 

---

**Anomaly Detection**

The results table for Anomaly Detection has the columns

**APPLY Results Table for Anomaly Detection**

Column Name| Datatype | 
---------|----------|
 _Case ID column name_ | Type of the case ID | 
 `PREDICTION` | `Number` | 
 `PROBABILITY` | `BINARY_DOUBLE` |

 ---

**Regression**

The results table for Regression has the columns 

**APPLY Results Table for Regression**

Column Name | Datatype | 
---------|----------|
 _Case ID column name_  | Type of the case ID | 
 `PREDICTION` | Type of the target | 

 ---

**Clustering**

Clustering is an unsupervised mining function, and hence there are no targets. The results of an APPLY procedure will contain simply the cluster identifier corresponding to a case, and the associated probability. The results table has the columns

**APPLY Results Table for Clustering**

Column Name| Datatype | 
---------|----------|
 _Case ID column name_ | Type of the case ID | 
 `PREDICTION` | `Number` | 
 `PROBABILITY` | `BINARY_DOUBLE` |

 ---

**Feature Extraction**

Feature Extraction is also an unsupervised mining function, and hence there are no targets. The results of an APPLY procedure will contain simply the feature identifier corresponding to a case, and the associated match quality. The results table has the columns described

**APPLY Results Table for Feature Extraction**

Column Name| Datatype | 
---------|----------|
 _Case ID column name_ | Type of the case ID | 
 `PREDICTION` | `Number` | 
 `PROBABILITY` | `BINARY_DOUBLE` 

**Examples**
This example applies the GLM Regression model `GLMR_SH_REGR_SAMPLE` to the data in the `MINING_DATA_APPLY_V` view. The APPLY results are output of the table `REGRESSION_APPLY_RESULT`.
```sql
SQL> BEGIN
       DBMS_DATA_MINING.APPLY (
       model_name     => 'glmr_sh_regr_sample',
       data_table_name     => 'mining_data_apply_v',
       case_id_column_name => 'cust_id',
       result_table_name   => 'regression_apply_result');
    END;
    /
 
SQL> SELECT * FROM regression_apply_result WHERE cust_id >  101485;
```

```
CUST_ID PREDICTION
---------------------
    101486 22.8048824
    101487 25.0261101
    101488 48.6146619
    101489   51.82595
    101490 22.6220714
    101491 61.3856816
    101492 24.1400748
    101493  58.034631
    101494 45.7253149
    101495 26.9763318
    101496 48.1433425
    101497 32.0573434
    101498 49.8965531
    101499  56.270656
    101500 21.1153047
```
## 43.7.5 COMPUTE_CONFUSION_MATRIX Procedure

## 43.7.11 CREATE_MODEL Procedure

This procedure creates a mining model with a given mining function.

Syntax
```sql
DBMS_DATA_MINING.CREATE_MODEL (
      model_name            IN VARCHAR2,
      mining_function       IN VARCHAR2,
      data_table_name       IN VARCHAR2,
      case_id_column_name   IN VARCHAR2,
      target_column_name    IN VARCHAR2 DEFAULT NULL,
      settings_table_name   IN VARCHAR2 DEFAULT NULL,
      data_schema_name      IN VARCHAR2 DEFAULT NULL,
      settings_schema_name  IN VARCHAR2 DEFAULT NULL,
      xform_list            IN TRANSFORM_LIST DEFAULT NULL);
```
**WIP**

## 43.7.17 EXPORT_MODEL Procedure   

## 43.7.40 IMPORT_MODEL Procedure

