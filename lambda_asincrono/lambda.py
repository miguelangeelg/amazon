import csv
import json
import boto3
from io import StringIO

def readcsv(content):
    # Use StringIO to treat the content as a file-like object
    csv_reader = csv.DictReader(StringIO(content))
    
    # Map the actual headers to expected headers
    header_mapping = {
        'Miguel': 'name',
        'Gutierrez': 'lastName'
        # Add more mappings as needed
    }
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table-miguel')
    
    for row in csv_reader:
        print(row)
        # Transform actual headers to expected headers
        transformed_row = {header_mapping[actual_header]: value for actual_header, value in row.items()}
        
        # Check if the row has at least two elements (name and lastName)
        if 'name' in transformed_row and 'lastName' in transformed_row:
            item = {
                'name': transformed_row['name'],
                'lastName': transformed_row['lastName']
            }
            table.put_item(Item=item)
        else:
            print(f"Skipping invalid row: {row}")

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    
    response = s3.get_object(Bucket=bucket, Key=objeto)
    csvfile = response['Body'].read().decode('utf-8')
    
    readcsv(csvfile)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
