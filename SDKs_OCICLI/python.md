# Python SDK

For further documentation: https://github.com/oracle/oci-python-sdk 

To install the Python SDK:

```sh
pip install oci
```

## Object Storage

Let's download and upload a file to a bucket in the object storage. 

First we need to import the libraries. 

`filecmp` is just for comparison of the files. 

```python
import filecmp
import oci
from oci.object_storage.models import CreateBucketDetails
import os
import pandas as pd
import io
from PIL import Image
from io import StringIO
```

Load the config file.

```python
config = oci.config.from_file("/home/oracle/.oci/config", "DEFAULT")
```

Check user identity / user data.

```python
identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data
print(user)
```

Display some information.

```python
compartment_id = config["tenancy"]
print(compartment_id)
object_storage = oci.object_storage.ObjectStorageClient(config)
print(object_storage)
namespace = object_storage.get_namespace().data
print(namespace)
```

Define bucket.  

```python
bucket_name = "sommeruni"
bucket = object_storage.get_bucket(namespace, bucket_name)
```

Get object list. 

```python
object_list = object_storage.list_objects(namespace, bucket_name)
for o in object_list.data.objects:
    print(o.name)
```

Upload new file.

```python
with open('home/oracle/uploadnewfile.txt', 'r') as f:
    obj = object_storage.put_object(namespace, bucket_name, 'uploadnewfile.txt', f)
```

Download file and save it locally.

```python
object_name = "bag01.jpg"
destination_dir = '/home/oracle/tmp'.format(object_name) 
get_obj = object_storage.get_object(namespace, bucket_name, object_name)
with open(os.path.join(destination_dir,object_name), 'wb') as f:
    for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)
```

Download file and write it into a variable.

```python
#object_name = "bag01.jpg"
object_name = "newtest.txt"
#destination_dir = '/home/oracle/tmp'.format(object_name) 
get_obj = object_storage.get_object(namespace, bucket_name, object_name)
for chunktest in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
    chunktest
```

It is saved as bytes.

```python
print(type(chunktest))
chunktest
```

For images. Convert to PIL image.

```python
imageStream = io.BytesIO(chunktest)
imageFile = Image.open(imageStream)
type(imageFile)
print(imageFile.size)
```

Display image.

```python
imageFile
```

For txt/csv/... files. 

```python
s=str(chunktest,'utf-8')
data = StringIO(s)
type(data)
```

This data is an IO String.

```python
contents = data.getvalue()
contents
```

We can read the IO String with pandas and create a Pandas Dataframe

```python
df=pd.read_csv(data)
df
```

