import boto3
import geocoder
import re
import random
import time
import json
from tweepy.streaming import StreamingClient
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamRule


def get_location(city):
  """
    This function get the geolocation (latitude,longitud) given a city name.
    
    Parameters
    ----------
    city: str
      City name
    
    Returns
    -------
    Geopoint: Geo_Point 
      Contains the latitud and longitud of a given city.
  """
  g = geocoder.bing(city, key='')
  results = g.json
  try:
    return "tuit-location[" + str(results['lng']) + "," + str(results['lat']) + "]"
  except:
    return "tuit-location[0,0]"

def clean_tweet(tweet_text):
  """
  This function clean the tweet so it can be analyzed.
  
  Parameters
  ----------
  tweet_text: str
    Original tweet
  
  Returns
  -------
  temp: str
    Cleaned tweet
  """
  # Replace NON-ASCII with space
  cleaned_text = tweet_text#''.join([i if ord(i) < 128 else '' for i in tweet_text])

  temp = cleaned_text.lower()
  temp = re.sub("@[A-Za-z0-9_]+","", temp)
  temp = re.sub("#[A-Za-z0-9_]+","", temp)
  temp = re.sub(r"http\S+", "", temp)
  temp = re.sub(r"http", "", temp)
  temp = re.sub(r"www.\S+", "", temp)
  temp = re.sub(r"rt : ", "", temp)
  temp = temp. rstrip('\n')
  return temp

#Variables that contains the user credentials to access Twitter API
Bearer_token=''

#Delivery Stream Name of Kinesis Firehose
DeliveryStreamName = 'PUT-S3-J7hLV'

#Client to be used with kinesis firehose
client = boto3.client('firehose', region_name='us-east-1',
                          aws_access_key_id='', 
                          aws_secret_access_key=''
                          )

#This is a basic listener that just prints received tweets and put them into the stream.
class StdOutListener(StreamingClient):
  """
    This Subclass generate a tweets stream inheriting from a parent class StreamingClient 
    
    Parameters
    ----------
    StreamingClient: StreamingClient V2
      Original tweet

  """
  def on_data(self, data):  
    if "location" in json.loads(data)["includes"]["users"][0]:
     client.put_record(DeliveryStreamName=DeliveryStreamName,
                      Record={'Data': clean_tweet(json.loads(data)["data"]["text"]) + "tuit-location" + str(json.loads(data)["includes"]["users"][0]["location"]) + get_location(str(json.loads(data)["includes"]["users"][0]["location"])) + " endtuit"})
     print (json.loads(data))
    return True

  def on_error(self, status):
      print (status)

#Generate tweets stream
stream = StdOutListener(Bearer_token)
stream.add_rules(StreamRule(["Dina Boluarte", "nuevas elecciones", "Peru"])) #adding the rules
stream.filter(user_fields=['location'],expansions=['author_id']) #runs the stream