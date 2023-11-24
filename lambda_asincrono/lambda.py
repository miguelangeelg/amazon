import csv
import json
import boto3
from io import StringIO

def readcsv(content):
    # Use StringIO to treat the content as a file-like object
    csv_reader = csv.DictReader(StringIO(content))
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table-miguel')
    
    for row in csv_reader:
        item = {
            'name': row[0],
            'lastName': row[1]
        }
        table.put_item(Item=item)

def lambda_handler(event, context):
    # Extract bucket and object information from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    
    # Retrieve the content of the CSV file from S3
    response = s3.get_object(Bucket=bucket, Key=objeto)
    csv_content = response['Body'].read().decode('utf-8')
    
    # Call the readcsv function with the content of the CSV file
    readcsv(csv_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
