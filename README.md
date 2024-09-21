
# Windy API Forecast Lambda

This project is an AWS Lambda function built using AWS SAM (Serverless Application Model) to fetch weather data from the [Windy API](https://api.windy.com) using a secure API key stored in AWS Secrets Manager.

## Features
- AWS Lambda function written in Python.
- Integration with the Windy API to fetch weather forecasts for specified coordinates.
- API key is securely retrieved from AWS Secrets Manager.
- Deployed using AWS SAM with an API Gateway as the front end for accessing the Lambda function.

## Project Structure

```
windy-lambda/
├── windyAPI.py               # Lambda function code
├── sam_template.yaml        # SAM template for Lambda, API Gateway, and IAM roles
└── requirements.txt     # Python dependencies (requests, boto3)
```

### Files:
- **`windyAP.py`**: Contains the Lambda function that calls the Windy API.
- **`sam_template.yaml`**: AWS SAM template defining the Lambda function, API Gateway, and IAM role with access to Secrets Manager.
- **`requirements.txt`**: Lists the dependencies (`requests`, `boto3`).

## Prerequisites

- AWS account with the necessary permissions (Lambda, API Gateway, Secrets Manager).
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) installed.
- Python 3.9 or 3.12 installed.

## Setup

### Step 1: Install Dependencies

Install Python dependencies by running the following command in the project directory:

```bash
pip install -r requirements.txt
```

### Step 2: Configure AWS Secrets Manager

Store your Windy API key securely in AWS Secrets Manager:
1. Go to AWS Secrets Manager in the AWS Console.
2. Create a new secret with a key-value pair like this:
   ```json
   {
     "WINDY_API_KEY": "your-windy-api-key"
   }
   ```
3. Name the secret **WindyAPIKey**.

### Step 3: Build and Deploy the SAM Application

To deploy the application:

1. **Build the SAM Application**:

   ```bash
   sam build --template-file sam_template.yaml
   ```

2. **Deploy the SAM Application**:

   ```bash
   sam deploy --guided
   ```

   Follow the prompts and provide the necessary information (stack name, AWS region, etc.). The `sam deploy` command will deploy the Lambda function and API Gateway.

### Step 4: Test the API

After deployment, you will get an API Gateway endpoint. You can test it using `curl` or your browser.

Example with `curl`:
```bash
curl "https://<api-id>.execute-api.<region>.amazonaws.com/Prod/forecast?lat=44.64&lon=-63.58"
```

This request will return the weather forecast for the given latitude and longitude.

## Undeploying the Application

To remove the deployed resources:

1. Go to AWS CloudFormation in the AWS Console.
2. Find the stack you deployed.
3. Select the stack and click **Delete** to remove all associated resources (Lambda, API Gateway, IAM roles, etc.).

Alternatively, you can use the AWS CLI to delete the stack:

```bash
aws cloudformation delete-stack --stack-name your-stack-name
```

## Notes
- Make sure you have appropriate permissions to deploy Lambda, API Gateway, and IAM roles.
- Ensure your API key is stored securely in AWS Secrets Manager.
