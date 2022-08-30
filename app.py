from flask import Flask, request, url_for, render_template

import shortuuid
from database import con
from utils import encode_to_base_62


cur = con.cursor()

shortuuid.set_alphabet("0123456789")
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

app = Flask(__name__)

@app.get("/url")
def handle_url_type():
    # check if short_url in DB? fetch

    # redirect to fetched short_url
    return "short url application"

@app.post("/")
def shorten_url():
    # generate unique id
    unique_id = int(shortuuid.uuid())
    # convert unique id to hash in base 62
    hashed_unique_id = encode_to_base_62(num=unique_id, alphabet=BASE62)
    # save in DB
    cur.execute(f"INSERT INTO short_urls VALUES ( {unique_id} , '{hashed_unique_id}' , '{long_url}' )")
    con.commit()
    # return shorten url to user
    return {
        "shorturl": f"http://localhost:5000/{hashed_unique_id}"
    }
