from rest_framework.response import Response
from rest_framework.decorators import api_view
from twitter_api_v2_handler import TwitterApiV2Hander
from db_handler import DbHandler
import json

@api_view(["GET"])
def ping(request):
    return Response("OK")


@api_view(["POST"])
def echo_post_json(request):
    try:
        json_data = json.loads(request.body)
        return Response({
            "message": "次の入力を受け付けました",
            "input": json_data
        })
    except:
        return Response("パラメタのパースに失敗しました。")

@api_view(["POST"])
def create_tweet(request):
    try:
        json_data = json.loads(request.body)
        twitter_tool_user_id = json_data["twitter-tool-user-id"]
        twitter_username = json_data["twitter-username"]
        text = json_data["text"]
    except Exception as e:
        return Response("Jsonのパースに失敗しました。")
    db_handler = DbHandler()
    consumer_key, consumer_secret, access_token, access_token_secret = db_handler.get_keys(twitter_tool_user_id, twitter_username)
    twitter_api_v2_handler = TwitterApiV2Hander(consumer_key, consumer_secret, access_token, access_token_secret)
    twitter_api_v2_handler.create_tweet(text)
