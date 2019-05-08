# Example Logistic Regression

## Display the SH.SUPPLEMENTARY_DEMOGRAPHICS Data

```sql
%sql
Select * from SH.SUPPLEMENTARY_DEMOGRAPHICS;
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/50.PNG)

## Clean up and drop table if already exists and create Data table 

```sql
%script
/*  Clean out old table  */

BEGIN
      EXECUTE IMMEDIATE 'DROP Table SUPPLEMENTARY_DEMOGRAPHICS2';
  EXCEPTION
      WHEN OTHERS THEN NULL;
END;
/

/*  Create SUPPLEMENTARY_DEMOGRAPHICS2 table  */

CREATE Table SUPPLEMENTARY_DEMOGRAPHICS2 
  AS (SELECT AFFINITY_CARD, BOOKKEEPING_APPLICATION, BULK_PACK_DISKETTES, CUST_ID, EDUCATION, FLAT_PANEL_MONITOR, HOME_THEATER_PACKAGE, HOUSEHOLD_SIZE, OCCUPATION, OS_DOC_SET_KANJI, PRINTER_SUPPLIES, YRS_RESIDENCE, Y_BOX_GAMES
      FROM SH.SUPPLEMENTARY_DEMOGRAPHICS);
```

## Preparatory Steps, Automation of Model Build and Test andClean up using PL/SQL script

```sql
%script
/* Build a classification model and then generate a lift test result and an apply result.  */

DECLARE
v_sql varchar2(100);

BEGIN


/*  drop build settings  */
BEGIN
v_sql := 'DROP TABLE n1_build_settings PURGE';
EXECUTE IMMEDIATE v_sql;
DBMS_OUTPUT.PUT_LINE (v_sql ||': succeeded');
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE (v_sql ||': drop unneccessary - no table exists');
END;

/*  drop model  */
BEGIN
v_sql := 'CALL DBMS_DATA_MINING.DROP_MODEL(''N1_CLASS_MODEL'')';
EXECUTE IMMEDIATE v_sql;
DBMS_OUTPUT.PUT_LINE (v_sql ||': succeeded');
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE (v_sql ||': drop unneccessary - no model exists');
END;

/*  drop apply result  */
BEGIN
v_sql := 'DROP TABLE N1_APPLY_RESULT PURGE';
EXECUTE IMMEDIATE v_sql;
DBMS_OUTPUT.PUT_LINE (v_sql ||': succeeded');
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE (v_sql ||': drop unneccessary - no table exists');
END;

/*  drop lift result  */
BEGIN
v_sql := 'DROP TABLE N1_LIFT_TABLE PURGE';
EXECUTE IMMEDIATE v_sql;
DBMS_OUTPUT.PUT_LINE (v_sql ||': succeeded');
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE (v_sql ||': drop unneccessary - no table exists');
END;


/*  Split the Data into N1_TRAIN_DATA and N1_TEST_DATA  */
EXECUTE IMMEDIATE 'CREATE OR REPLACE VIEW N1_TRAIN_DATA AS SELECT * FROM SUPPLEMENTARY_DEMOGRAPHICS2 SAMPLE (60) SEED (1)';
DBMS_OUTPUT.PUT_LINE ('Created N1_TRAIN_DATA');
EXECUTE IMMEDIATE 'CREATE OR REPLACE VIEW N1_TEST_DATA AS SELECT * FROM SUPPLEMENTARY_DEMOGRAPHICS2 MINUS SELECT * FROM N1_TRAIN_DATA';
DBMS_OUTPUT.PUT_LINE ('Created N1_TEST_DATA');

/*  Create a Build Setting (DT) for Model Build  */

EXECUTE IMMEDIATE 'CREATE TABLE n1_build_settings (setting_name VARCHAR2(30),setting_value VARCHAR2(4000))';
EXECUTE IMMEDIATE 'INSERT INTO n1_build_settings (setting_name, setting_value) VALUES (''ALGO_NAME'', ''ALGO_GENERALIZED_LINEAR_MODEL'')';
EXECUTE IMMEDIATE 'INSERT INTO n1_build_settings (setting_name, setting_value) VALUES (''PREP_AUTO'', ''ON'')';

/*

This setting enables fully automated data preparation.

The default is PREP_AUTO_ON.

PREP_SCALE_2DNUM:

This setting enables scaling data preparation for two-dimensional numeric columns.

PREP_AUTO must be OFF for this setting to take effect. The following are the possible values:

- PREP_SCALE_STDDEV: A request to divide the column values by the standard deviation of the column and is often provided together with

- PREP_SHIFT_MEAN to yield z-score normalization.

*/

DBMS_OUTPUT.PUT_LINE ('Created model build settings table: n1_build_settings ');
    
/*  Build a Classification Model  */

EXECUTE IMMEDIATE 'CALL DBMS_DATA_MINING.CREATE_MODEL(''N1_CLASS_MODEL'', ''CLASSIFICATION'', ''N1_TRAIN_DATA'', ''CUST_ID'','' AFFINITY_CARD'', ''n1_build_settings'')';
DBMS_OUTPUT.PUT_LINE ('Created model: N1_CLASS_MODEL ');

/*  Test the Model by generating a apply result and then create a lift result  */

EXECUTE IMMEDIATE 'CALL DBMS_DATA_MINING.APPLY(''N1_CLASS_MODEL'',''N1_TEST_DATA'',''CUST_ID'',''N1_APPLY_RESULT'')';
DBMS_OUTPUT.PUT_LINE ('Created apply result: N1_APPLY_RESULT ');
-- EXECUTE IMMEDIATE 'CALL DBMS_DATA_MINING.COMPUTE_LIFT(''N1_APPLY_RESULT'',''N1_TEST_DATA'',''CUST_ID'',''AFFINITY_CARD'',''N1_LIFT_TABLE'',''1'',''PREDICTION'',''PROBABILITY'',100)';
-- DBMS_OUTPUT.PUT_LINE ('Created lift result: N1_LIFT_TABLE ');
--EXECUTE IMMEDIATE 'CALL DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX(''v_accuracy'', ''N1_APPLY_RESULT'',''N1_TEST_DATA'',''CUST_ID'',''AFFINITY_CARD'',''nb_confusion_matrix'',''PREDICTION'',''PROBABILITY'')';
--DBMS_OUTPUT.PUT_LINE ('Created confusion matrix: v_accuracy & nb_confusion_matrix');



END;
```

## More Information

**Model settings**

```sql
%sql 
SELECT setting_name, setting_value 
  FROM user_mining_model_settings 
 WHERE model_name = 'N1_CLASS_MODEL' 
ORDER BY setting_name;
```
![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/51.PNG)

---

**Data information**

```sql
%sql  
SELECT attribute_name, attribute_type 
  FROM user_mining_model_attributes 
 WHERE model_name = 'N1_CLASS_MODEL'
ORDER BY attribute_name;
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/52.PNG)

---

**Overview Mining Funtions**

```sql
%sql  
SELECT mining_function, algorithm 
  FROM user_mining_models 
 WHERE model_name = 'N1_CLASS_MODEL';
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/53.PNG)

## Prediction Results

```sql
%sql
select * from N1_APPLY_RESULT order by cust_id;
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/54.PNG)

## Compute Performance Metrics

**Confusion Matrix**

```sql
%script
DECLARE
v_sql varchar2(100);
/*  drop build settings  */

BEGIN
v_sql := 'DROP TABLE nb_confusion_matrix PURGE';
EXECUTE IMMEDIATE v_sql;
DBMS_OUTPUT.PUT_LINE (v_sql ||': succeeded');
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE (v_sql ||': drop unneccessary - no table exists');
END;

DECLARE
v_accuracy NUMBER;
BEGIN
DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX(v_accuracy, 'N1_APPLY_RESULT','N1_TEST_DATA','CUST_ID','AFFINITY_CARD','nb_confusion_matrix','PREDICTION','PROBABILITY');
DBMS_OUTPUT.PUT_LINE('**** MODEL ACCURACY ****: ' || ROUND(v_accuracy,4));
END;
/
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/55.PNG)

```sql
%sql

select * from nb_confusion_matrix;
```

![](https://github.com/saschahsp/guides_workshops/blob/master/ADW_ML/img/56.PNG)