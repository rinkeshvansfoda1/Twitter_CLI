# from ast import parse
# from asyncore import read
# from base64 import decode
# from encodings import utf_8
# from pprint import PrettyPrinter
# from random import random
# from textwrap import indent
# from typing import IO, final
# import requests
# from bs4 import BeautifulSoup
# import requests


# headers = {
#     'authority': 'twitter.com',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
#     'x-twitter-client-language': 'en',
#     'x-csrf-token': 'ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997',
#     'sec-ch-ua-mobile': '?0',
#     'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#     'content-type': 'application/json',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'x-twitter-auth-type': 'OAuth2Session',
#     'x-twitter-active-user': 'yes',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://twitter.com/ANI',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE2FyjvSFlFJR45yIlYF%2Bw%3D%3D; _sl=1; att=1-rDMoiFqRmEVyAThTbPOrnt0blYMf2kreo5zx1kkQ; gt=1501075314654744576; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210',
# }


# # number of tweet/items user want
# # sas=int(input("enter: "))
# sas=int(20)

# params = (
#     ('variables', '{"userId":"355989081","count":'+f'{sas}'+',"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'),
# )

# response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets?variables=%7B%22userId%22%3A%22355989081%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)

# soup=BeautifulSoup(response.content,'html.parser')

# to make json file
# file=open('teett1.json','w',encoding='utf-8')
# file.write(str(soup))
# file.close()


# to read json file
# import json
# with open('C:\\Users\\KPRRS\\teett1.json',encoding='utf-8') as source_json:
#     read_context=json.load(source_json)



# import json
# with open('teett1.json','r',encoding='utf-8') as f:
#     data=json.load(f)
# print(data.keys())
# print(data['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][3]['item']['itemContent']['tweet_results']['result']['legacy']['created_at'])


# a=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
# b=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][1]['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
# print(a)
# print(b)

# j=sas
# for i in range(j):
#     try:
        # a=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][i]['item']['itemContent']['tweet_results']['result']['legacy']['created_at'] or a=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
        # aa=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][i]['item']['itemContent']['tweet_results']['result']['legacy']['full_text'] or a=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
#     except:
#         print("hmmm")
#     finally:
#         print(a)
#         print(aa)



# j=sas
# k=0 or 1
# for i in range(j):
    # try:
    #     if k==0 and k==1:
    #         a=(read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][k]['item']['itemContent']['tweet_results']['result']['legacy']['created_at'])
    #         b=(read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][k]['item']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            # print(a)
            # print(b)
    # except:
    #     print(a)
    #     print(b)
        # b=(read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][k]['item']['itemContent']['tweet_results']['result']['legacy']['full_text'])

    # try:
    #     print(read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
    # except:
    #     print(read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            

# aa=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][0]['item']['itemContent']['tweet_results']['result']['legacy']['created_at']
# bb=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][6]['item']['itemContent']['tweet_results']['result']['legacy']['full_text']
# print(bb)








# new start

# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# dict={}
# for i in obj1:
#     if (i.get('type')=='TimelineAddEntries'):
        # i['entries']
        # time
        # print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])

        # media
        # print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['media_url_https'])
        # print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['type'])
        # print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['url'])

        # text
        # print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])


# ~!~!~!~!~!
# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# k=1
# for i in obj1:
#     print(k)
#     if (i.get('type')=='TimelineAddEntries'):
#         # print(i['entries']['content'])
#         a=i['entries']
#         for j in a:
#             # working
#             # if j['content'].get('entryType')=="TimelineTimelineItem":
#             #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
#             #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
#             # print()
            
#             # temp (testing)
#             if j['content'].get('entryType')=="TimelineTimelineItem":
#                 print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
#                 print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
#                 try:
#                     abab=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]
#                     if abab:
#                     # media url
#                         print(abab['media_url_https'])
#                     # media type
#                         # print(j['type'])
#                 except:
#                     if j['content'].get('entryType')=="TimelineTimelineModule":
#                         at=j['content']['items']
#                         for l in at:
#                             # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
#                             if l['item']['itemContent'].get('itemType')=="TimelineTweet":
#                                 mj=(l['item']['itemContent']['tweet_results']['result'])
#                                 print(mj['legacy']['created_at'])
#                                 print(mj['legacy']['full_text'])
#                                 mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities'])
#                                 try:
#                                     aa=(mj['media'])
#                                     for i in aa:
#                                         print(i['media_url_https'])
#                                         print(i['type'])
#                                 except:
#                                     print()

# with upper for loop
# for j in a:
#     if j['content'].get('entryType')=="TimelineTimelineModule":
#         at=j['content']['items']
#         for l in at:
#             # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
#             if l['item']['itemContent'].get('itemType')=="TimelineTweet":
#                 mj=(l['item']['itemContent']['tweet_results']['result'])
#                 print(mj['legacy']['created_at'])
#                 print(mj['legacy']['full_text'])
#                 mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities'])
#                 try:
#                     aa=(mj['media'])
#                     for i in aa:
#                         print(i['media_url_https'])
#                         print(i['type'])
#                 except:
#                     print()
# k=k+1        


# print("Hello")




from encodings import utf_8
from textwrap import indent
from typing import IO, final
import requests
from bs4 import BeautifulSoup

# second for testing
# headers = {
#     'authority': 'twitter.com',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
#     'x-twitter-client-language': 'en',
#     'x-csrf-token': 'ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997',
#     'sec-ch-ua-mobile': '?0',
#     'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#     'content-type': 'application/json',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'x-twitter-auth-type': 'OAuth2Session',
#     'x-twitter-active-user': 'yes',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://twitter.com/ANI',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE2FyjvSFlFJR45yIlYF%2Bw%3D%3D; _sl=1; att=1-rDMoiFqRmEVyAThTbPOrnt0blYMf2kreo5zx1kkQ; gt=1501075314654744576; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210',
# }

# number of tweet/items user want
# sas=int(input("enter: "))
# sas=int(20)

# # print(sas)

# params = (
#     ('variables', '{"userId":"355989081","count":'+f'{sas}'+',"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'),
# )

# # print(params)

# response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets?variables=%7B%22userId%22%3A%22355989081%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)


# third testing for different account, and second and this both are working properly, only the change is required that the link on referer
# import requests


# acc=input("Enter the Twitter User Id to get the tweet from the Account: ")
# sas=int(input("Enter the number of tweet you want:"))

# headers = {
#     'authority': 'twitter.com',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
#     'x-twitter-client-language': 'en',
#     'x-csrf-token': 'ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997',
#     'sec-ch-ua-mobile': '?0',
#     'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#     'content-type': 'application/json',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'x-twitter-auth-type': 'OAuth2Session',
#     'x-twitter-active-user': 'yes',
#     'sec-ch-ua-platform': '"Windows"',
#     'accept': '*/*',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     # 'referer': f'https://twitter.com/{acc}',
#     'referer': 'https://twitter.com/ANI',
#     'accept-language': 'en-US,en;q=0.9',
#     'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; lang=en',
# }

# params = (
#     ('variables', '{"userId":"711760467383877632","count":'+f'{sas}'+',"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'),
# )

# response = requests.get('https://twitter.com/i/api/graphql/CDDPst9A-AHg6Q0k9-wo7w/UserTweets', headers=headers, params=params)

# # Note: original query string below. It seems impossible to parse and
# # reproduce query strings 100% accurately so the one below is given
# # in case the reproduced version is not "correct".
# #response = requests.get('https://twitter.com/i/api/graphql/CDDPst9A-AHg6Q0k9-wo7w/UserTweets?variables=%7B%22userId%22%3A%22711760467383877632%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)

# soup=BeautifulSoup(response.content,'html.parser')

# # to make json file
# file=open('teettt1.json','w',encoding='utf-8')
# file.write(str(soup))
# file.close()


# # to read json file
# import json
# with open('C:\\Users\\KPRRS\\teettt1.json',encoding='utf-8') as source_json:
#     read_context=json.load(source_json)


# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# for i in obj1:
#     if (i.get('type')=='TimelineAddEntries'):
#         # print(i['entries']['content'])
#         a=i['entries']
#         for j in a:
#             if j['content'].get('entryType')=="TimelineTimelineItem":
#                 print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
#                 print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
#                 try:
#                     try:
#                         abab=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media']
#                         for i in abab:
#                             print(i['type'])
#                             print(i['media_url_https'])
#                     except:
#                         abca=j['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values']
#                         for o in abca:
#                             if(o.get('key')=='photo_image_full_size_large'):
#                                 print(o['value']['type'])
#                                 print(o['value']['image_value']['url'])
#                 except:
#                     if j['content'].get('entryType')=="TimelineTimelineModule":
#                         at=j['content']['items']
#                         for l in at:
#                             # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
#                             if l['item']['itemContent'].get('itemType')=="TimelineTweet":
#                                 # mj=(l['item']['itemContent']['tweet_results']['result'])
#                                 print(mj['item']['itemContent']['tweet_results']['result']['legacy']['created_at'])
#                                 print(mj['item']['itemContent']['tweet_results']['result']['legacy']['full_text'])
#                                 try:
#                                     mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities']['media'])
#                                     # aa=(mj['media'])
#                                     for i in mj:
#                                         print(i['media_url_https'])
#                                         print(i['type'])
#                                 except:
#                                     print()




import requests

acc=input("Enter the Account Name: ")
acc_id=input("Enter the Account id:")
sas=int(input("Enter the number of tweets you want: "))

headers = {
    'authority': 'twitter.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'x-twitter-client-language': 'en',
    'x-csrf-token': 'ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': f'https://twitter.com/{acc}',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; lang=en',
}

params = (
    ('variables', '{"userId":"'f'{acc_id}''","count":'+f'{sas}'+',"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'),
)

response = requests.get('https://twitter.com/i/api/graphql/CDDPst9A-AHg6Q0k9-wo7w/UserTweets', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://twitter.com/i/api/graphql/CDDPst9A-AHg6Q0k9-wo7w/UserTweets?variables=%7B%22userId%22%3A%22355989081%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)

from bs4 import BeautifulSoup

soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

# # to make json file
file=open('teettt1.json','w',encoding='utf-8')
file.write(str(soup))
file.close()


# to read json file
import json
with open('C:\\Users\\KPRRS\\teettt1.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)

obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
for i in obj1:
    if (i.get('type')=='TimelineAddEntries'):
        # print(i['entries']['content'])
        a=i['entries']
        for j in a:
            if j['content'].get('entryType')=="TimelineTimelineItem":
                print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
                print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
                try:
                    try:
                        abab=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media']
                        for i in abab:
                            print(i['type'])
                            print(i['media_url_https'])
                    except:
                        abca=j['content']['itemContent']['tweet_results']['result']['card']['legacy']['binding_values']
                        for o in abca:
                            if(o.get('key')=='photo_image_full_size_large'):
                                print(o['value']['type'])
                                print(o['value']['image_value']['url'])
                except:
                    if j['content'].get('entryType')=="TimelineTimelineModule":
                        at=j['content']['items']
                        for l in at:
                            # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
                            if l['item']['itemContent'].get('itemType')=="TimelineTweet":
                                # mj=(l['item']['itemContent']['tweet_results']['result'])
                                print(mj['item']['itemContent']['tweet_results']['result']['legacy']['created_at'])
                                print(mj['item']['itemContent']['tweet_results']['result']['legacy']['full_text'])
                                try:
                                    mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities']['media'])
                                    # aa=(mj['media'])
                                    for i in mj:
                                        print(i['media_url_https'])
                                        print(i['type'])
                                except:
                                    print()


# backup
# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# for i in obj1:
    # if (i.get('type')=='TimelineAddEntries'):
    #     # print(i['entries']['content'])
    #     a=i['entries']
    #     for j in a:
            # temp (testing) 99% working
            # if j['content'].get('entryType')=="TimelineTimelineItem":
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            #     try:
            #         abab=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media']
            #         for i in abab:
            #             print(i['type'])
            #             print(i['media_url_https'])
            #     except:
            #         if j['content'].get('entryType')=="TimelineTimelineModule":
            #             at=j['content']['items']
            #             for l in at:
            #                 # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
            #                 if l['item']['itemContent'].get('itemType')=="TimelineTweet":
            #                     # mj=(l['item']['itemContent']['tweet_results']['result'])
            #                     print(mj['item']['itemContent']['tweet_results']['result']['legacy']['created_at'])
            #                     print(mj['item']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            #                     try:
            #                         mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities']['media'])
            #                         # aa=(mj['media'])
            #                         for i in mj:
            #                             print(i['media_url_https'])
            #                             print(i['type'])
            #                     except:
            #                         print()
