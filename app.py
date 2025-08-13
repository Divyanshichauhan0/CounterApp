from flask import Flask,render_template,redirect,url_for
from replit import db
app = Flask(__name__)

db ={'number':0}

@app.route('/')
def home():
    message = ""
    # put application's code here
    return render_template('index.html',number=db['number'],message=message)


@app.route('/increment',methods=['POST'])
def increment():
    message = ""
    db['number'] += 1
    return render_template('index.html', number=db['number'],message=message)

@app.route('/decrement', methods=['POST'])
def decrement():
    message = ""
    if db['number'] <=  0:
        return render_template('index.html', number=db['number'], message="Your counter can't count below 0")
    db['number'] -= 1
    return render_template('index.html', number=db['number'],message=message)


if __name__ == '__main__':
    app.run(debug=True)

