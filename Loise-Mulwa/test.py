from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def landingpage():
   
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/facts')
def contact():
    return render_template('facts.html')

if __name__=='__main__':
    app.run(debug=1)
