
import json

# read a file csv function
def read_csv(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines



def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    

    
    

data = read_csv('file.csv')
print(data)