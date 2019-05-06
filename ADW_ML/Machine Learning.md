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



