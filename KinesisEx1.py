import boto3
import json
import random


nombres = ['Pablo', 'Pedro', 'Ariel', 'Enzo', 'Jorge','Tomás', 'Julian','Diego','Bruce']
apellidos = ['Perez', 'Troglio', 'Ortega', 'Francescoli', 'Montalvan', 'Agua', 'Weich', 'Maradona', 'Wayne']
empresas = ['Lambda', 'Dynamo', 'ApiGateway']
barrios = ['Flores', 'Caballito', 'Once', 'Monserrat', 'San Nicolás'] 

dynamodb = boto3.client('dynamodb')

i = 0
while i < 10000:
  nombre = random.choice(nombres) + " " + random.choice(apellidos)
  empresa = random.choice(empresas)
  barrio = random.choice(barrios)
  dynamodb.put_item(
    TableName='AprendiendoAWS', 
      Item={  
        'NombreParticipantes':{'S':(nombre)},
        'Empresa':{'S':(empresa)},
        'Barrio':{'S':(barrio)},
        'Edad':{'S':(str(random.randint(18,65)))}
        }
    )
  print (i)  
  i+=1

