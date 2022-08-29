from flask import Flask
from flask import request
import sqlite3

import shortuuid

con = sqlite3.connect("shorturl.db", check_same_thread=False)
cur = con.cursor()

long_url = "https://roadmap.sh/python"

shortuuid.set_alphabet("0123456789")
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_to_base_62(num: int, alphabet):
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append
    _divmod = divmod
    base = len(alphabet)
    while num: 
        num, rem = _divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return "".join(arr)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_url_type():

    if request.method == "GET":
        # check if short_url in DB? fetch

        # redirect to fetched short_url
        return "short url application"

    if request.method == "POST":
        # generate unique id
        unique_id = int(shortuuid.uuid())
        # convert unique id to hash in base 62
        hashed_unique_id = encode_to_base_62(num=unique_id, alphabet=BASE62)
        # save in DB
        print(unique_id)
        print(hashed_unique_id)
        cur.execute(f"INSERT INTO short_urls VALUES ( {unique_id} , '{hashed_unique_id}' , '{long_url}' )")
        con.commit()
        # return shorten url to user
        return {
           "shorturl": f"http://localhost:5000/{hashed_unique_id}"
        }

