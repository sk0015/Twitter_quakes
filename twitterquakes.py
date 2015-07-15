
#API key ypoWX7AprOVl3JtDGpyim4Pml
#API secret Nba9QGUnyqjONpXVpxIHr91fxiXNwkM2n0fzusElB3Yxs1oLwT
#Access Token 357659097-TPpkTUmdOzUliaSK7nEVrxFHRia0Nqdo51Tgavnq
#Access Token Secret lY28UdmztzjaRipNIDsNvVWqWdRUeiWKSdg9Y0imEkzx2


#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "357659097-TPpkTUmdOzUliaSK7nEVrxFHRia0Nqdo51Tgavnq"
access_token_secret = "lY28UdmztzjaRipNIDsNvVWqWdRUeiWKSdg9Y0imEkzx2"
consumer_key = "ypoWX7AprOVl3JtDGpyim4Pml"
consumer_secret = "Nba9QGUnyqjONpXVpxIHr91fxiXNwkM2n0fzusElB3Yxs1oLwT"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 
    stream.filter(track=['python', 'javascript', 'ruby'])