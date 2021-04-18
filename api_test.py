import requests
import os

#"https://api.steampowered.com/<interface>/<method>/v<version>/"
steamAPIResponse = requests.get("https://api.steampowered.com/")

print(steamAPIResponse.status_code)







def search_test():
  key = os.environ.get("Youtube_API_KEY")
  pyoutubeRespone = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=surfing&key="+key)
  print(youtubeRespone.json())
  print("Hej")
  print(youtubeRespone)

def search_top_video(channel):
  key = os.environ.get("Youtube_API_KEY")
  youtubeRespone = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId="+channel+"&maxResults=10&order=viewCount&key="+key)
  print(youtubeRespone.json())


search_top_video('Linus Tech Tips')

'''
  requests.get('https://youtube.googleapis.com/youtube/v3/search?channelId=Linus%20Tech%20Tips%20&key=[YOUR_API_KEY]' \
  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
  --header 'Accept: application/json' \
  --compressed

GET https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=surfing&key=[YOUR_API_KEY] HTTP/1.1

Authorization: Bearer [YOUR_ACCESS_TOKEN]
Accept: application/json

os.environ.get("Youtube_API_KEY")

GET https://youtube.googleapis.com/youtube/v3/search?part=snippet&relatedToVideoId=Ks-_Mh1QhMc&type=video&key=[YOUR_API_KEY] HTTP/1.1

Authorization: Bearer [YOUR_ACCESS_TOKEN]
Accept: application/json

'''