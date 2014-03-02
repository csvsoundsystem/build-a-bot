from twython import TwythonStreamer

# twitter credentials
APP_KEY = 'yw06xDxHupA0d9NV7WLAg',
APP_SECRET = 'I0cokOO1gul7rpshZvIKq8inSyJuAfQnUkPYedOSko',
OAUTH_TOKEN = '2368977744-SNU9GJ3pWV12e9U3lDNpklrSlpRpbcg7sghWTUi',
OAUTH_TOKEN_SECRET = 'i5OqTSokHXRwUTh6SM6C6eL9Cb8b9LUg7uWgLaaoDpG5H'

class MyStreamer(TwythonStreamer):
  def on_success(self, data):
      print "hello"

  def on_error(self, status_code, data):
      print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='twitter')
