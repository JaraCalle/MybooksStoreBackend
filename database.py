import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración DynamoDB
dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "fake"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "fake"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN", "fake")
)

# Crear tabla (ejecutar una sola vez)
def create_books_table():
    table_name = "Books"
    existing_tables = dynamodb.meta.client.list_tables()["TableNames"]
    if table_name not in existing_tables:
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
        )
        print("Tabla creada:", table_name)

create_books_table()
books_table = dynamodb.Table("Books")
