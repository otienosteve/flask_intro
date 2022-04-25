
from flask import Flask, appcontext_popped
web = Flask(__name__)


def home():
  return '<h1>Hi there!</>'
web.add_url_rule('/',view_func=home)


if __name__ == '__main__':
    web.run(debug = True)