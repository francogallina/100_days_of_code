from flask import Flask

app = Flask(__name__)

def bold_function(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def emphasis_function(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def underline_function(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route('/')
@bold_function
@emphasis_function
@underline_function
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
