from dotenv import load_dotenv
import os


class DbHandler():
    def __init__(self):
        load_dotenv()
    
    def get_keys(self, twitter_tool_user_id, twitter_username):
        consumer_key = os.getenv("CONSUMER_KEY")
        consumer_secret = os.getenv("CONSUMER_SECRET")

        # TODO:twitter_tool_user_id, twitter_usernameをキーにして、DBからaccess_tokenとaccess_token_secretを取得する
        if twitter_tool_user_id == "1" and twitter_username == "devjima":
            access_token = os.getenv("ACCESS_TOKEN")
            access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        else:
            access_token = ""
            access_token_secret = ""
        
        return consumer_key, consumer_secret, access_token, access_token_secret
    
    def get_userid_from_username(self, username):
        # todo: username -> userid のマッピングはDBに保持するようにする
        if username == "devjima":
            userid = os.getenv("USERID")
        elif username == "igarashi20608":
            userid = "2424817662"
        else:
            userid = "0000"
        return userid