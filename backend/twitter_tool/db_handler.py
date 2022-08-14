from dotenv import load_dotenv
import os

def DbHandler():
    def __init__(self):
        load_dotenv()
    
    @staticmethod
    def get_keys(self, twitter_tool_user_id, twitter_username):
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        
        # TODO: twitter_tool_user_id, twitter_usernameをキーにして、
        # DBからaccess_tokenとaccess_token_secretを取得する
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        
        return consumer_key, consumer_secret, access_token, access_token_secret