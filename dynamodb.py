import boto3

print(boto3)

#create a function to list tables of dynamodb
def list_tables():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
        

#create a function to show tables of prueba table
def show_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('prueba')
    for item in table.scan()['Items']:
        print(item) 

show_table()

