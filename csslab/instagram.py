from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def instagram():
    return render_template("instagram.html")

if __name__ == '__main__':
    my_port = 5105

    app.run(host='0.0.0.0', port = my_port) 
