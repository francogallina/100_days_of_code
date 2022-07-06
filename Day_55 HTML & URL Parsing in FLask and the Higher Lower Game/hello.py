from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return "Bye!"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"

@app.route('/<names>/<path:apellido>')
def greeting(names, apellido):
    return f"Hello {names} de apellido {apellido}!"

if __name__ == "__main__":
    app.run(debug=True)

