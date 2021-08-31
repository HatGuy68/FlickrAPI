import requests, json

def getUserId(username):
    url = "https://www.flickr.com/services/rest/?method=flickr.people.findByUsername&format=json&nojsoncallback=1&username="+username+"&api_key="+key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.content)["user"]["id"]


def getPopularPhotos(user_id, username):
    url = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&user_id="+user_id+"&format=json&nojsoncallback=1&oauth_consumer_key="+key+"&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1630398594&oauth_nonce=EnrsmLENPZT&oauth_version=1.0&oauth_callback=example.com&oauth_signature=V9Tgoq0b1L7wCCcOZl5LkfEa8lM%3D"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print('Data of the user', username)
    print(response.text)
    o = input('\nWould you like to save data (Y/n): ')
    if o == "Y" or o == "y":
        with open(username+'_data.json', 'w') as f:
            json.dump(response.json(), f)

def main():
    print('Welcome to flickr API: ')
    global key
    key = 'e786b4bc97884e12c85bd2da66959291'
    username = input('Enter a username to get their data: ')
    user_id = getUserId(username)
    getPopularPhotos(user_id, username)

if __name__ == "__main__":
    main()
    # Sample Username: Andysea1