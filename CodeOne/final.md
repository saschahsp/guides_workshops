
# Data Science

## Conda 

conda activate tf-cpu

## Notebook

jupyter notebook --NotebookApp.token='' --ip=0.0.0.0 --port=8888

## Docker

### Big Data ?

//cloudera quickstart
sudo docker container run -it -p 8000-8001:8000-8001 -p 8081:8081 3f8612a3ff52 sh

### Tensorflow Serving

sudo docker run -d --name serving_base tensorflow/serving
sudo docker cp /home/opc/oco/tfservingflask/models serving_base:/models/1
sudo docker commit --change "ENV MODEL_NAME 1" serving_base oco/serving_base_cloths:v1
//sudo docker kill serving_base
sudo docker run -p 8501:8501 -t oco/serving_base_cloths:v1

## Firewall

sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --add-port=8080/tcp
sudo firewall-cmd --add-port=8501/tcp
sudo firewall-cmd --add-port=5000/tcp

## Flask

export FLASK_APP=/home/opc/oco/tfservingflask/app.py
export FLASK_ENV=development && flask run --host=0.0.0.0

# Big Data

## VNC

su -c "vncserver -depth 32 -geometry 1024x768" oracle

## PW

WElcome_123#

## oci-hdfs

<property>
  <name>fs.oci.client.hostname</name>
  <value>https://objectstorage.us-phoenix-1.oraclecloud.com</value>
</property>

<property>
  <name>fs.oci.client.hostname.myBucket.myNamespace</name>
  <value>https://objectstorage.bigdataprep@sehubpilot.oraclecloud.com</value><!-- Use Phoenix for bigdataprep@sehubpilot -->
</property>

<property>
  <name>fs.oci.client.auth.tenantId</name>
  <value>ocid1.tenancy.oc1..aaaaaaaatx62bxouthg6dqnqfxzdpbumb3rcq5dl7fn7xpdmlfytdx3v7xqq</value>
</property>

<property>
  <name>fs.oci.client.auth.userId</name>
  <value>ocid1.user.oc1..aaaaaaaaadnydxfkoixuwmv6h4uvscixrlpzhxqe6wc3rwbu7bmay2wr7rma</value>
</property>

<property>
  <name>fs.oci.client.auth.fingerprint</name>
  <value>30:72:17:ca:8e:45:f4:0e:2b:16:c8:9b:36:ac:b2:58</value>
</property>

<property>
  <name>fs.oci.client.auth.pemfilepath</name>
  <value>/home/oracle/.oci/oci_api_key.pem</value>
</property>

