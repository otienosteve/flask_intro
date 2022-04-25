from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    data="Flask is a Microframework"
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return "<h1>This is the About Page<h1>"


@app.route('/serve')
def services():
    return "<h2>Services<h2>"

if __name__=='__main__':
    app.run(debug=1)
