import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        "headers": {
            "Content-Type": "application/json",
        },        
        'body': json.dumps(event, indent=4)
    }
