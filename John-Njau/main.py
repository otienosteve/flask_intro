import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "Flask Basics"
    flask= "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks. Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy."
    return render_template('index.html', title=title, flask=flask)

@app.route('/about')
def about():
    about = "About Flask"
    return render_template('about.html', about=about)

@app.route('/deps')
def dependencies():
    deps = "Flask Dependencies"
    return render_template('dependencies.html', deps=deps)

@app.route('/more')
def more():
    more="More about Flask"
    return render_template('more.html', more=more)

if __name__ == '__main__':
    app.run(debug=True)