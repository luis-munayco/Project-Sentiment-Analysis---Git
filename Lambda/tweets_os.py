import boto3 # Pyhton AWS SDK module
import re
import requests #library to send doc to dashboard
from requests_aws4auth import AWS4Auth
import json

def load(tweets):
  """
 	This function sent the json documento to OpenSearch
	
	Parameters
	----------
	tweets: json
		tweets analyzed in JSON format

	"""
  region = 'us-east-1' # e.g. 
  service = 'es'
  credentials = boto3.Session().get_credentials()
  awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
  
  host = 'https://search-twitter-sentiment-analysis-yjup572lhzcbw7cywde6fi3ll4.us-east-1.es.amazonaws.com'
  index = 'tweets_2test'
  type_ = '_doc'
  url = host + '/' + index + '/' + type_
  
  headers = { "Content-Type": "application/json" }
  document = json.loads(tweets,strict=False)
  r = requests.post(url, auth=awsauth, json=document, headers=headers)
  print("r.status_code:    ", r.status_code)
