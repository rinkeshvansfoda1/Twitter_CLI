import requests
from bs4 import BeautifulSoup
import json

hashh=input("Enter the hashtag you want to search: ")
# below line will only contain  live(latest), default(top), image(photos), video(Videos) method type
typee=input("Enter the tweet search mode: ")

twett=int(input("Enter the number of tweets you want: "))

# teetete='https://twitter.com/search?q=%23'+hashh+'&src=typeahead_click&f='+typee+''
# print(teetete)

headers = {
    'authority': 'twitter.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'x-twitter-client-language': 'en',
    'x-csrf-token': 'ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    # 'referer': 'https://twitter.com/search?q=%23UkraineWar&src=typeahead_click&f=live',
    'referer': 'https://twitter.com/search?q=%23'+hashh+'&src=typeahead_click&f='+typee+'',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; lang=en',
}

params = (
    ('include_profile_interstitial_type', '1'),
    ('include_blocking', '1'),
    ('include_blocked_by', '1'),
    ('include_followed_by', '1'),
    ('include_want_retweets', '1'),
    ('include_mute_edge', '1'),
    ('include_can_dm', '1'),
    ('include_can_media_tag', '1'),
    ('include_ext_has_nft_avatar', '1'),
    ('skip_status', '1'),
    ('cards_platform', 'Web-12'),
    ('include_cards', '1'),
    ('include_ext_alt_text', 'true'),
    ('include_quote_count', 'true'),
    ('include_reply_count', '1'),
    ('tweet_mode', 'extended'),
    ('include_entities', 'true'),
    ('include_user_entities', 'true'),
    ('include_ext_media_color', 'true'),
    ('include_ext_media_availability', 'true'),
    ('include_ext_sensitive_media_warning', 'true'),
    ('include_ext_trusted_friends_metadata', 'true'),
    ('send_error_codes', 'true'),
    ('simple_quoted_tweet', 'true'),
    ('q', f'#{hashh}'),
    # to get live tweet then,
    # ('tweet_search_mode','live'),
    ('tweet_search_mode', f'{typee}'),
    ('count', f'{twett}'),
    ('query_source', 'typeahead_click'),
    ('pc', '1'),
    ('spelling_corrections', '1'),
    ('ext', 'mediaStats,highlightedLabel,hasNftAvatar,replyvotingDownvotePerspective,voiceInfo,enrichments,superFollowMetadata'),
)

response = requests.get('https://twitter.com/i/api/2/search/adaptive.json', headers=headers, params=params)

# this upper line will fetch data from referer in headers, rather it will 

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&include_ext_sensitive_media_warning=true&include_ext_trusted_friends_metadata=true&send_error_codes=true&simple_quoted_tweet=true&q=%23'+hashh+'&tweet_search_mode='+typee+'&count=20&query_source=typeahead_click&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CreplyvotingDownvotePerspective%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata', headers=headers)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

import os
current_dir=os.getcwd()

file=open(current_dir+'\\json\\hashtag.json','w',encoding='utf-8')
file.write(str(soup))
file.close()

with open('C:\\Users\\KPRRS\\hash.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)

# print(read_context)

# working for default, live, and image only
print("1. tweet_search_mode==live")
print("2. tweet_search_mode==default")
print("3. tweet_search_mode==image")
print()
objj=read_context['globalObjects']['tweets']
# print(objj)
for i in objj:
    print(objj[i]['created_at'])
    print(objj[i]['full_text'])
print()