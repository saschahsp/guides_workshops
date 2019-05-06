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

