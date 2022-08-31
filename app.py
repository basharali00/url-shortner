import shortuuid
from db import create_connection, execute_sql_file
from utils import encode_to_base_62

from flask import Flask, request, render_template, redirect

shortuuid.set_alphabet("0123456789")
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

app = Flask(__name__)

connection = create_connection("db/database.db")
execute_sql_file("db/schema.sql", connection=connection)
cursor = connection.cursor()

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
        cursor.execute(f"INSERT INTO urls VALUES ( {unique_id} , '{hashed_unique_id}' , '{long_url}' )")
        connection.commit()
        shorten_url = f"http://localhost:5000/{hashed_unique_id}"

    # render main page
    return render_template("index.html", shorten_url=shorten_url)

@app.route("/<url>")
def redirect_url(url):
    cursor.execute("SELECT long_url FROM urls WHERE short_url=?", (url,))
    row = cursor.fetchone()
    long_url = row[0]    
    return redirect(long_url, code=301)