import identify_keywords as identify
import spotify_keyword as spotify
from clarifai.client import ClarifaiApi
import scraper
import indicoio
from os import environ
from lxml import html
import requests
import html2text

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
    print "HELLO NG WORLD"
    text = html2text.html2text(text);
    keywords = identify.identify_keywords(text)
    print keywords
    keywords = identify.identify_keywords(text)
#     answers = getTagsFromImages(images)
#     for key in answers:
#         if (key in keywords):
#             keywords[key] += answers[key]
#         else:
# 	          keywords[key] = answers[key]
    wordlist = sorted(keywords.keys(), key = lambda x : -keywords[x])
    wordlist = wordlist[:10]
    songs = spotify.full_process(wordlist)
    song = scraper.computeSong(songs, keywords)
    print song[0] + " by " +  song[1]
  #   stuff = requests.get("http://api.musixmatch.com/ws/1.1/track.search?apikey=" + environ.get("MUSIX_API_KEY") + "&q_track=" + song[0] + "&q_artist=" + song[1])
  #   stuff = stuff.json()
  #   stuff = stuff["message"]["body"]["track_list"][0]["track"]["track_spotify_id"]
  #   print stuff
  #   return stuff
    return song[3]

# print chooseSong("Two days after asserting that President Barack Obama was a foreign-born Muslim, a guy who asked Donald Trump a provocative question at a New Hampshire rally is now the front-runner in the Republican race for President, according to a new poll. The poll, which was conducted by the University of Minnesota's Opinion Research Institute, shows Muslim Question Guy leading the G.O.P field with thirty-four per cent as opposed to nineteen percent for Trump.")
