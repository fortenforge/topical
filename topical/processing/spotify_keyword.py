import requests

def full_process(keywords):
  result = []
  for i in range(0, len(keywords)):
    temp = []
    temp.append(keywords[i])
    tempo = process(temp)
    for k in range(0, len(tempo)):
      result.append(tempo[k])
  for i in range(0, len(keywords)):
    for j in range(i + 1, len(keywords)):
      temp = []
      temp.append(keywords[i])
      temp.append(keywords[j])
      tempo = process(temp)
      for k in range(0, len(tempo)):
        result.append(tempo[k])
  result = sorted(result, key = lambda x: -x[2])
  return result[:10]

def process(keywords):
  query = "";
  for i in range(0, len(keywords)):
    query = query + keywords[i]
    if (i != len(keywords) - 1):
      query = query + " "
  result = requests.get("https://api.spotify.com/v1/search?type=track&limit=2&q=" + query)
  result = result.json()
  dictionary = []
  for i in range(0, len(result['tracks']['items'])):
    dictionary.append([
      result['tracks']['items'][i]['name'],
      result['tracks']['items'][i]['artists'][0]['name'],
      result['tracks']['items'][i]['popularity'],
      result['tracks']['items'][i]['id']
    ])
  return dictionary

