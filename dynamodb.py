import boto3
import uuid

#create a function to list tables of dynamodb
def list_tables2():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)


def list_tables(string):
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        if string in table.name:
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

# create a function complete to insert a register in a dynamodb table
def insert_register(table, name, lastName):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    table.put_item(
        Item = {
            'id': str(uuid.uuid4()),
            'name': name,
            'lastName': lastName
        }
    )
    print("Registro insertado!")
    

def select_register(table, id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    if id == "":
        for item in table.scan()['Items']:
            print(item)
    else:
        item = table.get_item(Key={'id': id})['Item']
        print(item)
        
# create function to delete a register in a dynamodb table
def delete_register(table, id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    table.delete_item(Key={'id': id})
    print("Registro eliminado")
    
# reconocer celebridad en imagen
def recognize_celebrity(image):
    rekognition = boto3.client('rekognition')
    response = rekognition.recognize_celebrities(Image={'Bytes': imagen})
    print(response['CelebrityFaces'][0]['Name'])


option = 1
while option != 0:
    print("Ingrese la opcion que desea")
    print("1. Listar tablas de la cuenta")
    print("2. Crear una tabla")
    print("3. Insert a document")
    print("4. Consultar registros")
    print("5. Eliminar un registro")
    print("6. Reconocer celebridad via imagen")
    option = int(input())
    if option == 1:
        list_tables("miguel")
    elif option == 2:
        print("Ingrese nombre para la tabla")
        name = str(input())
        create_table(name)
    elif option == 3:
        print("Ingrese nombre de la tabla")
        tableName = str(input())
        print("Ingrese nombre")
        name = str(input())
        print("Ingrese apellido")
        lastName = str(input())
        insert_register(tableName, name, lastName)
    elif option == 4:
        print("Ingrese nombre de la tabla")
        print("Estas son sus tablas:")
        list_tables("miguel")
        tableName = str(input())
        print("Ingrese id (Si lo deja vacio se traeran todos los registros)")
        id = str(input())
        select_register(tableName, id)
    elif option == 5:
        print("Ingrese nombre de la tabla")
        print("Estas son sus tablas:")
        list_tables("miguel")
        tableName = str(input())
        print("Ingrese id")
        id = str(input())
        delete_register(tableName, id)
    elif option == 6:
     with open("IMAGEN.png", "rb") as f:
            imagen = f.read()
            recognize_celebrity(imagen)
    elif option == 0:
        print("Hasta luego")
    else:
        print("Opcion invalida")
