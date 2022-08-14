from django.urls import path
from . import views


urlpatterns = [
    path('ping', views.ping, name="sping"),
    path('echo_post_json', views.echo_post_json, name="echo_post_json"),
    path('tweets/create', views.create_tweet, name="create_tweet")
]