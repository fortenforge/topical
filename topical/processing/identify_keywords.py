import re
import indicoio
import os

stopwords = set()
STOPWORDS_FILE = os.path.join('processing', 'stopwords.txt')
NUM_RESULTS    = 10

def filter_stopwords(word_list):
  global stopwords
  if len(stopwords) == 0:
    with open(STOPWORDS_FILE, 'r') as f:
      for word in f:
        stopwords.add(word.strip())

  return filter(lambda x: x not in stopwords, word_list)

def create_word_list(text):
  return re.split("\s+", text)

def identify_keywords(text):
  text = text.encode("ascii", "ignore")
  print len(text)
  x = indicoio.text_tags(text, threshold = 0.01, top_n = NUM_RESULTS)
  y = indicoio.keywords(text, threshold = 0.01, top_n = NUM_RESULTS)
  x.update(y)
  return x

if __name__ == '__main__':
  print identify_keywords(GETTY)
  print identify_keywords(PANGR)
  print identify_keywords(SPEEC)
  print identify_keywords(VOXDO)
