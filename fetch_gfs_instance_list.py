import json
import boto3
import os
import base64
from botocore.exceptions import ClientError

def create_template_inventory_file():
    f = open("inventory.txt", "a")
    f.write("[gssdev]" + '\n')
    f.close()

def get_list_of_instances(tag_name, tag_value):
    instance_list = []
    client = boto3.client('ec2', region_name='us-east-1')
    custom_filter = [
            {
                'Name': 'tag:' + tag_name,
                'Values': [tag_value]
            }]
    response = client.describe_instances(Filters=custom_filter)
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    if instance["State"]["Name"] == "running":
                        f = open("inventory.txt", "a")
                        f.write(instance["PrivateIpAddress"] + '\n')
                        f.close()
    return instance_list

# itam_list = ['BRM-B2B-GSS-APP-AWS', 'brm-GSS-APP-AWS', 'BRP-GSS-APP-AWS', 'brp-B2B-GSS-APP-AWS', 'BRP-B2B-GSS-APP-AWS', 'brp-GSS-APP-AWS', 'BIP-GSS-APP-AWS', 'bip-B2B-GSS-APP-AWS', 'BIP-B2B-GSS-APP-AWS', 'bip-GSS-APP-AWS', 'C2O-B2B-GSS-APP-AWS', 'C2O-GSS-APP-AWS', 'c2o-GSS-APP-AWS', 'c2o-GSS-APP-AWS']
itam_list = ['log']
create_template_inventory_file()
for itam in itam_list:
    get_list_of_instances('ITAM3', itam)
