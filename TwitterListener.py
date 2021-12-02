import tweepy
from KucoinAPI import *

from main import *

TWITTER_APP_KEY = "k5YYDnyX8emlhwX6pD9vPdcpA"
TWITTER_APP_SECRET = "Ro3D9nv14ljkMSzk3hV7VaOTHSz4mUkoOQHP0oZufKRebqpwmP"
TWITTER_KEY = "1044602734652067841-n1nEZXXmwhkCLcnkf9uv8RfUZMKgGu"
TWITTER_SECRET = "j64qHXgvHTTu1Vuzm5RnY088pNAXxhJLbFFxqj6UfOnVr"


class Listener(tweepy.Stream):

    def on_status(self, status):
        text = status.text
        if '$' in text:
            index = text.find('$')
            self.currency = text[index + 1:index + 5].replace(" ", "")

            currency1 = self.currency
            currency2 = 'USDT'

            final_action(currency1, currency2, AMOUNT)
