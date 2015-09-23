import identify_keywords as identify
import spotify_keyword as spotify
from clarifai.client import ClarifaiApi
import scraper
import indicoio
from os import environ
import requests

def getTagsFromImages(images):
    clarifai_api = ClarifaiApi() # assumes environment variables are set.
    ans = []
    if len(images) == 0:
      y = {"results": []}
    else:
      y = clarifai_api.tag_image_urls(images)
    ans = {}
    for x in y["results"]:
        for i in range(len(x["result"]["tag"]["classes"])):
            ans[x["result"]["tag"]["classes"][i]] = x["result"]["tag"]["probs"][i]/3
    return ans

#  def chooseSong(text, images):
def chooseSong(text):
    print "Selecting Song"
    # print "Converting to text"
    # text = html2text.html2text(text);
    # print text
    print "Finding Keywords:"
    keywords = identify.identify_keywords(text)
    for keyword in keywords.iteritems():
      print "{}: {}".format(keyword[0], keyword[1])
#     answers = getTagsFromImages(images)
#     for key in answers:
#         if (key in keywords):
#             keywords[key] += answers[key]
#         else:
# 	          keywords[key] = answers[key]
    wordlist = sorted(keywords.keys(), key = lambda x : -keywords[x])
    wordlist = identify.filter_stopwords(wordlist)
    wordlist = wordlist[:10]
    print "Top 10 words, filtered out stopwords"
    for word in wordlist:
      print word
#   print "Finding relevant songs"
    songs = spotify.full_process(wordlist)
    print songs
    # print "Finding lyrics"
    # song = scraper.computeSong(songs, keywords)
    song = songs[0]
    print "Final Song:"
    print song[0] + " by " +  song[1]
  #   stuff = requests.get("http://api.musixmatch.com/ws/1.1/track.search?apikey=" + environ.get("MUSIX_API_KEY") + "&q_track=" + song[0] + "&q_artist=" + song[1])
  #   stuff = stuff.json()
  #   stuff = stuff["message"]["body"]["track_list"][0]["track"]["track_spotify_id"]
  #   print stuff
  #   return stuff
    return song[3]

