from django.urls import include, path

urlpatterns = [
    path('',include("twitter_tool.urls")),
]
