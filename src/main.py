import json
import boto3
import os
import logging
import uuid
import base64
import mimetypes

logger = logging.getLogger()
logger.setLevel("INFO")

def lambda_handler(event, context):
    """
    AWS Lambda handler function example.
    """

    try:
        # logger gives us insight with priority levels
        # info -> warn -> error
        logger.info("assembling response")

        # message to be served
        message = {
            "message": "Hello, world from Lambda!",
            "input_event": event  
        }

        return {
            # 200: success
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
                },
            # convert message to json equivalent
            "body": json.dumps(message)
        }
    
    # in case anything goes wrong, catch the error and serve it
    except Exception as e:
        logger.exception(e)
        return {
            # 500: server error
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    