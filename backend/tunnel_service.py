
import requests
from flask import jsonify
graph_url = 'https://graph.facebook.com/v16.0/'

class TunnelService:

    def getHashData(hashtag_name):
        accessToken = 'EAAMsiJ2hwv0BAN2ZB5bSRBbB4Vo0W8FjuLbbfgXZCXr3Eg5EC6XusXDJSMD4Q8cGwmZBmWDbRlZAZCUw6sRCA78l2WGtXPhZCdGroveu0MIrt5gyGSIGNiVI3GD8wDrWn90roAICg8tYnMsJyZAPhqdi4mAZA8PX63int7nmfzIrdnCbGduBnQ33p7VokspF7tE3vOmPD5t1gELS9lBwy8jG4bVJ7FZAygP7quYFdzj7bze7jyXo1mmKx-------------------------------------------------------'
        instagramAccid = ""
        hashtag = hashtag_name
        hashtagId = TunnelService.get_hashtag_id(hashtag, instagramAccid, accessToken)
        print(hashtagId)
        TunnelService.get_data_of_hashtag(hashtagId, accessToken)
        response = TunnelService.get_recent_media(hashtagId, accessToken, instagramAccid)
        return response['data']

    def get_hashtag_id(hashtag='', instagram_account_id='', access_token=''):
        url = graph_url + 'ig_hashtag_search'
        param = dict()
        param['user_id'] = instagram_account_id
        param['q'] = hashtag
        param['access_token'] = access_token
        response = requests.get(url, param)
        response = response.json()
        print(response['data'])
        hashtag_id = response['data'][0]['id']
        return hashtag_id

    def get_data_of_hashtag(hashtag_id='', access_token=''):
        url = graph_url + hashtag_id
        param = dict()
        param['access_token'] = access_token
        param['fields'] = 'id,name'
        response = requests.get(url, param)
        response = response.json()
        return response

    def get_recent_media(hashtag_id='', access_token='', instagram_account_id=''):
        url = graph_url + hashtag_id + '/top_media'
        param = dict()
        param['access_token'] = access_token
        param['user_id'] = instagram_account_id
        param['fields'] = 'caption,permalink,comments_count,like_count,media_type,media_product_type,media_url,timestamp'
        response = requests.get(url, param)
        response = response.json()
        print(response)
        return response



