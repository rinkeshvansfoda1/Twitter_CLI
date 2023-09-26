import requests
from bs4 import BeautifulSoup
import json

raw_query = input("Enter the Hashtag: ")
# below line will only contain  Latest, Top, People, Media, Lists are method type of search mode
typee=input("Enter the tweet search mode: ")

twett=int(input("Enter the number of tweets you want: "))

# teetete='https://twitter.com/search?q=%23'+hashh+'&src=typeahead_click&f='+typee+''
# print(teetete)



cookies = {
    '_ga': 'GA1.2.265084132.1695490472',
    '_gid': 'GA1.2.1945644660.1695490472',
    'guest_id': 'v1%3A169549047452028732',
    'guest_id_marketing': 'v1%3A169549047452028732',
    'guest_id_ads': 'v1%3A169549047452028732',
    'external_referer': '8e8t2xd8A2w%3D|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D',
    'auth_token': '1292cec1502a98c3dbf34397a71cb647c3ab6ee4',
    'kdt': 'talcdVLN2FFj2awaOMUp1jJNBslqcHmjrDVzgdZh',
    'ct0': '6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d',
    'twid': 'u%3D1705642986431008768',
    'lang': 'en',
    'personalization_id': '"v1_yuHM+pKUbt3thJalzoevzA=="',
}

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # 'cookie': '_ga=GA1.2.265084132.1695490472; _gid=GA1.2.1945644660.1695490472; guest_id=v1%3A169549047452028732; guest_id_marketing=v1%3A169549047452028732; guest_id_ads=v1%3A169549047452028732; external_referer=8e8t2xd8A2w%3D|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D; auth_token=1292cec1502a98c3dbf34397a71cb647c3ab6ee4; kdt=talcdVLN2FFj2awaOMUp1jJNBslqcHmjrDVzgdZh; ct0=6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d; twid=u%3D1705642986431008768; lang=en; personalization_id="v1_yuHM+pKUbt3thJalzoevzA=="',
    'referer': "https://twitter.com/search?q=%23sachintendulkar&src=typeahead_click&f=top",
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-client-transaction-id': 'lBtWGDQAcsGa6qi14ohtwXToPQG2P2YLQTA5jsr4Yh6zhv7F/KjL7P7/V5hMcEJynrCWVZSVA4W+Anmp5eGDbzgmArmrlQ',
    'x-csrf-token': '6f41d64e2573f15babd87cababf97593b12dd07d38e3f89cd1a8daee6394a4423afe3220a04d20a62d73860c8ea6d991221e0644f6e02b8913d31455b153bf014ebe21e8d1e6d7683b304ad5a5510e4d',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}



# Create the 'variables' and 'features' JSON-like strings
variables = f'{{"rawQuery": "#{raw_query}","count": "{twett}","querySource": "typeahead_click","product": "{typee}"}}'

params = {
    'variables': '{"rawQuery":"#sachintendulkar","count":20,"querySource":"typeahead_click","product":"Top"}',
    'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
}

# Update the 'variables' keys in the params dictionary
params['variables'] = variables



response = requests.get(
    'https://twitter.com/i/api/graphql/tOUz374Df84NaVVr3M1p6g/SearchTimeline',
    params=params,
    cookies=cookies,
    headers=headers,
)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

import os
current_dir=os.getcwd()

file=open('hashtag.json','w',encoding='utf-8')
file.write(str(soup))
file.close()

with open('hashtag.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)

# print(read_context)

# working for default, live, and image only
print("Methods are:\nLatest, Top, People, Media, Lists")

objj=read_context.get('data',{}).get('search_by_raw_query').get('search_timeline').get('timeline').get('instructions')[0].get('entries')
# print(objj[0]['content']['itemContent'])

for i in range(len(objj)):
    data=objj[i]['content'].get('itemContent')
    if data:
        print(i,data.get('tweet_results').get('result').get('legacy').get('created_at'))
        print(i,data.get('tweet_results').get('result').get('legacy').get('full_text'))
    # else:
    #     print(i,"No Tweets")