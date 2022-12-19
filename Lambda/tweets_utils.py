"""
tweet_utils.py* - This module contain the next functions:
  - translate_tweet: Necesaria pues el método de clasificación usado funciona con
    textos en inglés.
  - sentiment_score: En función de la calificación obtenida con el analizador del
    módulo de TextBlob, se encuentra la polaridad del tweet.
  - word_polarity: Encuentra la palabra que más represente la polaridad. Necesaria
    para crear la nube de palabras en el tablero de OpenSearch.
  - analize_tweet:  Invoca las funciones anteriores, y crea el diccionario para crear
    el json con el formato adecuado para enviar a OpenSearch.
"""

from textblob import TextBlob # Library for text processing

comillas = '"'

def translate_tweet(tweet):   # Translate tweets from spanish to english
  return str(TextBlob(tweet).translate(from_lang = 'es', to='en'))

def sentiment_score(polarity_scores): # Return the polarity with the highest score
    c = polarity_scores['pos']
    b = polarity_scores['neg']
    a = polarity_scores['neu']
    if (a>b) and (a>c):
        return 1  # Positive
    elif (b>a) and (b>c):
        return -1 # Negative
    else:
        return 0  # Neutral

def word_polarity(tweet): # Return the most positive/negative/neutral word
  pos_words = {}
  neu_words = {}
  neg_words = {}
  words = tweet.split(" ")
  for word in words:
    analysis = TextBlob(word)
    sentiment_polarity = analysis.polarity
    if sentiment_polarity < 0.5:
        #print('negative')
        neg_words[word] = abs(sentiment_polarity)
    elif sentiment_polarity == 0:
        #print('neutral')
        neu_words[word] = sentiment_polarity
    else:
        #print('postive')
        pos_words[word] = sentiment_polarity

  max_value = 0
  max_word = ''
  for dic in [neg_words,neu_words,pos_words]:
    if len(dic):
      values = dic.values()
      key_list = list(dic.keys())

      max_ = max(values)
      if max_ > max_value:
        max_word = key_list[list(values).index(max_)]
        max_value = max_

  if max_word != '':
    return max_word
  else:
    return ' '

def analize_tweet(tweet, location, location2): # Return tweets analysis in JSON format
    tweet = translate_tweet(tweet)
    analysis = TextBlob(tweet)
    sentiment_polarity = analysis.polarity
    max_word = word_polarity(tweet)
    
    if sentiment_polarity < 0.5:
        doc = """{"tweet":""" + comillas + tweet + comillas + """, "polarity":"negative", "location": """ + comillas + location + comillas + ""","max_word": """ + comillas + max_word + comillas + ""","location2": """ + location2 + "}"
        return doc
    elif sentiment_polarity == 0:
        #print('neutral')
        doc = """{"tweet":""" + comillas + tweet + comillas + """, "polarity":"neutral", "location": """ + comillas + location + comillas + ""","max_word": """ + comillas + max_word + comillas + ""","location2": """ + location2 + "}"
        return doc
    else:
        doc = """{"tweet":""" + comillas + tweet + comillas + """, "polarity":"positive", "location": """ + comillas + location + comillas + ""","max_word": """ + comillas + max_word + comillas + ""","location2": """ + location2 + "}"
        return doc