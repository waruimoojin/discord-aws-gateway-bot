import json
import boto3
from botocore.exceptions import ClientError

# AWS S3 Configuration
BUCKET_NAME = 'employee-photo-bucket-0011'
FILE_NAME = 'messages.txt'

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract the request body from the API Gateway event
    try:
        body = json.loads(event['body'])
    except KeyError:
        return {
            "statusCode": 400,
            "body": json.dumps("Invalid request, missing body.")
        }

    # Extract the content of the message
    message_content = body.get('content')
    
    # Check if the message contains a specific text
    if message_content == "test123":
        # Save the message to S3
        try:
            s3.put_object(
                Bucket=BUCKET_NAME, 
                Key=FILE_NAME, 
                Body=f"Message received: {message_content}\n".encode()
            )
            return {
                "statusCode": 200,
                "body": json.dumps("Specific message received and saved to S3.")
            }
        except ClientError as e:
            return {
                "statusCode": 500,
                "body": json.dumps(f"Error saving to S3: {e}")
            }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps("No action required for this message.")
        }
