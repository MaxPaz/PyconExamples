import json
import boto3
import time
from time import gmtime, strftime

stream_name = "PyconStream"
kinesis_client = boto3.client('kinesis')
response_stream = kinesis_client.describe_stream(StreamName=stream_name)
my_shard_id = response_stream['StreamDescription']['Shards'][0]['ShardId']

shard_it = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=my_shard_id,
    ShardIteratorType='LATEST'
)
response = kinesis_client.get_records(
    ShardIterator=shard_it['ShardIterator'],
    Limit=500
)
while 'NextShardIterator' in response:
    record_responses = kinesis_client.get_records(ShardIterator=response['NextShardIterator'],
                                                  Limit=500)[u"Records"]
    print (record_responses)

    for record_response in record_responses:
        datum = json.loads(record_response[u'Data'])
        print(json.dumps(datum, indent=4, sort_keys=True))

