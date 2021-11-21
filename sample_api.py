import os, sys, urllib.request, json

##defining url to use for api
movie = ""
for i in range(len(sys.argv)):
    try:
        sys.argv[i+1]
    except IndexError:
        break        
    movie = movie + "+" +  sys.argv[i+1]
movie = movie[1 : ]

url = "http://www.omdbapi.com/"
api_token = os.getenv('TOKEN')
api_url = url + "?t=" + movie + "&apikey=" + api_token
api_url = api_url.lower()

##getting content in json
json_response = urllib.request.urlopen(api_url)
content =  json_response.read().decode(json_response.headers.get_content_charset())

content_array = json.loads(content)
try:
    print("Movie Title:" + content_array["Title"])
except KeyError:
    print("There is no such movie") 
    quit()
    
for i in content_array["Ratings"]:
    print (i["Source"] + ":" + i["Value"])