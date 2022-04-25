from flask import Flask, render_template
web = Flask(__name__)

@web.route('/')
def home():
    return render_template('home.html')

@web.route('/about')
def about():
    return render_template('about.html')

@web.route('/demo')
def demo():
    return render_template('demo.html')

@web.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    web.run(debug = True)