# Project-Sentiment-Analysis---Git

Tokenization analysis in Polish Stores Chain

The goal of this project is discover the key features in the description od the solds products by a Polish Stores Chain (Zabka) that lead customer to choose a product over the rest. For this purpuse, we analyzed data of millions of transactions (+ 2 GB) in all stores over the past 6 months. Data is stored in a Snowflake Warehouse. For our purpouse we are working with data of beer category

Objectives and tasks:

1. Clean and standarize Dataset
2. Tokenization of product descrption text.
3. Lemmanization of tokens
4. Calculate correlation among main tokens.
5. Calculate correlation between main tokens and quantity sales.

Software: 1- Python / 2- Power BI

Once the data is cleaned and standarized, product description text is tokenized and lemmanized. Then token frequency in the dataset is calculated and top 20 tokens are selected to be analized. Correlation between tokens is also estimated to find correlation sales and perform a future basket analysis.

<img
  src="/Images/diagram2.JPG"
  alt="Matrix Correlation"
  title="Matrix Correlation"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
  
  
In order to find the product features that lead costumer to choose a product, it is necessary to calculate correlation between the 20 main tokens and the quantity of sales.
  
  
  <img
  src="/Images/opensearch.JPG"
  alt="Correlation Sales Beer"
  title="Correlation Sales Beern"
  style="display: inline-block; margin: 0 auto; max-width: 150px">
