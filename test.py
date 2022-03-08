from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from pandas.io.json import json_normalize
import boto3

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('./client-secret.json', scope)

session = boto3.Session( 
        aws_access_key_id='AKIAZAV32EZOOJQX7FG4', 
        aws_secret_access_key='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'
        )

#client = session.client(service_name='ec2', region_name="us-west-2")
client = session.client(service_name='rds', region_name="us-west-2")

""" response = client.describe_db_engine_versions(
    Engine='MySQL',
    EngineVersion='8.0.23'
) """
#response = client.describe_instance_types()
""" response = client.describe_db_instance_types()

f = open("instance_types.json", "a")
f.write(json.dumps(response))
f.close() """


""" client = session.client(service_name='rds', region_name="us-west-2")
response = client.describe_instance_types()

f = open("instance_types.json", "a")
f.write(response)
f.close() """

response = client.describe_orderable_db_instance_options(
    Engine='aurora-mysql'
)

f = open("instance_types.json", "a")
f.write(json.dumps(response))
f.close()

print(response)