#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                abort(400, description="Error: Division by zero")
            result = num1 // num2  # Change this line for integer division
        elif operation == '%':
            result = num1 % num2
        else:
            abort(400, description="Error: Invalid operation")
    except Exception as e:
        abort(500, description=str(e))

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
