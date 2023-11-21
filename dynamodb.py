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

# create function to create a table in dynamodb with capacity under demand
def create_table(name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    print("Tabla creada exitosamente")


option = 1
while option != 0:
    print("Ingrese la opcion que desea")
    print("1. Listar tablas de la cuenta")
    print("2. Crear una tabla")
    option = int(input())
    if option == 1:
        list_tables()
    elif option == 2:
        print("Ingrese nombre para la tabla")
        name = str(input())
        create_table(name)
    elif option == 0:
        print("Hasta luego")
    else:
        print("Opcion invalida")
