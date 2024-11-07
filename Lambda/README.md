# AWS Lambda Function for Storing Discord Messages

This AWS Lambda function is designed to receive and process messages sent from a Discord bot via an API Gateway. When the Lambda function receives a message containing specific content (e.g., "test123"), it stores the message in an Amazon S3 bucket.

## Functionality

- **Receives POST requests** from the API Gateway containing message data from Discord.
- **Extracts message content** from the request body.
- **Validates message content** to check for a specific keyword or trigger phrase.
- **Stores message content in an S3 bucket** if the content matches the expected trigger phrase.
- **Responds with a status message** to confirm whether the message was processed successfully.

## Folder Contents

- `lambda_function.py`: The main code for the Lambda function.
- `requirements.txt`: A list of dependencies, if any, required for the Lambda function.
- `.env.example`: Template for environment variables (if needed).

## Usage

Deploy this function to AWS Lambda and connect it to an API Gateway endpoint. Configure the Discord bot to send HTTP POST requests to this endpoint, triggering the Lambda function whenever a relevant message is sent in the Discord channel.
