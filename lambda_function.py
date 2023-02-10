# function.py:
import json
import psycopg2
import psycopg2.extras
import os


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from github Lambda!')
    }
