from TwitterListener import *

AMOUNT = 0.1
STOP_ENTRY_PERCENTAGE = 5
STOP_LOSS_PERCENTAGE = 5
TRACK_TERMS = []
FOLLOW_TERMS = [1438561350536605698]


def main():
    # Creates a twitter listener that gets lives tweets.
    streamer = Listener(TWITTER_APP_KEY, TWITTER_APP_SECRET, TWITTER_KEY, TWITTER_SECRET)
    streamer.filter(follow=FOLLOW_TERMS, track=TRACK_TERMS)


if __name__ == '__main__':
    main()
