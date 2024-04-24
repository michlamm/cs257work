import flask
import psycopg2

app = flask.Flask(__name__)

@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    answer = int(num1) + int(num2) 
    return str(answer)

@app.route('/pop/<abbrev>')
def abbrev():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")

    cur = conn.cursor()

    pop = "select population from population where code = %s"
        cur.execute(pop)
        row1 = cur.fetchone()
    
    return row1

if __name__ == '__main__':
    my_port = 5105
    app.run(host='0.0.0.0', port = my_port) 
