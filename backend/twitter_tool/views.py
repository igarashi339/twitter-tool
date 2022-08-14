from rest_framework.response import Response
from rest_framework.decorators import api_view
from twitter_tool.twitter_api_v2_handler import TwitterApiV2Handler
from twitter_tool.db_handler import DbHandler
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
    except:
        return Response("Jsonのパースに失敗しました。")

    try:
        db_handler = DbHandler()
        consumer_key, consumer_secret, access_token, access_token_secret = db_handler.get_keys(twitter_tool_user_id, twitter_username)
    except:
        return Response("キー情報の取得に失敗しました。")

    if access_token == "" or access_token_secret == "":
        return Response(f"twitter-tool-user-id={twitter_tool_user_id}, twitter-user-name={twitter_username}のユーザが存在しません。")

    try:
        twitter_api_v2_handler = TwitterApiV2Handler(consumer_key, consumer_secret, access_token, access_token_secret)
        response_str = twitter_api_v2_handler.create_tweet(text)
        return Response(response_str)
    except:
        return Response("ツイートの投稿に失敗しました。")

