#This project is for URL shorten
import requests

#account credentials
username = "o_6oueteup2l"
password = "vijayynot108@gmail.com"

# the URL you want to shorten
url = input("Enter the URl to shorten:")

# get the access token
def get_access_token(user,passwd):   
    auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(user, passwd))
    if auth_res.status_code == 200:
        # if response is OK, get the access token
        access_token = auth_res.content.decode()
        print("[👌] Got access token:", access_token)
        return access_token
    else:
        print("[🥵] Cannot get access token, exiting...")
        pass
access_token = get_access_token(username,password)
# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
def Get_group_id(head):
    groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=head)
    if groups_res.status_code == 200:
        # if response is OK, get the GUID
        groups_data = groups_res.json()['groups'][0]
        guid = groups_data['guid']
        print("[👌] Yes you got your group is:",guid)
        return guid
    else:
        print("[🥵] Cannot get GUID, exiting...")

guid = Get_group_id(headers)        


# make the POST request to get shortened URL for `url`
def shorten_url(url_one,guid_one):
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid_one, "long_url": url_one}, headers=headers)
    if shorten_res.status_code == 200:
        # if response is OK, get the shortened URL
        link = shorten_res.json().get("link")
        return link

 
link= shorten_url(url,guid)
print("Shortened URL:", link)