import asyncio
from twikit import Client, TooManyRequests
from configparser import ConfigParser
from random import randint
import time
import csv

# Minimum tweets to retrieve
MINIMUM_TWEETS = 4000
QUERY = 'ipl lang:en'

async def get_tweets(client, tweets):
    if tweets is None:
        print("...Getting Tweets...")
        client.load_cookies('cookies.json')  # Uncomment this if you are using saved cookies
        # Get tweets
        tweets = await client.search_tweet(QUERY, product='Top')  # Await the coroutine
    else:
        wait_time = randint(5, 10)
        print(f"...Getting next tweets after {wait_time} seconds...")
        await asyncio.sleep(wait_time)  # Use asyncio.sleep instead of time.sleep
        tweets = await tweets.next()  # Await the coroutine
    return tweets

# Load credentials
config = ConfigParser()
config.read('config.ini')
username = config['X']['username']
email = config['X']['email']
password = config['X']['password']

# Create the CSV file and write headers (done once before collecting tweets)
with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet_count', 'Username', 'Location', 'Created At', 'Likes', 'Text'])

# Initialize the client
client = Client(language='en-US')

async def start():
    tweet_count = 3820  # Initialize the tweet count
    tweets = None  # Initialize tweets variable
        
    while tweet_count < MINIMUM_TWEETS:
        try:
            tweets = await get_tweets(client, tweets)  # Pass the client and await

            if not tweets:
                print(" - No more tweets found -")
                break

            # Process each tweet
            for tweet in tweets:
                if tweet.lang == 'en':  # Filter for English tweets
                    tweet_count += 1  # Increment tweet count
                    tweet_data = [tweet_count, tweet.user.name, tweet.user.location, tweet.created_at, tweet.favorite_count, tweet.text]

                    with open('tweets.csv', 'a', newline='', encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerow(tweet_data)

            # After all tweets are processed, print the tweet count
            print(f"Total tweets retrieved: {tweet_count}")

        except TooManyRequests:
            print("Rate limit exceeded. Please try again later.")
            await asyncio.sleep(60)  # Sleep for a minute before retrying
        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Running the async function
if __name__ == '__main__':
    asyncio.run(start())
