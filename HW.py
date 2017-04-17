from bottle import route, run
from bottle import template

@route('/hello')
def hello():
    return "Hello World!"

@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host='localhost', port=8080, debug=True)