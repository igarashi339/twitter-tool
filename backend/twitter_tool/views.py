from rest_framework.response import Response
from rest_framework.decorators import api_view
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

