import shortuuid
from database import con
from utils import encode_to_base_62

from flask import Flask, request, url_for, render_template, redirect

cur = con.cursor()

shortuuid.set_alphabet("0123456789")
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    shorten_url = None
    if request.method == "POST": 
        # generate unique id
        unique_id = int(shortuuid.uuid())
        # convert unique id to hash in base 62
        hashed_unique_id = encode_to_base_62(num=unique_id, alphabet=BASE62)
        # extract long_url from request
        long_url = request.form["long_url"]
        # save in DB
        cur.execute(f"INSERT INTO urls VALUES ( {unique_id} , '{hashed_unique_id}' , '{long_url}' )")
        con.commit()

    # render main page
    return render_template("index.html", shorten_url=shorten_url)
