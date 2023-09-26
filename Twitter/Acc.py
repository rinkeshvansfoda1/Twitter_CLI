# It is used to fetch the Twitter User Information

import json
import requests
from bs4 import BeautifulSoup

acc=input("Enter the User Id of Twitter Account to get Information: ")

cookies = {
    '_ga': 'GA1.2.265084132.1695490472',
    '_gid': 'GA1.2.1945644660.1695490472',
    'guest_id': 'v1%3A169549047452028732',
    'guest_id_marketing': 'v1%3A169549047452028732',
    'guest_id_ads': 'v1%3A169549047452028732',
    'gt': '1705638407622582754',
    'external_referer': '8e8t2xd8A2w%3D|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D',
    '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKvlMMOKAToMY3NyZl9p%250AZCIlYTViZDFiNDVjYjM1ZjU5ODNkMWEzNzZlOWRkZTkwNTU6B2lkIiUxOWQ4%250AM2Y2ODdmNjUxYTY5Zjg4MTQ1YmNkNjZhOTYyMA%253D%253D--217de3f2705b4e30cbac108164125b334558a4b6',
    'kdt': 'talcdVLN2FFj2awaOMUp1jJNBslqcHmjrDVzgdZh',
    'auth_token': '1292cec1502a98c3dbf34397a71cb647c3ab6ee4',
    'ct0': '6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d',
    'lang': 'en',
    'twid': 'u%3D1705642986431008768',
    'personalization_id': '"v1_r8K4lf+JyDkUpImhGRcJKQ=="',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.2.265084132.1695490472; _gid=GA1.2.1945644660.1695490472; guest_id=v1%3A169549047452028732; guest_id_marketing=v1%3A169549047452028732; guest_id_ads=v1%3A169549047452028732; gt=1705638407622582754; external_referer=8e8t2xd8A2w%3D|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKvlMMOKAToMY3NyZl9p%250AZCIlYTViZDFiNDVjYjM1ZjU5ODNkMWEzNzZlOWRkZTkwNTU6B2lkIiUxOWQ4%250AM2Y2ODdmNjUxYTY5Zjg4MTQ1YmNkNjZhOTYyMA%253D%253D--217de3f2705b4e30cbac108164125b334558a4b6; kdt=talcdVLN2FFj2awaOMUp1jJNBslqcHmjrDVzgdZh; auth_token=1292cec1502a98c3dbf34397a71cb647c3ab6ee4; ct0=6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d; lang=en; twid=u%3D1705642986431008768; personalization_id="v1_r8K4lf+JyDkUpImhGRcJKQ=="',
    'referer': 'https://twitter.com/narendramodi',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-client-transaction-id': '5nltyWMR1cp05VshJDCFxxUPlqHJ4YHCSqzik0J0ybvf3N/l9VG3vaA1clnpU4l61GsiWeYo1vnW+nlOwUA+Dmb0Y8ZZ5w',
    'x-client-uuid': '8ff302ef-2ff9-48f3-8a68-66a831357702',
    'x-csrf-token': '6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}

params = {
    'variables': '{"screen_name":"narendramodi","withSafetyModeUserFields":true}',
    'features': '{"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":true,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    'fieldToggles': '{"withAuxiliaryUserLabels":false}',
}

response = requests.get(
    'https://twitter.com/i/api/graphql/G3KGOASz96M-Qu0nwmGXNg/UserByScreenName',
    params=params,
    cookies=cookies,
    headers=headers,
)



# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://twitter.com/i/api/graphql/7mjxD3-C6BxitPMVQ6w0-Q/UserByScreenName?variables=%7B%22screen_name%22%3A%22ani%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D', headers=headers)


# to change the account then change the referer twitter id  and also in params under screen_name of same twitter referer account

if response.status_code==200:
    print("Connection is OK")
elif response.status_code==301:
    print("Connection is Moved Permanently")
elif response.status_code==403:
    print("Connection is Forbidden")
else:
    print("Connection is Not Found")


soup=BeautifulSoup(response.content,'html.parser')

import os
current_dir=os.getcwd()

# create the file
file=open(current_dir+'\\json\\account_data.json','w',encoding='utf-8')
file.write(str(soup))
file.close()


# read the file
with open(current_dir+'\\json\\account_data.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)

obj=read_context['data']['user']['result']['legacy']
print("Name:",obj['name'])
print("User ID:",read_context['data']['user']['result']['rest_id'])
print("Account Created at:",obj['created_at'])
print("Description:",obj['description'])
print("Account Image:",obj['profile_image_url_https'])
print("Location:",obj['location'])
print("Follower Count:",obj['followers_count'])
print("Tweet Posted or Media Count:",obj['media_count'])

obj1=read_context['data']['user']['result']['legacy']['entities']
print("Other Platform link: ")
for i in obj1:
    aa=(obj1[i]['urls'])
    for j in aa:
        print(j['expanded_url'])
        # if j['expanded_url']:
        #     print(j['expanded_url'])
        # else:
        #     print(j['expanded_url'],"Other Platform link are not available")
        # print(j['expanded_url'])
        # print("Not Other Platform link available")
print()

