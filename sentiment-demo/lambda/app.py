import os
import json
import boto3

def handler(event, context):

    var string = "Hei, dette er en sykt bra test!"
    client = boto3.client('comprehend')
    body = event["body"]
    sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)
    return {
            console.log(string)
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment ": json.dumps(sentiment)
            })
    }
