import json
import os
import boto3
import datetime

ddb = boto3.client("dynamodb", region_name='us-west-1')
DDBTable = os.environ['HITS_TABLE_NAME']

def handler(event, context):
    if 'queryStringParameters' in event and 'Nombre' in event['queryStringParameters']:
        Nombre = event["queryStringParameters"]["Nombre"]
    else:
        Nombre = ''
    print (Nombre)
    data = {
        'output': 'Hola ' + (Nombre) + ', bienvenido al PyconAR',
        'timestamp': datetime.datetime.utcnow().isoformat()
        }
    ddb.put_item(TableName=DDBTable, 
                Item={  
                        'Id':{'S':(datetime.datetime.utcnow().isoformat()),},
                        'Evento':{'S':'PyconAR',},
                        'Nombre':{'S': Nombre,},
                    }
                )
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
