<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is a Food Delivery Website!'

if __name__== '__main__':
=======
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is a Food Delivery Website!'

if __name__== '__main__':
>>>>>>> 849526a5728286609d4442bfe24f41cc5f5690de
    app.run(debug=True) 