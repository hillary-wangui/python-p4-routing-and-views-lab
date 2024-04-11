from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:value>')
def print_string(value):
    print(value)
    return value

@app.route('/count/<int:num>')
def count(num):
    return '<br>'.join(str(i) for i in range(num + 1))

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
