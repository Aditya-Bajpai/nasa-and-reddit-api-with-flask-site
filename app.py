from flask import Flask , render_template
import praw
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import apod_object_parser
import os
from config import api_key , password , client_secret , client_id
app = Flask(__name__)
pp = PrettyPrinter()


response = apod_object_parser.get_data(api_key)




picture = apod_object_parser.get_url(response)

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username="Adi_who_doesnt_simp",
                    password=password,
                    user_agent="prawpraw",
                    check_for_async=False)

subreddit = reddit.subreddit('aww')
hot  = subreddit.hot(limit = 50)




title = apod_object_parser.get_title(response)
@app.route('/')
def main():
    return render_template('main.html' , hot = hot)

@app.route('/nasa')
def nasa():
    return render_template('nasa.html' , picture=picture, title = title)

print(picture)

if __name__ == "__main__":
    app.run(debug=True)
