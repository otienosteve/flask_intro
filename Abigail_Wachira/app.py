from flask import Flask
web = Flask(__name__)

@web.route('/')
def home():
    return '<h1> This is the Home Page</h1>'

@web.route('/about')
def about():
    return '<h2> This is the page where you learn everything about this app. </h2>'

@web.route('/demo')
def demo():
    return '<h3> This is a demonstration of how the app works. </h3>'

@web.route('/contacts')
def contacts():
    return '<p> Incase of any questions, feel free to to contact us on 0712345678</p>'

if __name__ == '__main__':
    web.run(debug = True)