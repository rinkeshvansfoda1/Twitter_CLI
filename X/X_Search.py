import requests
from bs4 import BeautifulSoup
import json

acc=input("Enter the account name you want to search: ")

twettacc=int(input("Enter the number of account(row) you want: "))

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
variables = f'{{"rawQuery": "#{acc}","count": "{twettacc}","querySource": "typeahead_click","product": "People"}}'

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
# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=narendramodi&result_filter=user&count=20&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata', headers=headers)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

file=open('search.json','w',encoding='utf-8')
file.write(str(soup))
file.close()

with open('search.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)

objj=read_context.get('data',{}).get('search_by_raw_query').get('search_timeline').get('timeline').get('instructions')[1].get('entries')

for i in range(len(objj)):
    data=objj[i]['content'].get('itemContent')
    if data:
        print(i)
        if (len(data.get('user_results').get('result').get('legacy').get('name'))!=0):
            print(data.get('user_results').get('result').get('legacy').get('name'))
        else:
            print("No Name")
        if (len(data.get('user_results').get('result').get('legacy').get('created_at'))!=0):
            print(data.get('user_results').get('result').get('legacy').get('created_at'))
        else:
            print("No Created Time")
        if (len(data.get('user_results').get('result').get('legacy').get('description'))!=0):
            print(data.get('user_results').get('result').get('legacy').get('description'))
        else:
            print("No Description")
        if (len(str(data.get('user_results').get('result').get('legacy').get('favourites_count')))!=0):
            print(data.get('user_results').get('result').get('legacy').get('favourites_count'))
        else:
            print("No Favourite Count")
        if (len(str(data.get('user_results').get('result').get('legacy').get('followers_count')))!=0):
            print(data.get('user_results').get('result').get('legacy').get('followers_count'))
        else:
            print("No Followers")
        if (len(str(data.get('user_results').get('result').get('legacy').get('normal_followers_count')))!=0):
            print(data.get('user_results').get('result').get('legacy').get('normal_followers_count'))
        else:
            print("No Followers")
        if (len(str(data.get('user_results').get('result').get('legacy').get('friends_count')))!=0):
            print(data.get('user_results').get('result').get('legacy').get('friends_count'))
        else:
            print("No Friend Count")
        if (len(data.get('user_results').get('result').get('legacy').get('location'))!=0):
            print(data.get('user_results').get('result').get('legacy').get('location'))
        else:
            print("No Location")
        if (not data.get('user_results').get('result').get('legacy').get('profile_banner_url')):
            print("No Profile Banner")
        else:
            print(data.get('user_results').get('result').get('legacy').get('profile_banner_url'))

        if (not data.get('user_results').get('result').get('legacy').get('profile_image_url_https')):
            print("No Profile Image")
        else:
            print(data.get('user_results').get('result').get('legacy').get('profile_image_url_https'))
