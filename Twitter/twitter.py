# import requests
# from bs4 import BeautifulSoup

# # url='https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'
# # re=requests.get(url)
# # soup=BeautifulSoup(re.content,"html.parser")
# # # print(soup.prettify)

# # a=soup.find('h1',{'id':'firstHeading'})
# # print(a.text)

# url='https://twitter.com/ANI'
# re=requests.get(url)
# soup=BeautifulSoup(re.content,"html.parser")
# # print(soup)


# for i in soup.select('div',class_='react-root'):
#     for j in i.select('div',class_='css-1dbjc4n r-13awgt0 r-12vffkv'):
#         print(j)
    # print(i)
# a=soup.select('div',id_='reach-root')
# b=a.find('div',class_='css-1dbjc4n r-13awgt0 r-12vffkv')
# a=soup.select('div',class_='css-1dbjc4n r-13awgt0 r-12vffkv')
# print(a)



# https://twitter.com/ANI





# import urllib
# import urllib.request
# from bs4 import BeautifulSoup

# # url='https://twitter.com/ANI?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor'
# url='https://twitter.com/ANI'
# re=urllib.request.urlopen(url)
# soup=BeautifulSoup(re,"html.parser")

# print(soup.find_all('a'))




# using selenium

# from xml.etree.ElementTree import ElementTree
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# from bs4 import BeautifulSoup

# url='https://twitter.com/ANI'
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)

# soup=BeautifulSoup(driver.page_source,'lxml')
# print(soup)


# main_name=soup.find("div",{'id':"react-root"})
# con=main_name.find('div',class_="css-1dbjc4n r-13awgt0 r-12vffkv")
# second=con.find_next_sibling('div',{'class':"css-1dbjc4n r-13awgt0 r-12vffkv"})
# print(second)
# third=con.find_next('div',{'class':"css-1dbjc4n r-13awgt0 r-12vffkv"})
# print(third)

# print(main_name.text)

# a=driver.get(url)
# # print(a)

# # react-root
# element=driver.find_element_by_id('react-root')
# elements=driver.find_element_by_tag_name('div')
# print(element.text)
# print(elements.text)
# driver.quit()









from ast import parse
from asyncore import read
from base64 import decode
from encodings import utf_8
from pprint import PrettyPrinter
from random import random
from textwrap import indent
from typing import IO, final
import requests
from bs4 import BeautifulSoup

import requests

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
#     'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE%2FyjvSFlFJR45yIlYF%2Bw%3D%3D; _sl=1; att=1-rDMoiFqRmEVyAThTbPOrnt0blYMf2kreo5zx1kkQ; gt=1501075314654744576; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210',
# }


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
    'referer': 'https://twitter.com/ANI',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'guest_id_marketing=v1%3A164518841345234428; guest_id=v1%3A164518841345234428; guest_id_ads=v1%3A164518841345234428; personalization_id="v1_MObpKSkvrBOQ2NvNjLUGsQ=="; g_state={"i_p":1645195694014,"i_l":1}; _gid=GA1.2.1744467814.1645976846; des_opt_in=Y; _gcl_au=1.1.582248905.1646033245; mbox=PC#6ec026fe571049188ca02d803345442f.31_0#1709292756|session#0d0ca6a8c9834368a484506c96af88cb#1646049816; _ga_34PHSZMC42=GS1.1.1646047955.3.1.1646047993.0; _ga=GA1.2.2103790272.1645188481; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|ziZgIoZIK4nlMKUVLq9KcnBFms0d9TqBqrE2FyjvSFlFJR45yIlYF%2Bw%3D%3D; _sl=1; att=1-rDMoiFqRmEVyAThTbPOrnt0blYMf2kreo5zx1kkQ; gt=1501075314654744576; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; kdt=iM8rNH2sPQNcvfaTWebZ0o3fpRgtwxNxBGMV5aKL; auth_token=c9266ed14a4c27a10601875ff4694f8740422710; ct0=ada7b85b23cf557fe31fb21d7f7c5d63b1eab9d4d078842fea24d9dc331221d8c24ca3e86bb7bb9947a99b9925e8930d259aa9fe3b8d6e28861bffa608a2b4e533016ff1bf5df99530345fc977258997; twid=u%3D1501092726502494210',
}




# number of tweet/items user want
# sas=int(input("enter: "))
sas=int(20)

# print(sas)

params = (
    ('variables', '{"userId":"355989081","count":'+f'{sas}'+',"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}'),
)

# print(params)

response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets?variables=%7B%22userId%22%3A%22355989081%22%2C%22count%22%3A40%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text_enabled%22%3Atrue%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)

soup=BeautifulSoup(response.content,'html.parser')
# print(soup.text)

# to make json file
# file=open('teett1.json','w',encoding='utf-8')
# file.write(str(soup))
# file.close()


# to read json file
import json
with open('C:\\Users\\KPRRS\\teett1.json',encoding='utf-8') as source_json:
    read_context=json.load(source_json)



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







# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# j=10
# for i in obj1:
#     if (i.get('type')=='TimelineAddEntries'):
#         i['entries']
#         # time
#         b=i['entries']
#         print(len(b))

#         for i in range(len(b)):
#             print(b[i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])

# print(len(obj1))
# for k in range(j):
    # for i in obj1:
    #     if (i.get('type')=='TimelineAddEntries'):
    #         # time
    #         print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
    # print(k)

# media
# print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['media_url_https'])
# print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['type'])
# print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['url'])

# text
# print(i['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])








# ~!~!~!~!~!
# obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# for i in obj1:
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
#                     print("Inbetween Messenger")





obj1 = read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# print(obj1)
for i in obj1:
    if i.get('type')=='TimelineAddEntries':
        a=i['entries']
        for j in a:
            if j['content'].get('entryType')=="TimelineTimelineModule":
                at=j['content']['items']
                for l in at:
                    # print(l['item']['itemContent'].get('itemType')=="TimelineTweet") true or false
                    if l['item']['itemContent'].get('itemType')=="TimelineTweet":
                        mj=(l['item']['itemContent']['tweet_results']['result'])
                        print(mj['legacy']['created_at'])
                        print(mj['legacy']['full_text'])
                        mj=(l['item']['itemContent']['tweet_results']['result']['legacy']['entities'])
                        try:
                            aa=(mj['media'])
                            for i in aa:
                                print(i['media_url_https'])
                                print(i['type'])
                        except:
                            print()
                    # for g in oh:
                    #     print(g)
    # if (i.get('type')=='TimelineTimelineModule'):
    #     print(i)
#         a=i['entries']
#         print(a)
        # for j in a:
            # working
            # if j['content'].get('entryType')=="TimelineTimelineItem":
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            # print()
            
            # temp (testing)
            # if j['content'].get('entryType')=="TimelineTimelineItem":
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
            #     print(j['content']['itemContent']['tweet_results']['result']['legacy']['full_text'])
            #     try:
            #         abab=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]
            #         if abab:
            #         # media url
            #             print(abab['media_url_https'])
            #         # media type
            #             # print(j['type'])
            #     except:
            #         print("Inbetween Messenger")
                    # print("Inbetween other non media content check if there are no media this message will be there")
                # print(j['content']['itemContent']['tweet_results']['result']['legacy']['created_at'])
                # if j['content']['itemContent']['tweet_results']['result']['legacy']['entities']:
                    # print(j['entities'])
                #     continue
                #     print(j)
            # else:
                # aa=j['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media']
                # print(aa)
                # for n in aa:
                #     print(n[0])

            # print()

                # print(ook)
        # specific
        # i['entries'][0]['content'].get("entryType")=="TimelineTimelineItem"
        # al=['entries'][1]['content']
        # if (al.get("entryType")=="TimelineTimelineItem"):
        #     print(al)
        
        
# print(i)
# print(len(b))
# ab=i['entries'][0]['content']
# print(len(b))
# for i in range(len(b)):
#     if (ab.get("entryType")=="TimelineTimelineItem"):
#         print(ab)
#         # aba=ab['itemContent']['tweet_results']['result']['legacy']['created_at']
#         # print(aba)
#     else:
#         continue

#     # i['itemContent']
#     print(i)






# if i.get == 'TimelineAddEntries':
# print(i.get('type')=='TimelineAddEntries')
# i['entries'][1]['content']['itemContent']['tweet_results']







# multiple time
# j=sas
# i=1
# k=2
# for i in range(j):
#     if i==3 or i==6 or i==12 or i==13 or i==15 or i==17 or i==18:
#         continue
#     print(i)
#     a=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
#     b=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
#     print(a)
#     print(b)
#     print()
    # print(aa)
    # print(bb)



# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)


# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][0]['content']['items'][1]['item']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)



# solve error
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][9]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)

# a=[0,1,2,3,4,5,6,7,8,9]
# b=[]
# for i in a[0:10]:
#     if i==3:
#         a.remove(i)
#         # b.append(i)
#     elif i!=3:
#         print(i)
# print(b)
# print(a)



# a.remove(1)

# error
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][3]['content']['items'][0]['item']['itemContent']



# solve error
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][4]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)

# 2nd check
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][sas-1]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['normal_followers_count']
# print(question_access)

# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][sas-1]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)

# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][sas-1]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
# print(question_access)


# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][sas-1]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
# print(question_access)










# name
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['in_reply_to_screen_name']
# print(question_access)


# follower count
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['normal_followers_count']
# print(question_access)


# time
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
# print(question_access)


# photo1
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['media_url_https']

# hashtag
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['hashtags'][0]['text']

# photo2
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][0]['media_url_https']

# photo3
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][1]['media_url_https']

# photo4
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][2]['media_url_https']


# photo5
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][3]['media_url_https']


# text
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']


# types
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0]['type']
# print(question_access)





# from operator import itemgetter
# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# for x in sorted(question_access,key=itemgetter('height')):
#     print(x)


# print(json.dumps(read_context,indent=3))

# print(type(read_context))
# access=read_context['data']['user']['result']['__typename']
# print(access['timeline_v2'])

# question_access=read_context['data']['user']['result']['timeline_v2']['timeline']['instructions']
# print(question_access)
# for i in question_access:
#     header=i.keys()
#     print(header)



# print(question_access)
# next=question_access[1]
# a=next['entries']
# b=a[0]
# c=b['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']['entities']['description']['urls']
# # d=c['tweet_results']
# print(c)
# print(type(c))



# temporary
# soup=BeautifulSoup(response.content,'lxml')
# print(soup)

# profile_image_url_https
# description

# print(soup)
# print(type(soup))

# print(response.content)
# print(soup.prettify)

