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
    
    def like_tweet(self, like_exec_user_id, tweet_id):
        """
        like_exec_user_id: likeする側のユーザID
        tweet_id: likeするツイートのID
        """
        payload = {
            "tweet_id": tweet_id
        }
        response = self.oauth.post(
            "https://api.twitter.com/2/users/{}/likes".format(like_exec_user_id), json=payload
        )
        return response

    def unlike_tweet(self, unlike_exec_user_id, tweet_id):
        """
        unlike_exec_user_id: unlikeする側のユーザID
        tweet_id: unlikeするツイートのID
        """
        response = self.oauth.delete(
            "https://api.twitter.com/2/users/{}/likes/{}".format(unlike_exec_user_id, tweet_id)
        )
        return response