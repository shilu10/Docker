from flask import Flask, render_template, render_template_string
from redis import Redis


app = Flask(__name__)

redis = Redis(host = 'redis-server', port = 6379)
redis.set('visits', 1)


@app.route("/")
def home() :
    number_of_visits = redis.get('visits')
    redis.set('visits', int(number_of_visits)+1 )
    return render_template_string(f"Number of Visits to my page is : {number_of_visits}")
    

app.run(port = 30000, debug = True, host = '0.0.0.0')
