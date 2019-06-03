#
# S3 list_objects_v2
#
import boto3

s3_client = boto3.client('s3')

for key in s3_client.list_objects_v2(
        Bucket='my_bucket_name',
        Prefix='my_path/to_some_data/',
        Delimiter="/")['Contents']:
    print(key['Key'])
