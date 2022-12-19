import json
import urllib.parse 
import boto3 # Pyhton AWS SDK module
import logging # Logging module
import twitter_to_os # Module to connect with OpenSearch y send the documents to the dashboard
from tweet_utils import analize_tweet # Funtion to perform sentiment analysis in tweets

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Loading function')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info("test")
    logger.info(event)
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
        
        try:
            #Get tweets information
            response = s3.get_object(Bucket=bucket, Key=key)
            s3_file_content = response['Body'].read().decode('utf-8')
            tweets = s3_file_content.split('endtuit')
            
            #Analize tweets
            for tweet in tweets:
                tuits = tweet.split('tuit-location')
                doc={"test":"lambda"}
                if len(tuits) == 3:
                    #Check tweet format
                    doc = analize_tweet(tuits[0], tuits[1], tuits[2])
                    
                try:
                    twitter_to_os.load(doc) # Send doc to OpenSearch dashboard
                except Exception as e:
                    logger.info(e)
                    logger.info('Error loading data into OpenSearch')

        except Exception as e:
            logger.info(e)
            logger.info('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
            