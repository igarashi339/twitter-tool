from requests_oauthlib import OAuth1Session


class TwitterApiV2Handler:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

    def create_tweet(self, text, media_ids):
        payload = {
            "text": text
        }
        if media_ids:
            payload["media"] = {
                "media_ids": media_ids,
                "tagged_user_ids": []
            }
        response = self.oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )
        return response
