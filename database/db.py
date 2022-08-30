import sqlite3

con = sqlite3.connect("database/shorturl.sqlite", check_same_thread=False)
cur = con.cursor()

# cur.execute("""
#     CREATE TABLE urls 
#         (   
#             unique_id, 
#             short_url, 
#             long_url,
#             PRIMARY KEY (unique_id)
#         )
#     """)