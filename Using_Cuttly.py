import json
import requests
from requests import status_codes
 
#get Api_key from user by login in cuttly
api_key=input("Enter api_key for cuttly: ")

url = input("Enter the Url to shorten: ")
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

#to make request
def get_url(api):
    data = requests.get(api).json()["url"]
    if data["status"] == 7:
        shorten_url = data["shortLink"]
        return shorten_url
    else:
        print("[🥵]SOMETHING HAPPEN ")

short_url= get_url(api_url)
print("[👌] The Shorten URL :",short_url)











