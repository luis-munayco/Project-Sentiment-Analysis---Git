# Project-Sentiment-Analysis---Git

Sentiment analysis of tweets using AWS Serverless Services
The goal of this project is developed a full data pipeline using python and AWS Services in order to analyze tweets information and show the results in an OpenSearch dashboard. An specific topic is chosen in the python script to narrowed the results.

Objectives and tasks:

1. Generate a tweets stream using AWS EC2 and API Twiteer v2
2. Sent the tweets stream to an S3 Bucket using AWS Kinesis Firehose.
3. Perform sentiment analized of the new tweets using a python program in AWS Lambda
4. Sent the analized tweets to an OpenSearch Cluster.
5. Show the results in a Opensearch Dashboard.

Tools: 1- Python / 2- AWS Kinesis / 3- AWS Lambda / 4- Opensearch

Once the data is cleaned and standarized, product description text is tokenized and lemmanized. Then token frequency in the dataset is calculated and top 20 tokens are selected to be analized. Correlation between tokens is also estimated to find correlation sales and perform a future basket analysis.

<img
  src="/Images/diagram2.JPG"
  alt="AWS Pipeline Diagram"
  title="AWS Pipeline Diagram"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
  
  
In order to find the product features that lead costumer to choose a product, it is necessary to calculate correlation between the 20 main tokens and the quantity of sales.
  
  
  <img
  src="/Images/opensearch.JPG"
  alt="Sentiment Analysis Dashboard"
  title="Sentiment Analysis Dashboard"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
