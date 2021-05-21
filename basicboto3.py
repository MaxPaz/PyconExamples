
print("######Resource######")
import boto3
import datetime
print ("startime: " + str(datetime.datetime.utcnow()))
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
    if i.state['Name'] == 'stopped':
        print (i.instance_id, i.instance_type)
print ("endtime: " + str(datetime.datetime.utcnow()))

print("######Client######")
import boto3
import datetime
print ("startime: " + str(datetime.datetime.utcnow()))
ec2 = boto3.client('ec2')
ec2_list = ec2.describe_instances(Filters=[{'Name':'instance-state-name', 'Values': ['stopped',],},],)
for instance in ec2_list['Reservations']:
    for i in instance['Instances']:
        print (i['InstanceId'], i['InstanceType'])
print ("endtime: " + str(datetime.datetime.utcnow()))