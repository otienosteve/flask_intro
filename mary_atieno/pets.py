from flask import Flask, render_template
pet = Flask(__name__)


@pet.route('/')
def about():
    return render_template('about.html')


@pet.route('/home')
def home():
    return render_template('home.html')


@pet.route('/services')
def services():
    return render_template('services.html')  


@pet.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')        


if __name__ == '__main__':
    pet.run(debug=True)
