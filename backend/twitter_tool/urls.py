from django.urls import path
from . import views


urlpatterns = [
    path('ping', views.ping, name="sping"),
    path('echo_post_json', views.echo_post_json, name="echo_post_json"),
    path('tweets/create', views.create_tweet, name="create_tweet"),
    path('likes/create',views.create_like, name="create_like"),
    path('likes/delete',views.delete_like, name="unlike_tweet"),
    path('media/upload', views.upload_media, name="delete_like")
]