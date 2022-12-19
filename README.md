# Project-Sentiment-Analysis---Git

Sentiment analysis of tweets using AWS Serverless Services
The goal of this project is developed a full data pipeline using python and AWS Services in order to analyze tweets information and show the results in an OpenSearch dashboard. An specific topic is chosen in the python script to narrowed the results. For this project, the keywords "Dina Boluarte", "Vacancia" and "Peru" were used.

Objectives and tasks:

1. Generate a tweets stream using AWS EC2 and API Twiteer v2
2. Sent the tweets stream to an S3 Bucket using AWS Kinesis Firehose.
3. Perform sentiment analized of the new tweets using a python program in AWS Lambda
4. Sent the analized tweets to an OpenSearch Cluster.
5. Show the results in a Opensearch Dashboard.

Tools: 1- Python / 2- AWS Kinesis / 3- AWS Lambda / 4- Opensearch

ETL Pipeline have been built using AWS Serverless Services: AWS Kinesis Firehose, AWS Lambda. Sentiment analysis function is deployed in AWS Lambda. This AWS Lambda function is trigger every time a new tweet is added to the S3 bucket. Moreover, as it was said, AWS Kinesis is in charge of sending the tweets documents.

<img
  src="/Images/diagram2.JPG"
  alt="AWS Pipeline Diagram"
  title="AWS Pipeline Diagram"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
  
Steps:
1. Create tweets stream in EC2.
- Create new EC2 instance. Amazon Linux.
- Load the python script to capture tweets.
- Change Kinesis Stream Name for your own stream name.
3. Configure AWS Kinesis Firehose:
- IAM Role. Configure Firehose role with permissions for writing on S3 Bucket.
- Create a new AWS Kinesis Firehose stream.
- Target stream to your S3 Bucket.
4. Configure AWS Lambda:
- IAM Role. Configure Lambda role with permissions for reading on S3 Buckes and writing on OpenSearch.
- Create a new AWS Lambda function using the previous created role. Functions are described in Lambda folder
- Set new trigger event: New S3 Bucket object.
- Create new layer to import needed libraries : TextBloob, Request
5. Configure AWS Kinesis OpenSearch:
- Create a new domain twitter-sentiment-analysis
- Create a new OpenSearch Dashboard
- In Cluster Configuration > Network > Access, set Public 


An Opensearch cluster have to be set before. For this purpose, AWS is also used. Results of analisys is presented in a OpenSearch Dashboard
  
  
  <img
  src="/Images/opensearch.JPG"
  alt="Sentiment Analysis Dashboard"
  title="Sentiment Analysis Dashboard"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
