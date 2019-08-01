# OCI Cli

Please follow https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliinstall.htm to install OCI Cli.

## Object Storage

To upload a file to the object storage. 

```bash
oci os object put \
-ns <object_storage_namespace> \
-bn <bucket_name> \
--file <file_location> \
--name <object_name> \
--part-size <upload_part_size_in_MB> \ (optional)
--parallel-upload-count <maximum_number_parallel_uploads> (optional)
```

To download a file from the object storage. 

* `-bn` - bucketname
* `--file` - file path and name
* `--name` - name of the file in the bucket

```bash
oci os object get -bn samplebucket --file /home/oracle/tmp/test.txt --name test.txt
```


