from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/service')
def services():
    return render_template('service.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')


if __name__=='__main__':
    app.run(debug=1)




