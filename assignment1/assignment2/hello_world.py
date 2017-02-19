from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/birthday")
def birthday():
    return 'My birthday is: December 17, 1978'


@app.route("/greeting/<name>")
def greeting(name):
    return "Hello " + name + "!"


@app.route("/sum/<int:number1>/<int:number2>/")
def add(number1, number2):
    result = number1 + number2
    return str(result)

# @app.route('/sum/<int:num1>/<int:num2>/')
# def add(num1, num2):
#     answer = num1 + num2
#     return str(answer)


# @app.route("/multiply/<int:a>/<int:b>/")
# def multiply(a, b):
#     result = a * b
#     print (result)
#     return str(result)

@app.route('/multiply/<num1>/<num2>/')
def multiply(num1, num2):
    num1, num2 = int(num1), int(num2)
    result = num1 * num2
    return str(result)

if __name__ == "__main__":
    app.run()