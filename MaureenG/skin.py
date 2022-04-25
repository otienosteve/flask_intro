from flask import Flask,render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def about():
    return render_template('products.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def officehours():
    return render_template('contacts.html')


if __name__=='__main__':
    app.run(debug=1)