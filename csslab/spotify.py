
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template("spotify.html") #can also click hello and goodbye to change

if __name__ == '__main__':
    my_port = 5105

    app.run(host='0.0.0.0', port = my_port) 
