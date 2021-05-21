import boto3
import json
from datetime import datetime
import time
 
my_stream_name = "PyconStream"
 
kinesis_client = boto3.client('kinesis')
response = kinesis_client.describe_stream(StreamName=my_stream_name)
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
 
shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                ShardId=my_shard_id,
                ShardIteratorType='LATEST') # values can be: AT_SEQUENCE_NUMBER, AFTER_SEQUENCE_NUMBER, LATEST & TRIM_HORIZON
my_shard_iterator = shard_iterator['ShardIterator']
 
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=100)
while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=100)
 
    print (record_response)
 
    # wait for 2 seconds until next run
    time.sleep(2)