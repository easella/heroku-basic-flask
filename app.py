from flask import Flask
import jinja2
from requests import get
from flask_redis import FlaskRedis
app = Flask(__name__)
redis_client = FlaskRedis(app)

SITE_NAME = 'https://games.awdrgyjil1234.repl.co/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  resp = get(f'{SITE_NAME}{path}')
  if resp.headers.get('content-type'):
    return resp.content
  return resp.text
  
if __name__ == '__main__':
  app.jinja_env.cache = {}
  app.run(host='0.0.0.0', port=8080)
