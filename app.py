from flask import Flask, render_template, redirect, url_for
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = 6379

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("visitor_count")
    return render_template("index.html", count=count)

@app.route("/reset", methods=["POST"])
def reset():
    r.set("visitor_count", 0)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
