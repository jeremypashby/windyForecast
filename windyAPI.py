import requests
import boto3
import json

def get_secret():
    secret_name = "WindyAPIKey"
    region_name = "ca-central-1" # set your region yoour secret is in

    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e

    secret = get_secret_value_response['SecretString']
    secret_json = json.loads(secret)
    return secret_json['WindyAPIKey']

def lambda_handler(event, context):
    api_key = get_secret()
    lat = event.get('lat', 44.647430) # Latitude, default to Halifax, Nova Scotia
    lon = event.get('lon', -63.580219) # Longitude, default Halifax, Nova Scotia

    url = "https://api.windy.com/api/point-forecast/v2"
    params = {
        "lat": lat,
        "lon": lon,
        "model": "gfs",
        "parameters": ["temp", "precip", "wind"],
        "key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        forecast_data = response.json()
        return {
            'statusCode': 200,
            'body': json.dumps(forecast_data)
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Failed to fetch data'
        }
