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

Define test variables. 

```python
bucket_name = "sommeruni"
object_name = "test.txt"
my_data = "Hello, World!"
```

Create a bucket (can obviously be skipped if a bucket already exists)

```python
print("Creating a new bucket {!r} in compartment {!r}".format(bucket_name, compartment_id))
request = CreateBucketDetails()
request.compartment_id = compartment_id
request.name = bucket_name
bucket = object_storage.create_bucket(namespace, request)
```

Create a file and write the content into the file. 

```python
print("Uploading new object {!r}".format(object_name))
obj = object_storage.put_object(
    namespace,
    bucket_name,
    object_name,
    my_data)
```

Get the file into your python environment. 

```python
same_obj = object_storage.get_object(
    namespace,
    bucket_name,
    object_name)
print(same_obj)

print("{!r} == {!r}: {}".format(
    my_data, same_obj.data.content,
    my_data == same_obj.data.content))
```

Upload a sample file to the object storage

```python
print('Uploading a file to object storage')

# First create a sample file
sample_content = b'a' * 1024 * 1024 * 5
with open('example_file', 'wb') as f:
    f.write(sample_content)
```

Upload a local file to the object storage. 

```python
# Then upload the file to Object Storage
example_file_object_name = 'newtest.txt'
with open('/home/oracle/newtest.txt', 'rb') as f:
    obj = object_storage.put_object(namespace, bucket_name, example_file_object_name, f)
```

Retrieve the file, streaming it into another file in 1 MiB chunks

```python
print('Retrieving file from object storage')
get_obj = object_storage.get_object(namespace, bucket_name, example_file_object_name)
with open('example_file_retrieved', 'wb') as f:
    for chunk in get_obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)

print('Uploaded and downloaded files are the same: {}'.format(filecmp.cmp('/home/oracle/newtest.txt', 'example_file_retrieved')))
```

Commands to clean the environment.

```python
print("Deleting object {}".format(object_name))
object_storage.delete_object(namespace, bucket_name, object_name)

print("Deleting object {}".format(example_file_object_name))
object_storage.delete_object(namespace, bucket_name, example_file_object_name)

print("Deleting bucket {}".format(bucket_name))
object_storage.delete_bucket(namespace, bucket_name)
```