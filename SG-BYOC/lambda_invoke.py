import os
import io
import boto3
import json

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
Bucket = os.environ['Bucket']
s3Prefix = os.environ['s3Prefix']

# grab runtime client
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    try:
        #Serialize data for endpoint
        data = json.loads(json.dumps(event))
        payload = json.dumps(data)
        # add two more key-value pairs to the dictionary
        data["Bucket"] = Bucket
        data["s3Prefix"] = s3Prefix
    
        # convert the updated dictionary back to JSON string
        updated_payload = json.dumps(data)
        
        # # Invoke the model. In this case the data type is a JSON
        
        response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/json',
                                       Body=updated_payload)
        #Parse results
        result = json.loads(response['Body'].read().decode())
        return result
        
    except Exception as e:
        # Return an error response if an exception occurs
        return {
            'statusCode': 500,
            'errorMessage': json.dumps({'An error occurred (ModelError) when calling the InvokeEndpoint operation': str(e)}),
            'errorType': "ModelError"
            }       