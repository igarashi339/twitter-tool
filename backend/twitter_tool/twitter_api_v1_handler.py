from requests_oauthlib import OAuth1Session


class TwitterApiV1Handler:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

    def upload_media(self, media_data):
        target_url = "https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image"
        payload = {
            "media_data": media_data
        }
        response = self.oauth.post(
            target_url,
            files=payload
        )
        return response
